#recording video

ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 output.mkv



#recording audio

#hw is selected from arecord -l
ffmpeg -f alsa -i hw:1  out.wav
