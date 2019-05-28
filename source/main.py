#!/usr/bin/python3

import matplotlib as mpl
import numpy as np
import imageio
import pathlib
import sys


def as_monochrome(rgb_image):
    hsv_image = mpl.colors.rgb_to_hsv(rgb_image)

    return hsv_image[:, :, 2]


def main():
    if len(sys.argv) != 2:
        print("Usage: program-name filename")
        sys.exit(-1)

    image_path = pathlib.Path('./' + sys.argv[1])

    if not image_path.exists() or not image_path.is_file():
        print("Input image does not exist!")
        sys.exit(-1)

    image = imageio.imread(image_path)

    out_image = as_monochrome(image)

    imageio.imwrite("out.png", out_image)


main()