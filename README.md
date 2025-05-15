# 🛡️ Human Detection Alert System using YOLOv8

This is a Python-based real-time human detection system using YOLOv8 and OpenCV. When a person is detected in a video stream, the system captures a snapshot and sends an email alert with the image attached.

## 🚀 Features

- Real-time human detection using YOLOv8
- Draws bounding boxes on detected persons
- Saves the detected frame as an image
- Sends email notifications with the attached image
- Supports video files or webcam input

## 📦 Requirements

- Python 3.8+
- [OpenCV](https://opencv.org/)
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)

Install required libraries:

```bash
pip install opencv-python ultralytics
