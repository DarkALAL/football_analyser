import cv2
import subprocess
import os

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames,output_video_path):
    temp_path = "temp_video.avi"
    fourcc= cv2.VideoWriter_fourcc(*'XVID')
    out= cv2.VideoWriter(temp_path,fourcc,24,(output_video_frames[0].shape[1],output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", temp_path, "-vcodec", "libx264", "-crf", "23", "-preset", "slow", output_video_path
    ]
    subprocess.run(ffmpeg_cmd)
    os.remove(temp_path)
    