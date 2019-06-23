# Converting Roughness Maps to use in Unity

Unity uses a format in wich the metalicity of a texture is stored in the red channel and the smoothness map (inverted roughness map) is stored on the alpha channel.

A python 3 program to generate this images automatically is provided in the source folder, note that you will need imageio and numpy.

To run the program execute:

    python unity_conversion.py

Them, when asked, provided the roughness map file name.

Follow the remaining instructions from the program.

The generated image will be saved as:

    <roughness map file name provided>_unity.png

Them you can just import the file into Unity.
