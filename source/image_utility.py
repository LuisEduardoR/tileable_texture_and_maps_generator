# Contains functions used by multiple images.
import matplotlib as mpl
import numpy as np
import imageio


def as_monochrome(rgb_image):

    hsv_image = mpl.colors.rgb_to_hsv(rgb_image)

    return hsv_image[:,:, 2]


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

def level_image(gray_scale, in_shadow, in_highlight, midtones, out_shadow, out_highlight):

    # Creates the new image.
    leveled_image = gray_scale

    # Calculates the gamma correction to be used.
    gamma = gamma_correction(midtones)

    # Levels the input values.
    leveled_image = 255 * np.clip((leveled_image - in_shadow) / (float)(in_highlight - in_shadow), 0, 255)

    # Iterates the grayscale image assigning the leveled values to the new image.
    leveled_image = 255 * np.power((leveled_image / 255.0), gamma)

    # Levels the output values.
    leveled_image = ((leveled_image / 255.0) * (float)(out_highlight - out_shadow )) + out_shadow
                
    return leveled_image
