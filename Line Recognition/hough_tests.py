# Based on https://docs.opencv.org/master/d6/d10/tutorial_py_houghlines.html

import cv2 as cv
import numpy as np
import os


def hough1(input_img: str, output_img: str):

    # Getting the paths
    image_dir = os.path.realpath("../images")
    input_img_path = f"{image_dir}/{input_img}"  # jpeg or png? they could make difference
    output_img_path = f"{image_dir}/{output_img}"

    # Getting the image
    img = cv.imread(filename=input_img_path)

    # Processing
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi / 180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imwrite(output_img_path, img)


def hough2(input_img, output_img):
    img = cv.imread(cv.samples.findFile('sudoku.png'))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv.imwrite('houghlines5.jpg', img)


if __name__ == '__main__':
    hough1("imagem_teste", "houghlines3.jpg")
