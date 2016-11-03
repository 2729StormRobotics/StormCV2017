#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
using namespace cv;
//using namespace cv;
int posX, posY, lastX, lastY, tarX, tarY;
int lowH, highH, lowS, highS, lowV, highV;
int main(int argc, char** argv)
{
	std::cout << "Program initiated by user." << std::endl;
	Mat imgTmp, imgLines, imgOriginal, imgHSV, imgThresholded;
	int count;
	bool bSuccess;
	VideoCapture cap(0);
	if (!cap.isOpened())
	{
		std::cout << "ERROR: Webcam was unable to be opened" << std::endl;
		return -1;
	}
	else
		std::cout << "Webcam Initiated" << std::endl;
	namedWindow("Storm 2729 Vision System", CV_WINDOW_AUTOSIZE);
	lowH = 170;//170
	highH = 179;//179
	lowS = 150;//150
	highS = 255;//255
	lowV = 60;//60
	highV = 255;//255
	cap.read(imgTmp);
	imgLines = Mat::zeros(imgTmp.size(), CV_8UC3);
	count = 0;
	while (true)
	{
		if (count % 5 == 0)
			imgLines = Mat::zeros(imgTmp.size(), CV_8UC3);
		bSuccess = cap.read(imgOriginal);
		if (!bSuccess)
		{
			std::cout << "Frame dropped" << std::endl;
			break;
		}
		cvtColor(imgOriginal, imgHSV, COLOR_BGR2HSV);
		inRange(imgHSV, Scalar(lowH, lowS, lowV), Scalar(highH, highS, highV), imgThresholded);
		erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
		dilate(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
		dilate(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
		erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
		Moments oMoments = moments(imgThresholded);
		double dM01 = oMoments.m01;
		double dM10 = oMoments.m10;
		double dArea = oMoments.m00;
		double deltaPos = ((posX - lastX) + (posY - lastY)) / 2;
		if (dArea > 10000)
		{
			posX = dM10 / dArea;
			posY = dM01 / dArea;
			if ((deltaPos >= 10 || deltaPos <= -10) && lastX >= 0 && lastY >= 0 && posX >= 0 && posY >= 0)
				line(imgLines, Point(posX, posY), Point(lastX, lastY), Scalar(0, 0, 255), 4);
			else
				line(imgLines, Point((posX + lastX) / 2, (posY + lastY) / 2), Point((posX + lastX) / 2, (posY + lastY) / 2), Scalar(0, 0, 255), 4);
//<<<<<<< HEAD
//			tarX = posX - lastX;
//			tarY = (posY - lastY) * .87;
//=======
//			tarX = 2 * posX - lastX;
//			tarY = posY + ((posY - lastY) * .87);
//>>>>>>> d543bdd99fe71c9b8bc425ba4aad2b593a1a814b
			lastX = posX;
			lastY = posY;
		}
		imshow("Thresholded Image", imgThresholded);
		imgOriginal = imgOriginal + imgLines;
		imshow("Original", imgOriginal);
		count++;
		if (waitKey(30) == 27)
		{
			std::cout << "Program Terminated by user." << std::endl;
			break;
		}
	}
	return 0;
}