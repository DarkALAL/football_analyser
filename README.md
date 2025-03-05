# Football Analysis

## Introduction
The goal of this project is to detect and track players, referees, and footballs in a video using YOLO—one of the most advanced AI object detection models available. In addition to leveraging YOLO for initial object detection, the model will be further trained to enhance its performance over time. To distinguish teams on the field, players will be assigned to teams based on the colors of their t-shirts through K-means pixel segmentation and clustering techniques. This information will then be used to calculate each team's ball acquisition percentage during a match.

Furthermore, the project employs optical flow algorithms to measure camera movement between frames, which enables the precise tracking of individual player movements. By applying perspective transformation, the scene’s depth and perspective are accurately represented, allowing for the measurement of player movement in meters instead of pixels. These calculations will also provide key metrics such as player speed and distance covered.

To enhance user experience and accessibility, a simple yet professional frontend and backend have been developed using Flask. This integration offers an intuitive and streamlined interface, ensuring that both beginners and experienced machine learning engineers can easily interact with and benefit from the system.

![Screenshot](output_videos/screenshot.png)

## Modules Used
The following modules are used in this project:
- YOLO: AI object detection model
- Kmeans: Pixel segmentation and clustering to detect t-shirt color
- Optical Flow: Measure camera movement
- Perspective Transformation: Represent scene depth and perspective
- Speed and distance calculation per player

## Trained Models
- [Trained Yolo v5xu](https://drive.google.com/drive/folders/1tS4um8lus-l4OJ5DOA04bYQrIJsrBK8Q?usp=sharing)

## Sample video
-  [Sample input video](https://drive.google.com/drive/folders/1bgE6JcS-VgFr3FsZl8BfevK-o4hE3OPH?usp=sharing)

## Requirements
To run this project, you need to have the following requirements installed:
- FFmpeg
- Python 3.x
- ultralytics
- supervision
- Flask
- watchdog
- OpenCV
- NumPy
- Matplotlib
- Pandas

# Instructions
- Create a virtual environment and activate it.
- Install the requirements from the file `requirements.txt` to an virual environment with the command:
  `pip install -r requirements.txt`
- Now start the `app.py` using the command:
  `python3 app.py`
- Now go to `http://127.0.0.1:5000` on your local machine and upload the video from the `sample videos`.