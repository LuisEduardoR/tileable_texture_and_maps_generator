#!/usr/bin/python3

# Contains general functions used to edit images.

import matplotlib as mpl
import numpy as np

# Returns a monochrome version of an image.
def as_monochrome(rgb_image):

    hsv_image = mpl.colors.rgb_to_hsv(rgb_image)

    return hsv_image[:,:, 2]


# Performs gamma correction on a image.
def gamma_correction (midtone):

    gamma = 1

    midtone_normalized = midtone / 255

    if midtone < 128:
        midtone_normalized = midtone_normalized * 2
        gamma = 1 + ( 9 * ( 1 - midtone_normalized ) )
        gamma = min( gamma, 9.99 )
    elif midtone > 128:
        midtone_normalized = ( midtone_normalized * 2 ) - 1
        gamma = 1 - midtone_normalized
        gamma = max( gamma, 0.01 )

    return (1 / gamma)

# Performs the 'levels' operation that can be found on programs like GIMP or Photoshop on an image.
def level_image(gray_scale, in_shadow, in_highlight, midtones, out_shadow, out_highlight):

    # Creates the new image.
    leveled_image = gray_scale

    # Calculates the gamma correction to be used.
    gamma = gamma_correction(midtones)

    # Levels the input values.
    leveled_image = np.clip(255 * (leveled_image - in_shadow) / (float)(in_highlight - in_shadow), 0, 255)

    # Iterates the grayscale image assigning the leveled values to the new image.
    leveled_image = 255 * np.power((leveled_image / 255.0), gamma)

    # Levels the output values.
    leveled_image = ((leveled_image / 255.0) * (float)(out_highlight - out_shadow )) + out_shadow
                
    return leveled_image

# Gets the standard deviation between the pixels of an image.
def get_image_std(image):

    # Stores the average intensitity in a channel.
    channel_mean = []

    for channel in range(image.shape[2]):
        channel_mean.append(image[:,:,channel].mean())

    channel_mean = np.array(channel_mean)

    # Gets the difference between the channels and the channel average.
    diff = np.zeros(image.shape)

    for channel in range(image.shape[2]):
        diff[:,:,channel] = image[:,:,channel] - channel_mean[channel]

    # Returns the standard deviation between the differences.
    return diff.std()