# tileable_texture_and_maps_generator

Made as final assigment for SCC0251 Image Processing course of ICMC-USP on 2019. 

## Authors:

* Gabriel de Moura Peres 
* Luís Eduardo Rozante de Freitas Pereira

---

# Generating Tileable Textures for 3D Rendering.

## Abstract: 

In 3D rendering sometimes it is very important to be abble to repeat a texture side by side multiple times without "seams" between the repetitions in order to save both memory and artistic effort. This is known as a tileable or seamless texture, along with it, lots of texture maps are used to allow faking ligthining effects, those could include, but are not limited to: height, normal and roughness maps. The program will, given the photo of a surface, with any resolution and close to uniform ligthining and texture, generate a tileable Power of Two texture (one that has dimensions (width,height) equals to (2^p, 2^q), being p and q natural numbers) and its normal, height and roughness maps.

---

## Example:

![Original Image](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/samples/texture_sample01.jpg)
*Original image of the surface*

![Tileable Image](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/samples/texture_sample01_artist_tile.jpg)
*Tileable version of the image, done by hand by an artist on GIMP.*

![Tiling Pattern](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/samples/texture_sample01_artist_tiling.jpg)
*Multiple tiles of the image next to each other.*

![Tileable Image Height Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/samples/texture_sample01_artist_height.jpg)
*Height map, done by hand by an artist on GIMP.*

![Tileable Image Normal Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/samples/texture_sample01_artist_normal.jpg)
*Normal map, generated using a plugin for GIMP.*

![Tileable Image Roghness Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/samples/texture_sample01_artist_rough.jpg)
*Roughness map, done by hand by an artist on GIMP.*

![3D Rendering](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/samples/sample01_artist_render.png)
*3D rendered material, made using the tileable texture and its maps, rendered on Unity Engine. (OBS: note that Unity uses a different system for roughness, information on how to convert roughness maps to the ones used in Unity is on the "UnityConversion.md" file in the tutorials folder)*

---

## Partial Report:

---

### Tiling the Texture:

The tiling process is probably one of the hardest parts of the project, so it was decided to get the map generation working first. But some research was done and a possible solution was found, this solution tries to automate what an artist would generally attempt when tiling a texture. The idea is to first select a square region of the input image with a power of two resolution, them put two instances of the image side-by-side horizontally, remove the seam on the center, them take the central square from the generated rectangle as a new texture and repeat the process vertically. For removing the seams, algorithms like "Best Tile" and "Min Cut" are being considered, also simulating the "Patch" tool that can be in found in programs like GIMP and Photoshop is a possibility, the problem is that this tool normally relies in the judgment of the artist to achieve good results, so an algorithm to analise how to use the tool would be necessary.

---

#### Grayscale Conversion:

Most of the texture maps that need to be generated are created from grayscale images, so a function to convert the input image (for now, before tiling) was added. The process consists in converting the image to HSV, and uginsg the V channel.texture_sample01_result_height.png

---

### Height Map:

The height map is generated by leveling and gamma correcting the grayscale image. Presently, hard coded values that produce good results in most situations are being used, but some analysis and user customization is planned to be added. Current idea is to analise the histogram of the image to get the min and max relevant intensities (Ones that appear a reasonable amount of times in the image, so anomalous intensities that barely happen are discarded) and use those values as input for the shadown and highlight parameters for the levels function, also, the user will be allowed to customize the midtones value. By assigning this values from histrogram, a larger difference between the minum and maximum height is allowed, and with the midtone customization the user can control how rough he wants the texture, and how steep the differences between heights are. 

![Generated Height Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/texture_sample01_result_height.png)
*Height map generated by the program from the hand made tile for sample 01.*

---

### Normal Map:

Throught the implementation details are still being researched, it was discovered that it's possible to convert height maps to normal maps, so, as height maps will also be generated, those will be used to generate the normal maps.

---

### Roughness Map:

Similar to the height map, the roughness map is generated by leveling the grayscale image. Like the height map, hard coded values are being used until better methods and customization is implemented.