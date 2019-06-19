#!/usr/bin/python3

#   This program is intended to convert the roughness maps generated by the main program into a format that can be used by Unity.
#   Unity uses a format in wich the metalicity of a texture is stored in the red channel and the smoothness map (inverted roughness map)
#   is stored on the alpha channel.

import numpy as np
import imageio
import pathlib
import sys
import time

import image_utility as util

def main():

    # Prints a messagge if the program was incorrectly used.
    if len(sys.argv) != 2:
        print("Usage: <program name> <file name>")
        sys.exit(-1)

    print("\n# This program will convert a roughness map into a texture that can be directly used in Unity. #\n")

    # Gets the filename from the arguments used when calling the program.
    filename = sys.argv[1]

    # Gets the path to the image.
    image_path = pathlib.Path('./{}'.format(filename))

    # Verifies if the image exists.
    if not image_path.exists() or not image_path.is_file():
        print("Input image does not exist!")
        sys.exit(-1)

    # Opens the image.
    image = imageio.imread(image_path)

    # Receives how metallic should the texture be.
    print(" > Enter how metallic is your texture (0 = not metallic, 255 = full metallic):")
    metal = int(input())

    metal = np.clip(metal, 0, 255)

    print("\n# Converting...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Convert the image to a format that can be used in Unity engine.
    shp = (image.shape[0], image.shape[1], 4)
    out_image = np.zeros(shp, dtype = int)

    out_image[:,:,0] = metal
    out_image[:,:,1] = 1
    out_image[:,:,2] = 0
    out_image[:,:,3] = 1 - image[:,:]

    # Measures the maount of time spent.
    end_t = time.time()

    print("# DONE! (Time spent: {:.2f})".format(end_t - start_t))

    print("# Saving file...")

    # Stores the start time of the operation.
    start_t = time.time()

    # Gets the name of the to be used for the output image (removes the extension at the end).
    outname = filename.split('.')[0]

     # Saves the output image.
    imageio.imwrite("{}_unity.png".format(outname), out_image.astype(np.uint8), compress_level = 5)
    
    # Measures the amount of time spent.
    end_t = time.time()

    print("# DONE! (Time spent: {:.2f})\n".format(end_t - start_t))


main()
