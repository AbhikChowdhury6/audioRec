#!/bin/bash

# Define a timestamp function
timestamp() {
  date +"%T"
}

# do something...
timestamp # print timestamp

#how about we just capture HD pictures at 5HZ

ffmpeg -f v4l2 -framerate 30 -video_size 1920x1080 -i /dev/video0 output.mp4
