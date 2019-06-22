#!/usr/bin/python3

# Contains general functions used to edit images.

import numpy as np

# Returns a monochrome version of an image.
def as_monochrome(rgb_image):
    gray_scale = 0.229 * rgb_image[:, :, 0] + 0.587 * rgb_image[:, :, 1] + 0.114 * rgb_image[:, :, 2]
    return np.rint(gray_scale).astype(np.uint8)


# Calculates the gamma correction to be used.
def get_gamma (midtone):

    gamma = 1.0

    midtone_normalized = midtone / 255.0

    if midtone < 128.0:
        midtone_normalized = midtone_normalized * 2.0
        gamma = 1.0 + ( 9.0 * ( 1.0 - midtone_normalized ) )
        gamma = min( gamma, 9.99 )
    elif midtone > 128.0:
        midtone_normalized = ( midtone_normalized * 2.0 ) - 1.0
        gamma = 1.0 - midtone_normalized
        gamma = max( gamma, 0.01 )

    return (1.0 / gamma)

# Performs the 'levels' operation that can be found on programs like GIMP or Photoshop on an image.
def level_image(gray_scale, in_shadow, in_highlight, midtones, out_shadow, out_highlight):

    # Creates the new image.
    leveled_image = gray_scale.astype(float)

    # Gets the gama value.
    gamma = get_gamma(midtones)

    # Levels the input values.
    leveled_image = np.clip(255.0 * (leveled_image - in_shadow) / (float)(in_highlight - in_shadow), 0.0, 255.0)

    # Iterates the grayscale image assigning the leveled values to the new image.
    leveled_image = 255.0 * np.power((leveled_image / 255.0), gamma)

    # Levels the output values.
    leveled_image = ((leveled_image / 255.0) * (float)(out_highlight - out_shadow )) + out_shadow
                
    return np.clip(leveled_image, 0.0, 255.0).astype(np.uint8)

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


def get_image_histogram(gray_scale, level_count):
    histogram = np.zeros(level_count).astype(np.uint8)

    for i in range(level_count):
        histogram[i] += np.where(gray_scale == i)[0].shape[0]

    return histogram
