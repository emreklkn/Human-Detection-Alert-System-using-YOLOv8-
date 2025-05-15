# -*- coding: utf-8 -*-
"""
Created on Thu May 15 04:00:34 2025

@author: emrek
"""

import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from ultralytics import YOLO

# E-posta ayarları
def send_email(image_path):
    from_email = 'your_email@gmail.com'
    to_email = 'recipient_email@gmail.com'
    password = 'your_email_password'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'İnsan Tespiti Uyarısı'

    body = 'Kamerada bir insan tespit edildi.'
    msg.attach(MIMEText(body, 'plain'))

    with open(image_path, 'rb') as img:
        img_data = MIMEImage(img.read())
        msg.attach(img_data)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"E-posta gönderilemedi: {e}")

# YOLO modelini yükle
model = YOLO("yolov8n.pt")  # YOLOv8 modelini yükleyin

# Kamera aç
cap = cv2.VideoCapture('3.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # İnsan tespiti yap
    results = model(frame)
    for result in results:
        for box in result.boxes:
            if box.cls == 0:  # 0, 'person' sınıfının ID'sidir
                # Tespit edilen kişiyi çerçevele
                x1, y1, x2, y2 = box.xyxy[0]
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, "Person Detected", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                # Tespit edilen kişiyi içeren görüntüyü kaydet
                cv2.imwrite("detected_person.jpg", frame)

                # E-posta bildirimi gönder
                send_email("detected_person.jpg")

    # Sonuçları göster
    cv2.imshow("Kamera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
