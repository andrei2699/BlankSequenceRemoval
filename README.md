# Blank Sequence Removal

This is a simple tool to remove blank sequences from live video streams or video files.

## Usage

Run the main.py file with the following

### Modes

There are two modes of operation:

- Debug
- Normal

In the debug mode the program will show the video stream and the detected blank sequences along with some debug windows
that show intermediate results. Some trackbars are also available to adjust the parameters of the algorithm.

In the normal mode the program will only show the video stream and the detected blank sequences.

### Input Sources

The program can take input from a video file or from a live video stream.
The function `capture_video` in the `main.py` file can be used to specify the input source.
It can take a file path as an argument and in that case will play the video from the file.
If no argument is given it will capture video from the default camera.

## Algorithm

The algorithm is based on the following steps:

1. Calculate the absolute difference between the current frame and the previous frame.
2. Convert the video stream to grayscale
3. Apply a gaussian blur to the grayscale image
4. Apply an adaptive threshold to the blurred image
5. Apply a threshold to the non-zero pixels
6. If the number of non-zero pixels is less than a threshold then the frame is considered blank and a red X is drawn on
   the frame
7. If the number of non-zero pixels is greater than a threshold then the frame is considered non-blank and the frame is
   saved to the output video file
