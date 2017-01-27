#!/usr/bin/python3

"""
Sample program that uses a generated GRIP pipeline to detect red areas in an image and publish them to NetworkTables.
"""

import cv2
from networktables import NetworkTables
from networktables import NetworkTable
from retrotape import Retrotape
import time
import logging
import numpy as np

def extra_processing(pipeline):
    #time.sleep(1)
    """
    Performs extra processing on the pipeline's outputs and publishes data to NetworkTables.
    :param pipeline: the pipeline that just processed an image
    :return: None
    """
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []
    areas = []
    final_area = 0
    # Find the bounding boxes of the contours to get x, y, width, and height
    for contour in pipeline.filter_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left corner of the bounding box
        center_y_positions.append(y + h / w)
        widths.append(w)
        heights.append(y)
        areas.append(w*h)
    #Publish to the '/vision/red_areas' network table
    #print("Posting Data...")
    try:
        final_area = areas[0]+areas[1]
    except:
        ""
    #print(center_x_positions)
    #print(center_y_positions)
    table = NetworkTables.getTable('Vision')
    table.putNumberArray('x', center_x_positions)
    table.putNumberArray('y', center_y_positions)
    table.putNumberArray('width', widths)
    table.putNumberArray('height', heights)
    table.putNumberArray('area', areas)
    #table.putNumber('final area', final_area)
    return final_area

def main():
    logging.basicConfig(level=logging.DEBUG)
    print('Initializing NetworkTables')
    #NetworkTable.setTeam('2729')
    #NetworkTables.setClientMode()
    #NetworkTables.setIPAddress('10.27.29.202')
    NetworkTables.initialize(server='10.27.29.100')

    print('Creating pipeline')
    pipeline = Retrotape()

    print('Creating video capture')
    #stream = cv2
    #cap = cv2.VideoCapture("http://localhost:1181/?action=stream")
    cap = cv2.VideoCapture(0)
    print('Running pipeline')
    iteration = 0
    total = 0
    while cap.isOpened():
        have_frame, frame = cap.read()
        if have_frame:
            pipeline.process(frame)
            currArea = extra_processing(pipeline)
            total += currArea
            iteration+=1
            #print(iteration)
            #print(total)

            #***EQUATION DISTANCE VS AREA*** 53111e^(-1.702x)
            #***Inverse*** ln(A/53111)/-1.702 = d
            if(iteration%30 == 0):
                table = NetworkTables.getTable('Vision')
                table.putNumber('Average Area', total/30)
                print(total / 30)
                iteration = 0
                total = 0
            print("area: {:d}estimated dist: {:d}".format(area, 1))
            table.putNumber('Distance', np.log(currArea/5311)/-1.702)
    print('Capture closed')

if __name__ == '__main__':
    main()
