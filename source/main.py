#!/usr/bin/python3

import matplotlib as mpl
import numpy as np
import imageio
import pathlib
import sys
import time

import image_utility as util
import maps
import tiling

def main():

    print("- Enter the filename:")
    
    # Gets the filename .
    filename = str(input()).rstrip()

    # Gets the path to the image.
    image_path = pathlib.Path('./{}'.format(filename))

    # Verifies if the path provided leads to a valid file.
    if not image_path.exists() or not image_path.is_file():
        print("# Input image doesn't exist!")
        sys.exit(-1)

    # Opens the image.
    image = imageio.imread(image_path)

    print("# (TODO) Tiling image...")

    # Stores the start time of the operation.
    start_t = time.time()

    tile_image = tiling.tile_image(image)

    # Measures the amount of time spent.
    end_t = time.time()
    print("DONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("# Generating grayscale...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates a grayscale image to be used to create height and roughness maps.
    grayscale = util.as_monochrome(tile_image)

    # Measures the amount of time spent.
    end_t = time.time()
    print("DONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("# Generating height map...")
    print("## Aplying levels...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates the height map.
    height_map = maps.generate_height_map(grayscale)

    # Measures the amount of time spent.
    end_t = time.time()
    print("DONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("# (TODO) Generating normal map...")

    #           #
    #   TODO    #
    #           #

    print("# Generating roughness map...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates the roughness map
    roughness_map = maps.generate_roughness_map(grayscale)

    # Measures the amount of time spent.
    end_t = time.time()
    print("DONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("# Saving generated images...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Gets the name of the to be used for the output image (removes the extension at the end).
    outname = filename.split('.')[0]

    imageio.imwrite("{}_tile.png".format(outname), tile_image.astype(np.uint8), compress_level=5)

    # Grayscale is an intermediary step that doesn't need to be saved, if you want to uncomment this line.
    #imageio.imwrite("{}_gray.png".format(outname), out_image.astype(np.uint8), compress_level = 5)

    imageio.imwrite("{}_height.png".format(outname), height_map.astype(np.uint8), compress_level=5)
    # (TODO) Save normal map
    imageio.imwrite("{}_rough.png".format(outname), roughness_map.astype(np.uint8), compress_level=5)

    # Measures the amount of time spent.
    end_t = time.time()
    print("DONE! (Time spent: {:.2f})".format(end_t - start_t));


main()