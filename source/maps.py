#!/usr/bin/python3

# Contains functions used to generate the different texture maps.

import image_utility as util

# Generates a height map from a grayscale image.
def generate_height_map(grayscale, height):
    return util.level_image(grayscale, 0, 255, int(255.0 * 0.95 * height), 0, 255)

# Generates a normal map from the height map.
# def generate_normal_map(height_map):

# Generates a roughness map from a grayscale image.
def generate_roughness_map(grayscale, roughness):

    return -util.level_image(grayscale, int(255.0 * 0.15 * roughness), 255, int(255.0 * 0.7 * roughness), 0, 255)