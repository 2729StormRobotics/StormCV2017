env LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH mjpg_streamer -o "output_http.so -w ./www -p 5801" -i "input_uvc.so -d /dev/video0 -r 320x240 -f 30 -ex 0 -br 30 -sh 0 -l off" &

