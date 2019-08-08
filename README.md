# tileable_texture_and_maps_generator

Made as final assigment for SCC0251 Image Processing course of ICMC-USP on 2019. 

## Authors:

* Amanda de Moura Peres
* Luís Eduardo Rozante de Freitas Pereira

---

# Generating Tileable Textures and Texture Maps for 3D Rendering.

## Abstract: 

In 3D rendering sometimes it is very important to be abble to repeat a texture side by side multiple times without "seams" between the repetitions in order to save both memory and artistic effort. This is known as a tileable or seamless texture, along with it, lots of texture maps are used to allow faking ligthing effects, those could include, but are not limited to: height, normal and roughness maps. This program will, given the photo of a surface, with any resolution and close to uniform ligthing and texture, generate a tileable Power of Two texture (one that has dimensions (width,height) equals to (2^p, 2^q), being p and q natural numbers) and its normal, height and roughness maps.

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
*3D rendered scene, made using a material created from the tileable texture and its maps, rendered on Unity Engine. (OBS: note that Unity uses a different system for roughness, information on how to convert roughness maps to the ones used in Unity is on the "UnityConversion.md" file in the tutorials folder)*

---

## Report:

---

#### Samples:

The samples used for the program can be found on the "samples" folder, they are images taken by the group of various surfaces, some have received post-processing in the form of contrast and color manipulation to create a nicer appearence. 

---

### Tiling the Texture:

The tiling process is probably one of the hardest parts of the project, so, due to lack of time, a very simple method was opted for. What is being done is the slicing of the original image into a version with width and height being a power of two, it was decided to make all textures squares for now. The slice is selected between the four corners plus the center of the image using the standard deviation between the channel value differences and the channel mean as a criteria, the one with the minimum value is selected. This is done in an attempt to get the slice that would be, most of the time, easier to tile. Using the slice with the minimum standard deviation, generally the part of the image with the least texture and lighting variance, should allow for making tiles with better final appearence, as, though the image provided should be already pretty uniform, this would eliminate most of the remaining outlier regions. Them, for each axis of the texture the following proccess is done: first, a mask is generated with a gradual fade towards the center of the image; second, a multiplier based on the grayscale of the image is added to the mask, with the objective of trying to better keep details in the faded region; third the image is rolled along the axis by 50% of it's size, this makes the image tileable on the axis it's was rolled on, but ends up moving the original seam between the textures to the middle of the image; finally, the produced mask is applied to the original texture and the result is used to cover the seam from the step before. After repeating this proccess to both axis the result will be a completly tileable texture.

![Generated Height Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/texture_sample01_mask_example.png)
*Mask generated for one of the axis of the samples/texture_sample01.jpg slice that better fitted the criteria.*

![Generated Height Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/texture_sample01_tile.png)
*Tileable texure generated from the samples/texture_sample01.jpg slice that better fitted the criteria.*

![Generated Height Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/texture_sample01_tiling.png)
*Multiple tiles of the image next to each other.*

---

#### Grayscale Conversion:

Most of the texture maps that need to be generated are created from grayscale images, so a function to convert the power of two image was added. The process consists in combining the RGB channels into one using the 0.229, 0.587 and 0.114 weights respectively. 

---

### Height Map:

The height map is generated by leveling and gamma correcting the grayscale image. The histogram of the image is used to get the min and max relevant intensities (Ones that appear a reasonable amount of times in the image, so anomalous values that barely happen are discarded) in order to increase the intensity range for the height map, these values, along with an user customizable height multiplier, are used as parameters for the leveling and gamma correction function, generating better results and allowing user customization.

![Generated Height Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/texture_sample01_height.png)
*Height map generated by the program from the tileable image.*

---

### Normal Map:

The normal map is generated using the height map as a base, transforming the grayscale value into vector space and them saving XYZ to RGB. The vector space values can be calculated via the discrete partial derivatives from the normalized height map. More details can be found on the bibliography [9].

![Generated Normal Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/texture_sample01_normal.png)
*Normal map generated by the program from the tileable image.*

---

### Roughness Map:

Similar to the height map, the roughness map is also generated by leveling and gamma correcting the grayscale, but the image is inverted before saving, making dark areas lighter on the final texture indicating more roughness, what will generate less light reflection in the 3D rendering. A value provided by the user is used as a parameter for the leveling and gamma correction, allowing some customization on how rough the texture will be.  

![Generated Roughness Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/texture_sample01_rough.png)
*Roughness map generated by the program from the tileable image.*

---

## Conclusion:

The final result turned out really well for most textures given the simplicity of the methods used, as can be seen in the following render:

![3D Rendering](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/sample01_render.png)
*3D rendered scene, made using a material created from the generated tileable texture for samples/texture_sample01.jpg and its maps, rendered on Unity Engine.*

But for others some problems are apparent, the method choosen for the tiling proccess tends to produce very visible duplication of some details from the image and also doesn't generate good results for textures with very apparent geometrical patterns.

![Generated Height Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/texture_sample03_tile.png)
*Tileable texure generated from samples/texture_sample03.jpg, note that the squares do not match what would be expected.*

Another problem is the method used to select the best slice, though apparently working with most of the samples, sample 07 caused trouble, making the program select what an artist would consider the worst slice possible, what indicates a better selection method should be considered.

![Generated Height Map](https://github.com/LuisEduardoR/tileable_texture_and_maps_generator/blob/master/results/texture_sample07_best_slice.png)
*Selected "best" slice from samples/texture_sample07.jpg, note the inclusion of what should have been considered an anomaly in the slice.*

The texture map generation ended up being the most successfull part of the program, only possible needing more customization to allow better handling of some cases that would be ambigous for probably most algorithmic decisions. The tiling proccess also could use customization as well, allowing the user to select the axis in which the image will be tiled, as some textures are only meant to be tileable in one direction, the option to completly skip the tiling proccess if only the texture maps are desired would also be a good addition. Ultimatly, the program serves it's purpose for most cases that would, in a real situation, only take artist time for pretty simple handwork during a 3d render production, and with some improvements, might be usable even for some trickier situations, what is a pretty favorable result.

---

## Bibliography:

* [1] http://pages.cs.wisc.edu/~preasa/534/paper.pdf
* [2] https://computergraphics.stackexchange.com/questions/5317/seamless-textures
* [3] http://graphics.stanford.edu/papers/tile_mapping_gh2004/final/paper_final.pdf
* [4] http://eric-yuan.me/texture-synthesis/
* [5] https://www.ripublication.com/irph/ijict_spl/ijictv4n16spl_08.pdf
* [6] http://cs.brown.edu/courses/cs129/results/proj4/jvkoh/
* [7] https://stackoverflow.com/questions/2368728/can-normal-maps-be-generated-from-a-texture
* [8] https://www.gamedev.net/forums/topic/475213-generate-normal-map-from-heightmap-algorithm/
* [9] https://blender.stackexchange.com/questions/52865/creating-normal-maps-from-a-texture
