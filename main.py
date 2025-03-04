import sys
import os
import time
from processor import VideoProcessor
from utils import read_video, save_video
from trackers import Tracker

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_path> <output_filename>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_filename = sys.argv[2]
    
    # Initialize processor with same directories as Flask app
    processor = VideoProcessor('input_videos', 'output_videos')
    
    try:
        print(f"Starting processing: {input_path}")
        
        #read vid
        video_frames = read_video(input_path)
        
        #tracker=Tracker('models/best.pt')
        
        #tracks=tracker.get_object_tracks(video_frames)
    
    
        #save vid
        output_path = os.path.join(processor.output_dir, output_filename)
        with open(output_path, 'w') as f:
            save_video(video_frames,output_path)
        
        print(f"Processing completed: {output_path}")
        sys.exit(0)
        
    except Exception as e:
        print(f"Processing failed: {str(e)}")
        sys.exit(1)