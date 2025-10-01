# Video-to-Frames-Extractor-using-Python
This project extracts individual frames from a video and saves them as image files in a specified folder. It is useful for applications like video processing, machine learning datasets, and computer vision projects.
🚀 Features

Reads a video file frame by frame

Saves each frame as a JPEG image

Automatically creates the output folder (if it doesn’t exist)

Displays live preview of frames while extracting

Press q to stop extraction anytime

🛠️ Technologies Used

Python 3

OpenCV (cv2)
 – for video reading and image writing

OS module
 – for file/folder handling

📂 How to Run

Install OpenCV:

pip install opencv-python


Run the script:

python video_to_frames.py


Update the script with your video path and output folder path:

video_path = "C:\\Users\\anton\\Downloads\\walk.mp4"
output_folder = "C:\\Users\\anton\\Desktop\\frames"


Frames will be saved as:

frame_0000.jpg
frame_0001.jpg
frame_0002.jpg
...
