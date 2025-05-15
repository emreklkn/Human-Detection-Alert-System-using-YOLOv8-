🛡️ Human Detection Alert System using YOLOv8
This project is a real-time human detection system built with Python, YOLOv8, and OpenCV. When a person is detected in the video stream, the system takes a snapshot and automatically sends an email alert with the captured image.

🚀 Features
📦 Real-time human detection using YOLOv8

📷 Captures frames when a person is detected

📤 Sends email alerts with attached detection images

🎥 Works with video files or webcam
📁 Project Structure
bash

project-folder/
│
├── 3.py                   # Main Python script
├── yolov8n.pt             # YOLOv8 model (not included)
├── yolov4.weights         # (optional) YOLOv4 model weights
├── yolov4.cfg             # (optional) YOLOv4 configuration
├── coco.names             # Class labels
├── 3.mp4                  # Sample video input (not included)
├── detected_person.jpg    # Output image (generated dynamically)
├── .gitignore             # File to prevent uploading sensitive/large files
📦 Requirements
Python 3.8+

OpenCV

ultralytics

SMTP-supported email (Gmail or similar)

Install dependencies:

bash

pip install opencv-python ultralytics

🔐 Email Configuration
⚠️ Important: For security reasons, do NOT hardcode your email credentials. Store them in a separate config.json file (which is excluded from GitHub using .gitignore):

config.json

json
{
  "from_email": "your_email@gmail.com",
  "to_email": "recipient_email@gmail.com",
  "password": "your_app_password"
}
Then load it in your Python script:
import json
with open('config.json') as f:
    config = json.load(f)

from_email = config['from_email']
to_email = config['to_email']
password = config['password']
📥 Required Files (NOT Included in GitHub)
These files are required for the system to work but are excluded from this repository due to size or licensing:

File	Purpose	Download Link
yolov8n.pt	YOLOv8 model	Download from Ultralytics
yolov4.weights	YOLOv4 weights (optional)	Download
yolov4.cfg	YOLOv4 config (optional)	Download
coco.names	Class labels	Download
3.mp4	Test video	Provide your own or use any MP4 file

After downloading, place them in the project root directory.


