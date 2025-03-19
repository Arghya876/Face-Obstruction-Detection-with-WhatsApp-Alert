import cv2
import time
import numpy as np
import pywhatkit as kit
import threading

YOUR_WHATSAPP_NUMBER = "+91XXXXXXXXX"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(3, 640)  
cap.set(4, 480)  

last_sent_time = 0
alert_interval = 5  
face_disappeared_time = None  

def send_whatsapp_message():
    try:
        kit.sendwhatmsg_instantly(YOUR_WHATSAPP_NUMBER, "⚠️ Alert! An object is covering your face!")
        print("WhatsApp message sent.")
    except Exception as e:
        print("Error sending WhatsApp message:", e)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) > 0:
        face_disappeared_time = None

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    else:
        if face_disappeared_time is None:
            face_disappeared_time = time.time()  

        time_elapsed = time.time() - face_disappeared_time

        if time_elapsed > 5:
            cv2.putText(frame, "Face Covered!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.rectangle(frame, (50, 100), (590, 400), (0, 0, 255), 2)  

            current_time = time.time()
            if current_time - last_sent_time > alert_interval:
                threading.Thread(target=send_whatsapp_message, daemon=True).start()
                last_sent_time = current_time

    cv2.imshow("Face Obstruction Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
