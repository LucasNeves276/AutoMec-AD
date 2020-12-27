# Based on https://docs.opencv.org/master/d6/d10/tutorial_py_houghlines.html

import cv2 as cv
import numpy as np
import os


def hough1(input_img: str, output_img: str = ""):
    """

    :param input_img: input image name
    :param output_img: output name -> if ommited doesn't save
    :return: output_img
    """

    # Getting the paths
    images_dir = get_abs_path('../images', is_dir=True)
    image_path = get_abs_path(f"../images/{input_img}")
    if output_img != "":
        output_img_path = f"{images_dir}/{output_img}"
    else:
        output_img_path = ""

    # Getting the image
    img = cv.imread(filename=image_path)

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
    if output_img_path != "":
        cv.imwrite(output_img_path, img)
    else:
        show_image_temp(img=img)


def hough2(input_img, output_img):
    """

    :param input_img:
    :param output_img:
    :return:
    """

    # Getting the paths
    images_dir = get_abs_path('../images', is_dir=True)
    image_path = get_abs_path(f"../images/{input_img}")
    output_img_path = f"{images_dir}/{output_img}"

    img = cv.imread(cv.samples.findFile(image_path))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    if output_img_path != "":
        cv.imwrite(output_img_path, img)
    else:
        show_image_temp(img=img)


def show_image(img_path):
    """

    :param img_path: Image's absolute path: /.../image.png
    :return: Window showing the requested image. Press any key to close it
    """

    img = cv.imread(filename=img_path)

    show_image_temp(img=img)


def show_image_temp(img):
    """

    :param img:
    :return:
    """
    # Create a visualization window
    # CV_WINDOW_AUTOSIZE : window size will depend on image size
    cv.namedWindow("Display window", cv.WINDOW_AUTOSIZE)

    # Show the image
    cv.imshow("Display window", img)

    # Wait
    cv.waitKey(0)

    # Destroy the window -- might be omitted
    cv.destroyWindow("Display window")


def get_abs_path(rel_path: str, is_dir: bool = False):
    """

    :param rel_path: relative path
    :param is_dir:
    :return:
    """

    path = os.path.realpath(rel_path)

    assert os.path.exists(path), "File does not exist in specified path!"
    assert not is_dir or os.path.isdir(path), "Expected directory, got file"

    return path


if __name__ == '__main__':
    hough2("imagem_teste.jpeg", "houghlines3_2.jpg")
