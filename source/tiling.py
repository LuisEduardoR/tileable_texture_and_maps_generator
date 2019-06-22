#!/usr/bin/python3

import numpy as np
import imageio

import image_utility as util

debug_tiling = False

def get_tile(image):

    # Gets a power of two version of the image with minimum standard deviation.
    po2_image = power_of_two_min_std(image)

    # DEBUG: Used to print the selected power of two slice of the texture before tiling.
    if debug_tiling:
        imageio.imwrite("po2texture.png", (po2_image).astype(np.uint8), compress_level=5)

    return perform_tiling(po2_image)

def perform_tiling(po2_image):

    # Creates a base for the mask to be used in tiling.
    mask_base = np.fromfunction(lambda i, j: 1 - ((i - po2_image.shape[0] / 2) / (po2_image.shape[0] / 4))**2, (po2_image.shape[0], po2_image.shape[1]), dtype=float)
    mask_base = np.clip(mask_base, 0, 1)

    # Calculates a modifier to the mask based on the image grayscale.
    monochrome_mask = np.sqrt(util.as_monochrome(po2_image)[:,:].astype(float)) / 8.0

    # Stores the mask to be used on tiling.
    mask = np.zeros(po2_image.shape)

    mask[:,:,0] = mask_base[:,:]**monochrome_mask # Aplies the monochrome modifier to the mask.
    mask[:,:,1] = mask[:,:,0] # Copies the mask to the other colo channels.
    mask[:,:,2] = mask[:,:,0]

    # DEBUG: Used to print the mask to be used for tiling on the x axis.
    if debug_tiling:
        imageio.imwrite("mask_tiling_x.png", (255 * mask).astype(np.uint8), compress_level=5)

    # Tiles the image on the x-axis.
    tile_x = np.roll(po2_image, po2_image.shape[1] // 2, axis=0)
    tile_x = (tile_x * (1 - mask)) + (po2_image * mask)

    # Rotates the base mask for y tiling.    
    mask_base = np.rot90(mask_base, 1, (0,1))

    # Creates a mask to be used in the y-axis tiling.
    mask[:,:,0] = mask_base[:,:]**monochrome_mask # Aplies the monochrome modifier to the mask.
    mask[:,:,1] = mask[:,:,0] # Copies the mask to the other colo channels.
    mask[:,:,2] = mask[:,:,0]

    # DEBUG: Used to print the mask to be used for tiling on the x axis.
    if debug_tiling:
        imageio.imwrite("mask_tiling_y.png", (255 * mask).astype(np.uint8), compress_level=5)

    # Tiles the image on the y-axis.
    tile_x_y = np.roll(tile_x, tile_x.shape[0] // 2, axis=1)
    tile_x_y = (tile_x_y * (1 - mask)) + (tile_x * mask)


    return tile_x_y

# Returns a power of two version of the image.
# Chooses the power of two slice of the original with min standard deviation between the slices on the 4 corners and the center of the image.
def power_of_two_min_std(image):

    # Gets the largest power of two that fits in the original image.
    p = np.floor(np.log2(image.shape[0]))
    q = np.floor(np.log2(image.shape[1]))

    r = np.minimum(q, p)

    res = int(2**r)

    # If the image is already power of two returns it.
    if image.shape[0] == image.shape[1] and image.shape[0] == res:
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