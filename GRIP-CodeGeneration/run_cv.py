#!/usr/bin/python3

import cv2
import threading
from datetime import datetime
from networktables import NetworkTables
#from retrotape import Retrotape
from retrotapehsl import RetrotapeHSL
import time
import logging
import numpy as np
from collections import OrderedDict
RES = 320 # x resolution

def main():
    logging.basicConfig(level=logging.DEBUG)
    print('Initializing NetworkTables')
    # NetworkTables.setTeam(2729)
    # NetworkTables.setClientMode()
    # NetworkTables.setIPAddress('10.27.29.202')
    NetworkTables.initialize(server='roboRIO-2729-frc.local')

    print('Creating pipeline')
    #pipeline = Retrotape()
    pipeline = RetrotapeHSL()

    print('Creating video capture')
    cap = cv2.VideoCapture(0)
    camSetup(cap)
    print('Running pipeline')

    iteration = 0
    total_area = 0
    curr_time = datetime.now()
    table = NetworkTables.getTable('Vision')

    while cap.isOpened():
        have_frame, frame = cap.read()
        if have_frame:
            pipeline.process(frame)
            publishValues(pipeline)
            total_area += table.getNumber('curr_area')
            iteration += 1

            if(iteration % 200 == 0):
                avgValues(total_area, curr_time, 200)
                iteration = 0
                total = 0
    print('Capture closed')

def camSetup(cap):
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    cap.set(cv2.CAP_PROP_EXPOSURE, 0)
    cap.set(cv2.CAP_PROP_BRIGHTNESS, 30)

def publishValues(pipeline):
    center_x_positions = []
    midpoint_x = RES / 2 #half resolution
    center_y_positions = []
    widths = []
    heights = []
    areas = []
    final_area = 0
    shift = 0

    # Find the bounding boxes of the contours to get x, y, width, and height
    for contour in pipeline.filter_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        center_x_positions.append(x + w / 2)
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(h)
        areas.append(cv2.contourArea(contour))

    try:
        final_area = areas[0] + areas[1]
        midpoint_x = (center_x_positions[0] + center_x_positions[1]) / 2
        shift = shiftEstimate(center_x_positions)
    except:
        pass

    scaling = 6.8
    estDistance = distanceEstimate(final_area * scaling)
    p_angle = (50/320)*(midpoint_x - (RES/2))

    table = NetworkTables.getTable('Vision')
    table.putNumberArray('x', center_x_positions)
    table.putNumberArray('y', center_y_positions)
    table.putNumberArray('width', widths)
    table.putNumberArray('height', heights)
    table.putNumberArray('area', areas)

    table.putNumber('shift', shift)
    table.putNumber('midpoint_x', midpoint_x)
    table.putNumber('center_dist', midpoint_x - (RES/2))
    table.putNumber('p_angle', p_angle)
    table.putNumber('est_distance', estDistance)
    table.putNumber('curr_area', final_area)
    table.flush()

def shiftEstimate(center_x_positions):
    if center_x_positions[0] < center_x_positions[1]: #values are reported left to right
        shift = widths[1] - widths[0] #return (-) if l-shift
    else:
        shift = widths[0] - widths[1] #return (+) if r-shift

def distanceEstimate(currArea):
    areaHash = {48800: 0.4,
                33785: 0.5,
                24215: 0.6,
                18180: 0.7,
                13689: 0.8,
                11272: 0.9,
                9235: 1.0,
                7715: 1.1,
                6570: 1.2,
                5619: 1.3,
                4897: 1.4,
                4235: 1.5,
                3795: 1.6,
                3375: 1.7,
                3090: 1.8,
                2718: 1.9,
                2432: 2.0,
                2142: 2.1,
                1961: 2.2,
                1723: 2.3,
                1587: 2.4,
                1450: 2.5}
    currArea = currArea
    estDistance = 0
    prevDistVal = 0
    prevAreaVal = 0

    areaHash = OrderedDict(sorted(areaHash.items(), key = lambda areaHash: areaHash[0]))
    values = areaHash.values()

    for areaVal, distVal in areaHash.items():
        if currArea > 48800:
            estDistance = -0.648088 * np.log(0.0000191212 * currArea)
            print("areaTrend: {:f} estimated dist: {:f}".format(currArea, estDistance))
            break

        if currArea < areaVal:
            try:
                m = (distVal - prevDistVal)/(areaVal - prevAreaVal)
                b = distVal - (m * areaVal)
                # estDistance = m * areaVal + b
                estDistance = (distVal + prevDistVal) / 2.0
                print("areaHash: {:f} estimated dist: {:f}".format(currArea, estDistance))
                # print("distVal: {:f} prevDistVal: {:f}".format(distVal, prevDistVal))
            except:
                pass
            break
        prevDistVal = distVal
        prevAreaVal = areaVal
    return estDistance

def avgValues(area, curr_time, cycles):
    table = NetworkTables.getTable('Vision')
    table.putNumber('FPS', cycles / (datetime.now() - curr_time).total_seconds())
    curr_time = datetime.now()
    table.putNumber('Average Area', area / cycles)
    print(area / cycles)

if __name__ == '__main__':
    main()
