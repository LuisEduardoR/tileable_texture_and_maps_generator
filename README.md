# tileable_texture_and_maps_generator

Made as final assigment for SCC0251 Image Processing course of ICMC-USP on 2019. 

## Authors:

* Gabriel de Moura Peres 
* Luís Eduardo Rozante de Freitas Pereira

# Generating Tileable Textures for 3D Rendering.

## Abstract: 

In 3D rendering sometimes it is very important to be abble to repeat a texture side by side multiple times without "seams" between the repetitions in order to save both memory and artistic effort. This is known as a tileable or seamless texture, along with it, lots of texture maps are used to allow faking ligthining effects, those could include, but are not limited to: height, normal and roughness maps. The program will, given the photo of a surface, with any resolution and close to uniform ligthining, generate a tileable Power of Two texture (one that has dimensions (width,height) equals to (2^p,2^q), being p and q natural numbers) and its normal, height and roughness maps.
