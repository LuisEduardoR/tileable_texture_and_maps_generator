#!/usr/bin/python3

# Contains functions used to generate the different texture maps.

import image_utility as util

# Generates a height map from a grayscale image.
def generate_height_map(grayscale):
    return util.level_image(grayscale, 90, 255, 70, 0, 255)

# Generates a normal map from the height map.
# def generate_normal_map(height_map):

# Generates a roughness map from a grayscale image.
def generate_roughness_map(grayscale):
    return -util.level_image(grayscale, 120, 255, 100, 30, 200)