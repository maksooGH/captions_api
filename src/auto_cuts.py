import cv2
import numpy as np
from collections import deque

def detect_scene_cuts(video_path, threshold=0.85, avg_frames=5, min_cut_gap=30):
    cap = cv2.VideoCapture(video_path)
    prev_hist_queue = deque(maxlen=avg_frames)  # Store previous histograms
    frame_number = 0
    scene_cuts = []
    last_cut_frame = -min_cut_gap  # To ensure minimum gap between cuts

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Compute histogram with fewer bins
        hist = cv2.calcHist([gray], [0], None, [32], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        # Store histogram in queue
        if len(prev_hist_queue) > 0:
            avg_hist = np.mean(prev_hist_queue, axis=0)  # Compute moving average
            diff = cv2.compareHist(avg_hist, hist, cv2.HISTCMP_CORREL)

            if diff < threshold and (frame_number - last_cut_frame) > min_cut_gap:
                scene_cuts.append(frame_number)
                last_cut_frame = frame_number  # Update last detected cut

        prev_hist_queue.append(hist)
        frame_number += 1

    cap.release()
    return scene_cuts

# Example usage
video_file = "1_s1.mp4"
cuts = detect_scene_cuts(video_file, threshold=0.9, avg_frames=5, min_cut_gap=15)  # Adjust threshold and smoothing
print("Detected scene cuts at frames:", cuts)

