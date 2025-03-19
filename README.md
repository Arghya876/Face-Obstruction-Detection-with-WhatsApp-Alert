# Face Obstruction Detection with WhatsApp Alert

## Overview
This project detects if an object is obstructing a person's face using OpenCV and sends an alert message via WhatsApp using `pywhatkit`. If the face is covered for more than 5 seconds, the system automatically sends a WhatsApp message to a predefined number.

## Features
- Detects faces using OpenCV's Haar cascade classifier.
- Alerts when a face is covered for more than 5 seconds.
- Sends an automated WhatsApp message to notify about the obstruction.
- Uses threading to ensure smooth execution without delays.

## Technologies Used
- Python
- OpenCV (`cv2`)
- NumPy (`numpy`)
- PyWhatKit (`pywhatkit`)
- Threading (`threading`)

## How It Works
1. Captures real-time video from the webcam.
2. Detects faces using a pre-trained Haar cascade model.
3. If a face is detected, it continues tracking.
4. If the face disappears for more than 5 seconds, an alert message is displayed.
5. A WhatsApp message is sent to the specified phone number.

### Install Dependencies
```sh
pip install opencv-python numpy pywhatkit

