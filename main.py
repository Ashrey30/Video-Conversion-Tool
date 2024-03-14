import cv2
import numpy as np
import os
import sys
import time

def load_video(video_path):
    video_capture = cv2.VideoCapture(video_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    return video_capture, fps, total_frames

def separate_frames(video_capture, total_frames):
    frames = []
    for _ in range(total_frames):
        ret, frame = video_capture.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def upscale_frame(frame):
    return cv2.resize(frame, (1280, 720))

def upscale_video(frames):
    return [upscale_frame(frame) for frame in frames]

def linear_interpolation(frame1, frame2, num_intermediate_frames):
    alpha_values = np.linspace(0, 1, num_intermediate_frames + 2)[1:-1]
    interpolated_frames = [(1 - alpha) * frame1 + alpha * frame2 for alpha in alpha_values]
    return interpolated_frames

def interpolate_frames(frames, target_fps, fps):
    num_intermediate_frames = int(target_fps / fps)
    interpolated_frames = []
    for i in range(len(frames) - 1):
        frame1 = frames[i]
        frame2 = frames[i + 1]
        interpolated_frames.extend(linear_interpolation(frame1, frame2, num_intermediate_frames))
    return interpolated_frames

def reconstruct_video(frames, output_path, fps):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    height, width, _ = frames[0].shape
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for frame in frames:
        video_writer.write(cv2.convertScaleAbs(frame))
    video_writer.release()

def main():
    start_time = time.time()
    print(f"Loading Video......")
    video_path = sys.argv[1]
    video_capture, fps, total_frames = load_video(video_path)
    print(f"Seperating frames......")
    frames = separate_frames(video_capture, total_frames)
    print(f"Upscaling & Interpolating......")
    upscaled_frames = upscale_video(frames)
    target_fps = 30
    interpolated_frames = interpolate_frames(upscaled_frames, target_fps, fps)
    print(f"Assigning output path......")
    directory_name = "outputs"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    filename = os.path.basename(video_path)
    output_path = os.path.join(directory_name, filename)
    print(f"Reconstructing Video......")
    reconstruct_video(interpolated_frames, output_path, target_fps)
    end_time = time.time()
    print(f"Output video saved at: {output_path}")
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python new.py input_file_path")
        sys.exit(1)
    main()
