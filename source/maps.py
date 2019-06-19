#!/usr/bin/python3

# Contains functions used to generate the different texture maps.

import numpy as np

import image_utility as util

# Generates a height map from a grayscale image.
def generate_height_map(grayscale, height):
    return util.level_image(grayscale, 0, 255, int(255.0 * 0.95 * height), 0, 255)

# Generates a normal map from the height map.
def generate_normal_map(height_map):

    # Gets a normalized version of the height map.
    normalized = (height_map.astype(float)) / 255.0

    # Calculates the discrite partial derivatives in x and y.
    del_x = np.roll(normalized, 1, axis=0) - np.roll(normalized, -1, axis=0)
    del_y = np.roll(normalized, 1, axis=1) - np.roll(normalized, -1, axis=1)

    # Calculates the normal vector to the image and saves its XYZ coordinates to the RGB channels.
    normal = np.zeros((height_map.shape[0], height_map.shape[1], 3))

    normal[:,:,0] = ((-del_x / (np.sqrt(del_x**2 + del_y**2 + 1))) + 1) / 2.0
    normal[:,:,1] = ((-del_y / (np.sqrt(del_x**2 + del_y**2 + 1))) + 1) / 2.0
    normal[:,:,2] = 1 / (np.sqrt(del_x**2 + del_y**2 + 1))

    # Returns the normal map as an 24bit per pixel RGB image.
    return (255.0 * normal).astype(np.uint8)

# Generates a roughness map from a grayscale image.
def generate_roughness_map(grayscale, roughness):

    return -util.level_image(grayscale, int(255.0 * 0.15 * roughness), 255, int(255.0 * 0.7 * roughness), 0, 255)