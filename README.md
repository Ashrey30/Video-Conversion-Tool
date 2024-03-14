# Video Interpolation and Upscaling
This Python script is designed to upscale (SD to HD) and interpolate a given video file. It utilizes OpenCV library for video processing tasks.


## Prerequisites
Creating a virtual environment is preferred.
Make sure you have Python installed on your system, along with the following libraries:
- OpenCV (`cv2`)
- NumPy (`numpy`)
You can install these libraries via pip: `pip install opencv-python numpy` OR use the command: `pip install -r requirements.txt`


## Usage
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script (`main.py`) in your terminal or command prompt.
3. Run the script with Python, passing the input video file path as a command-line argument: `python main.py input_video.mp4`
Replace `input_video.mp4` with the path to your desired input video file.
4. The script will then process the video, upscale it, interpolate frames, and reconstruct the video at a target FPS of 30.
5. Once completed, the output video will be saved in the `outputs` directory within the same directory as the script.


## Notes
- The output video will be in MP4 format.
- Ensure that the input video file exists and the file path is correct.
- The script may take some time to process, depending on the length and resolution of the input video.
- For any issues or improvements, feel free to submit an issue or pull request on GitHub.