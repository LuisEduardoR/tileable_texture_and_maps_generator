# tileable_texture_and_maps_generator

Made as final assigment for SCC0251 Image Processing course of ICMC-USP on 2019. 

## Authors:

* Gabriel de Moura Peres 
* Luís Eduardo Rozante de Freitas Pereira

# Generating Tileable Textures for 3D Rendering.

## Abstract: 

In 3D rendering sometimes it is very important to be abble to repeat a texture side by side multiple times without "seams" between the repetitions in order to save both memory and artistic effort. This is known as a tileable or seamless texture, along with it, lots of texture maps are used to allow faking ligthining effects, those could include, but are not limited to: height, normal and roughness maps. The program will, given the photo of a surface, with any resolution and close to uniform ligthining and texture, generate a tileable Power of Two texture (one that has dimensions (width,height) equals to (2^p, 2^q), being p and q natural numbers) and its normal, height and roughness maps.

## Example:

![Original Image](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/Samples/texture_sample01.jpg)
*Original image of the surface*

![Tileable Image](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/Samples/texture_sample01_artist_tile.jpg)
*Tileable version of the image, done by hand by an artist on GIMP.*

![Tiling Pattern](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/Samples/texture_sample01_artist_tiling.jpg)
*Multiple tiles of the image next to each other.*

![Tileable Image Height Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/Samples/texture_sample01_artist_height.jpg)
*Height map, done by hand by an artist on GIMP.*

![Tileable Image Normal Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/Samples/texture_sample01_artist_normal.jpg)
*Normal map, generated using NVIDIA plugin for GIMP.*

![Tileable Image Roghness Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/Samples/texture_sample01_artist_rough.jpg)
*Roughness map, done by hand by an artist on GIMP.*

![3D Rendering](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/Samples/sample01_artist_render.png)
*3D rendered material, made using the tileable texture and its maps, rendered on Unity Engine. (OBS: note that Unity uses a different system for roughness map, for information on how to convert roughness map to the map used in Unity check the "TO DO" file in the tutorials folder)*