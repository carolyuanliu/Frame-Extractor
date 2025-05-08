import cv2
import os

def video_to_frames(video_path, output_dir, prefix="frame", skip_frames=24):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Skipping {video_path} (cannot open).")
        return

    os.makedirs(output_dir, exist_ok=True)
    saved_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join(output_dir, f"{prefix}_{saved_idx:05d}.jpg")
        cv2.imwrite(frame_filename, frame)
        saved_idx += 1
        for _ in range(skip_frames):
            if not cap.grab():
                break

    cap.release()
    print(f"Extracted {saved_idx} frames from {os.path.basename(video_path)} to {output_dir}")
