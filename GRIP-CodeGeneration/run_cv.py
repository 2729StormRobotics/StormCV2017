#!/usr/bin/python2

"""
Sample program that uses a generated GRIP pipeline to detect red areas in an image and publish them to NetworkTables.
"""

import cv2
from networktables import NetworkTables
from networktables import NetworkTable
from retrotape_b import Retrotape
import time
import logging


def extra_processing(pipeline):
    """
    Performs extra processing on the pipeline's outputs and publishes data to NetworkTables.
    :param pipeline: the pipeline that just processed an image
    :return: None
    """
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []

    # Find the bounding boxes of the contours to get x, y, width, and height
    for contour in pipeline.filter_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left corner of the bounding box
        center_y_positions.append(y + h / w)
        widths.append(w)
        heights.append(y)
        print("x")
        print(x)
        print("y")
        print(y)
        print("w")
        print(w)
        print("h")
        print(h)

    # Publish to the '/vision/red_areas' network table
    table = NetworkTables.getTable('Vision')
    table.putNumberArray('x', center_x_positions)
    table.putNumberArray('y', center_y_positions)
    table.putNumberArray('width', widths)
    table.putNumberArray('height', heights)


def main():
    logging.basicConfig(level=logging.DEBUG)
    print('Initializing NetworkTables')
    #NetworkTable.setTeam('2729')
    #NetworkTables.setClientMode()
    #NetworkTables.setIPAddress('10.27.29.202')
    NetworkTables.initialize(server='10.27.29.205')

    table = NetworkTables.getTable('/A/B')
    table.putNumber('dsTime', 100)
    time.sleep(5)
    
    print('Creating video capture')
    cap = cv2.VideoCapture(0)

    print('Creating pipeline')
    pipeline = Retrotape()

    print('Running pipeline')
    while cap.isOpened():
        have_frame, frame = cap.read()
        if have_frame:
            pipeline.process(frame)
            extra_processing(pipeline)

    print('Capture closed')

if __name__ == '__main__':
    main()
