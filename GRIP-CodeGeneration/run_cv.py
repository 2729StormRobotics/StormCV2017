#!/usr/bin/python3


"""
Sample program that uses a generated GRIP pipeline to detect red areas in an image and publish them to NetworkTables.
"""

import cv2
import threading
from networktables import NetworkTables
from networktables import NetworkTable
from retrotape import Retrotape
import time
import logging
import numpy as np
from collections import OrderedDict


def extra_processing(pipeline):
    """
    Performs extra processing on the pipeline's outputs and publishes data to NetworkTables.
    :param pipeline: the pipeline that just processed an image
    :return: sum area or rectangles
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
        # X and Y are coordinates of the top-left corner of the bounding box
        center_x_positions.append(x + w / 2)
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(h)
        # areas.append(w * h) lw calculation
        areas.append(cv2.contourArea(contour))
    # Publish to the '/vision/red_areas' network table
    try:
        final_area = areas[0] + areas[1]
    except:
        ""
    table = NetworkTables.getTable('Vision')
    table.putNumberArray('x', center_x_positions)
    table.putNumberArray('y', center_y_positions)
    table.putNumberArray('width', widths)
    table.putNumberArray('height', heights)
    table.putNumberArray('area', areas)
    return final_area

def distanceEstimate(currArea):
    areaHash = {
        13000: .7,
        11850: .8,
        9370: .9,
        7830: 1,
        6500: 1.1,
        5470: 1.2,
        4650: 1.3,
        3925: 1.4,
        3500: 1.5,
        3100: 1.6,
        2770: 1.7,
        2390: 1.8,
        2260: 1.9,
        2060: 2,
        1880: 2.1,
        1735: 2.2,
        1620: 2.3,
        1455: 2.4,
        1375: 2.5,
        1210: 2.6,
        1035: 2.7,
        1000: 2.8,
        975: 2.9,
        940: 3,
        845: 3.1,
        780: 3.2,
        750: 3.3,
        695: 3.4,
        655: 3.5,
        630: 3.6}

        estDistance = 0
        prevDistVal = 0
        prevAreaVal = 0

        areaHash = OrderedDict(sorted(areaHash.items(), key = lambda areaHash: areaHash[0]))
        values = areaHash.values()

        for areaVal, distVal in areaHash.items():
            if currArea > 13000:
                estDistance = -1.0142 * np.log(0.0000578938 * currArea)
                if estDistance > 1.3 and estDistance < 2:
                    estDistance -= 0.1
                    print("areaTrend: {:f} estimated dist: {:f}".format(currArea, estDistance))
                break

            if currArea < areaVal:
                try:
                    m = (distVal - prevDistVal)/(areaVal - prevAreaVal)
                    b = distVal - (m * areaVal)
                    estDistance = m * areaVal + b
                    # estDistance = (distVal + prevDistVal) / 2.0
                    print("areaHash: {:f} estimated dist: {:f}".format(currArea, estDistance))
                    # print("distVal: {:f} prevDistVal: {:f}".format(distVal, prevDistVal))
                except:
                    ""
                break
            prevDistVal = distVal
            prevAreaVal = areaVal

def main():
    logging.basicConfig(level=logging.DEBUG)
    print('Initializing NetworkTables')
    # NetworkTable.setTeam('2729')
    # NetworkTables.setClientMode()
    # NetworkTables.setIPAddress('10.27.29.202')
    NetworkTables.initialize(server='10.27.29.100')

    print('Creating pipeline')
    pipeline = Retrotape()

    print('Creating video capture')
    cap = cv2.VideoCapture(0)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 544)
    cap.set(cv2.CAP_PROP_EXPOSURE, 0)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 30)

    print('Running pipeline')
    iteration = 0
    total = 0
    while cap.isOpened():
        have_frame, frame = cap.read()
        if have_frame:
            pipeline.process(frame)
            currArea = extra_processing(pipeline)
            total += currArea
            iteration += 1
            table = NetworkTables.getTable('Vision')

            if(iteration % 200 == 0):
                # table = NetworkTables.getTable('Vision')
                table.putNumber('Average Area', total / 200)
                print(total / 200)
                iteration = 0
                total = 0
            
            estDistance = distanceEstimate(currArea)
            table.putNumber('Distance', estDistance)
    print('Capture closed')

if __name__ == '__main__':
    main()