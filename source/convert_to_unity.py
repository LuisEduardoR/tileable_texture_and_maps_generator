import imageio
import numpy as np

roughness_map = imageio.imread("roughness.png")
metallic_map = np.ndarray((roughness_map.shape[0], roughness_map.shape[1], 4))
metallic_map[:, :, 3] = -roughness_map
imageio.imwrite("unity_metallic.png", metallic_map.astype(np.uint8))