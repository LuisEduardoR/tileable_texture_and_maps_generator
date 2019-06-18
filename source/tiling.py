#!/usr/bin/python3

import numpy as np

import image_utility as util

def tile_image(image):

    # Gets a power of two version of the image with minimum standard deviation.
    po2_image = power_of_two_min_std(image)

    # TODO: Tile the image.

    return po2_image

# Returns a power of two version of the image.
# Chooses the power of two slice of the original with min standard deviation between the slices on the 4 corners and the center of the image.
def power_of_two_min_std(image):

    # Gets the largest power of two that fits in the original image.
    p = np.floor(np.log2(image.shape[0]))
    q = np.floor(np.log2(image.shape[1]))

    r = np.minimum(q, p)

    res = int(2**r)

    # If the image is already power of two returns it.
    if image.shape[0] == image.shape[1] && image.shape[0] == res:
        return image

    # Gets square slices with resolution 'res' from the original image 4 corners and center.
    slices = []

    slices.append(image[0:res,0:res,:])
    slices.append(image[(image.shape[0]-res):image.shape[0],0:res,:])
    slices.append(image[0:res,(image.shape[1]-res):image.shape[1],:])
    slices.append(image[(image.shape[0]-res):image.shape[0],(image.shape[1]-res):image.shape[1],:])
    slices.append(image[((image.shape[0]-res) // 2):((image.shape[0]-res) // 2 + res),((image.shape[1]-res) // 2):((image.shape[1]-res) // 2 + res),:])

    # Gets the standard deviation of the slices.
    slice_std_var = []
    for i in range(len(slices)):
        slice_std_var.append(util.get_image_std(slices[i]))

    # Returns the power of two slice with the minimum standard deviation.
    return slices[np.argmin(np.array(slice_std_var))]