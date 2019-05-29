#!/usr/bin/python3

import matplotlib as mpl
import numpy as np
import imageio
import pathlib
import sys
import time

import image_utility as util

def main():
    if len(sys.argv) != 2:
        print("Usage: program-name filename")
        sys.exit(-1)

    image_path = pathlib.Path('./' + sys.argv[1])

    if not image_path.exists() or not image_path.is_file():
        print("Input image does not exist!")
        sys.exit(-1)

    image = imageio.imread(image_path)

    print("# (TODO) Tiling image...")

    #           #
    #   TODO    #
    #           #

    print("# Generating grayscale...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates a grayscale image to be used to create height and roughness maps.
    grayscale = util.as_monochrome(image)

    # Measures the amount of time spent.
    end_t = time.time()
    print("DONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("# Generating height map...")
    print("## Aplying levels...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates the height map.
    height_map = util.level_image(grayscale, 90, 255, 70, 0, 255)

    # Measures the amount of time spent.
    end_t = time.time()
    print("DONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("# Saving files...")

    print("# (TODO) Generating normal map...")

    #           #
    #   TODO    #
    #           #

    print("# (TODO) Generating roughness map...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates the roughness map
    roughness_map = -util.level_image(grayscale, 110, 210, 120, 50, 230)

    # Measures the amount of time spent.
    end_t = time.time()
    print("DONE! (Time spent: {:.2f})".format(end_t - start_t));

    #           #
    #   TODO    #
    #           #

    print("# Saving generated images...")

    #           #
    #   TODO    #
    #           #

    # Stores the start time of the operation.
    start_t = time.time()

    # (TODO) Save tiling texture
    imageio.imwrite("grayscale.png", grayscale.astype(np.uint8))
    imageio.imwrite("height.png", height_map.astype(np.uint8))
    # (TODO) Save normal map
    imageio.imwrite("roughness.png", roughness_map.astype(np.uint8))

    # Measures the maount of time spent.
    end_t = time.time()
    print("DONE! (Time spent: {:.2f})".format(end_t - start_t));


main()