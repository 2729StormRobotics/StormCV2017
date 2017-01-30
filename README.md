# StormCV2017

Computer Vision code for the 2017 FRC season.  This is a GRIP based vision system.  We utilize the "Genereate Code" feature in order to run python code on our Raspberry pi 3.  On the base directory we have the file start-mjg-streamer.sh which streams an ipcamera stream to port 1181 on the raspberry pi.  In the GRIP-CodeGeneration we have all the vision processing code.  run_cv.py is what we change manually to do the desired calculations on the processed vision.  The other .py files are simply taken from the tools>GenerateCode feature on GRIP.

## Getting Started

If you wish to use our setup just clone this repo to your raspberry pi
```
git clone https://github.com/2729StormRobotics/StormCV2017.git
```

### Prerequisites

We use python3 and OpenCV3 on our raspberrypi3.  Python is super easy to install...
```
sudo apt-get install python3
```

OpenCV3 is a bit more of a pain.  Here's a helpful link... 
http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/

Also on a windows computer you will need Eclipse with the wpilib plugins.  Here's a helpful link...
http://wpilib.screenstepslive.com/s/4485/m/13503/l/599679-installing-eclipse-c-java

## Running the Code
Assuming you've gotten all the installs running the code is fairly straightforward
1. Connect both the pi and Windows machine to the same network
2. On eclipse press WPIlib>RunOutlineViewer>StartServer
3. Run the python code in the StormCV2017/GRIP-CodeGeneration directory
```
python3 run_cy.py
```

## Who are we
Storm Robotics NJ (2729)
