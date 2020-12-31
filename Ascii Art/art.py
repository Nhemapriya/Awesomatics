import cv2
import numpy as np

import sys

symbols_list = ["*", "?", "^", ".", "+"]
threshold_list = [0, 30, 90, 120, 150]

def print_out_ascii(array):
    """prints the coded image with symbols"""
    for row in array:
        for e in row:
            print(symbols_list[int(e) % len(symbols_list)], end="")
        print()


def img_to_ascii(image):
    """returns the numeric coded image"""
    height, width = image.shape
    new_width = int(width / 20) 
    new_height = int(height / 40)

    resized_image = cv2.resize(image, (new_width, new_height),)
    thresh_image = np.zeros(resized_image.shape)

    for i, threshold in enumerate(threshold_list):
        thresh_image[resized_image > threshold] = i
    return thresh_image


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("Using {} as Image Path\n".format(sys.argv[1]))
        image_path = sys.argv[1]

    image = cv2.imread(image_path, 0)  # read image

    ascii_art = img_to_ascii(image)
    print_out_ascii(ascii_art)