# Smile Detector

## Description
This Python script uses the OpenCV library to capture video from a webcam and detect faces in real-time. For each detected face, it analyzes emotions using the DeepFace library to determine if the person is smiling. The script displays the video feed with labeled faces indicating whether each person is "Smiling" or "Not Smiling".

### Installation Prerequisites

You need Python installed on your machine. Python 3.6 or higher is recommended. You can download it from python.org.

## Dependencies

Before running the script, you need to install the following Python libraries:

OpenCV: For capturing video and face detection.

DeepFace: For analyzing emotions.

You can install these dependencies using pip:

## Bash
Copy code

### pip3 install opencv-python deepface

Running the Script
To run the script, navigate to the directory containing the script and run the following command in your terminal:

Copy code

### python3 smile.py

Make sure your webcam is enabled and has the necessary permissions to be accessed by your system.

## Usage

### Once the script is running:

It will open a window displaying the video captured from your webcam.

Detected faces will be outlined with a green rectangle.

Each face will be labeled either "Smiling" or "Not Smiling" based on the emotion analysis.

To stop the script, press the 'q' key while the video window is active. This will close the window and terminate the script.

## Troubleshooting

1) If the script fails to run or does not detect the webcam, ensure that:

2) Your webcam drivers are up to date and functioning correctly.

3) Python and all required libraries are correctly installed.

4) The script has the necessary permissions to access your webcam.

For any other issues, check the error messages in the terminal for clues on what might be going wrong.

### License

This project is open-source and available under the MIT License.
