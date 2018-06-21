#!/bin/bash

# Define a timestamp function
timestamp() {
  date +"%T"
}

# do something...
timestamp # print timestamp


ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 output.mkv
