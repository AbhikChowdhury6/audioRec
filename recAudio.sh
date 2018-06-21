#!/bin/bash

# Define a timestamp function
timestamp() {
  date +"%T"
}

# do something...
timestamp # print timestamp

#recording audio

#hw is selected from arecord -l
ffmpeg -f alsa -ac 2 -ar 44100 -i hw:0 -strict -2 ft1.mp4


#sample using arecord
#sudo arecord -D plughw:0 -c 2 -t wav --separate-channels t3chan1.wav t3chan2.wav
