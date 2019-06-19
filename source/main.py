#!/usr/bin/python3

import numpy as np
import imageio
import pathlib
import sys
import time

import image_utility as util
import maps
import tiling

def main():

    print("\033[1;37;40m- Enter the filename:\033[0;37;40m")
    
    # Gets the filename .
    filename = str(input()).rstrip()

    # Gets the path to the image.
    image_path = pathlib.Path('./{}'.format(filename))

    print("\033[0;33;40m# Opening image...")

    # Verifies if the path provided leads to a valid file.
    if not image_path.exists() or not image_path.is_file():
        print("\033[1;31;40m\tInput image doesn't exist!\033[0;37;40m")
        sys.exit(-1)

    # Opens the image.
    image = imageio.imread(image_path)

    # Verifies if the image has 3 channels (images must be RGB).
    if len(image.shape) != 3 or image.shape[2] != 3:
        print("\033[1;31;40m\tInvalid image! (Image must be RGB)\033[0;37;40m")
        sys.exit(-1)

    print("\033[1;32;40m\tImage opened succesfully!")

    # Gets the user parameters for the map generation.

    # Gets the image height multiplier.
    print("\033[1;37;40m- Enter image height (0.0 - 1.0):\033[0;37;40m")
    img_height = float(input())

    # Gives an error if an invalid img_height was passed.
    if img_height < 0 or img_height > 1:
        print("\033[1;31;40m\tInvalid height value! (Must be between 0.0 and 1.0 but was {})\033[0;37;40m".format(img_height))
        sys.exit(-1)

    # Gets the image roughness multiplier.
    print("\033[1;37;40m- Enter image roughness (0.0 - 1.0):\033[0;37;40m")
    img_roughness = float(input())

    # Gives an error if an invalid img_roughness was passed.
    if img_roughness < 0 or img_roughness > 1:
        print("\033[1;31;40m\tInvalid roughness value! (Must be between 0.0 and 1.0 but was {})\033[0;37;40m".format(img_roughness))
        sys.exit(-1)

    print("\033[0;33;40m# (TODO) Tiling image...")

    # Stores the start time of the operation.
    start_t = time.time()

    tile_image = tiling.tile_image(image)

    # Measures the amount of time spent.
    end_t = time.time()
    print("\033[1;32;40m\tDONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("\033[0;33;40m# Generating grayscale...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates a grayscale image to be used to create height and roughness maps.
    grayscale = util.as_monochrome(tile_image)

    # Measures the amount of time spent.
    end_t = time.time()
    print("\033[1;32;40m\tDONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("\033[0;33;40m# Generating height map...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates the height map.
    height_map = maps.generate_height_map(grayscale, img_height)

    # Measures the amount of time spent.
    end_t = time.time()
    print("\033[1;32;40m\tDONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("\033[0;33;40m# Generating normal map...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates the roughness map
    normal_map = maps.generate_normal_map(grayscale)

    # Measures the amount of time spent.
    end_t = time.time()
    print("\033[1;32;40m\tDONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("\033[0;33;40m# Generating roughness map...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Generates the roughness map
    roughness_map = maps.generate_roughness_map(grayscale, img_roughness)

    # Measures the amount of time spent.
    end_t = time.time()
    print("\033[1;32;40m\tDONE! (Time spent: {:.2f})".format(end_t - start_t));

    print("\033[0;33;40m# Saving generated images...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Gets the name of the to be used for the output image (removes the extension at the end).
    outname = filename.split('.')[0]

    imageio.imwrite("{}_tile.png".format(outname), tile_image.astype(np.uint8), compress_level=5)

    # Grayscale is an intermediary step that doesn't need to be saved, if you want to uncomment this line.
    # imageio.imwrite("{}_gray.png".format(outname), grayscale.astype(np.uint8), compress_level=5)

    imageio.imwrite("{}_height.png".format(outname), height_map.astype(np.uint8), compress_level=5)
    imageio.imwrite("{}_normal.png".format(outname), normal_map.astype(np.uint8), compress_level=5)
    imageio.imwrite("{}_rough.png".format(outname), roughness_map.astype(np.uint8), compress_level=5)

    # Measures the amount of time spent.
    end_t = time.time()
    print("\033[1;32;40m\tDONE! (Time spent: {:.2f})\033[0;37;40m".format(end_t - start_t));


main()