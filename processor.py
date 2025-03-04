import os
import uuid
from datetime import datetime

class VideoProcessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(input_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

    def generate_filename(self, original_name):
        ext = original_name.split('.')[-1]
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        return f"processed_{timestamp}_{uuid.uuid4().hex[:6]}.mp4"

    def process(self, input_path, output_filename):
        """To be implemented in main.py"""
        raise NotImplementedError("Processing logic must be implemented in main.py")

    def get_latest_output(self):
        files = [os.path.join(self.output_dir, f) for f in os.listdir(self.output_dir)]
        return max(files, key=os.path.getmtime) if files else None