import os
from extractor.extractor import video_to_frames

def process_all_videos(input_folder="Videos", output_folder="frames", skip_frames=24):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            video_path = os.path.join(input_folder, filename)
            video_to_frames(video_path, output_folder, prefix=filename.split('.')[0], skip_frames=skip_frames)

if __name__ == "__main__":
    process_all_videos()
