#!/usr/bin/python3

# Contains functions used to generate the different texture maps.

import matplotlib.pyplot as plt
import image_utility as util
import numpy as np


# Generates a height map from a grayscale image.
def generate_height_map(gray_scale, height):
    histogram = util.get_image_histogram(gray_scale, 256)

    hist_mean = np.mean(histogram)

    in_shadow = 0
    for i in range(256):
        print(histogram[i])
        if histogram[i] >= hist_mean:
            in_shadow = i
            break

    in_highlight = 0
    for i in reversed(range(256)):
        if histogram[i] >= hist_mean:
            in_highlight = i
            break

    print("Histogram mean: {}".format(hist_mean))
    print("in_shadow: {}".format(in_shadow))
    print("in_highlight: {}".format(in_highlight))

    return util.level_image(gray_scale, in_shadow, in_highlight, int(255.0 * 0.95 * height), 0, 255)

# Generates a normal map from the height map.
# def generate_normal_map(height_map):

# Generates a roughness map from a grayscale image.
def generate_roughness_map(grayscale, roughness):

    return -util.level_image(grayscale, int(255.0 * 0.15 * roughness), 255, int(255.0 * 0.7 * roughness), 0, 255)