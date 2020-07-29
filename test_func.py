import numpy as np
import cv2

def gaussian_2d():
    """
    Create a 2-dimensional isotropic Gaussian map.
    :return: a 2D Gaussian map. 1000x1000.
    """
    mean = 0
    radius = 2.5
    # a = 1 / (2 * np.pi * (radius ** 2))
    a = 1.
    x0, x1 = np.meshgrid(np.arange(-5, 5, 0.01), np.arange(-5, 5, 0.01))
    x = np.append([x0.reshape(-1)], [x1.reshape(-1)], axis=0).T

    m0 = (x[:, 0] - mean) ** 2
    m1 = (x[:, 1] - mean) ** 2
    gaussian_map = a * np.exp(-0.5 * (m0 + m1) / (radius ** 2))
    gaussian_map = gaussian_map.reshape(len(x0), len(x1))

    max_prob = np.max(gaussian_map)
    min_prob = np.min(gaussian_map)
    gaussian_map = (gaussian_map - min_prob) / (max_prob - min_prob)
    gaussian_map = np.clip(gaussian_map, 0., 1.)
    return gaussian_map*255.0



heatmap = gaussian_2d()
cv2.imwrite('heat.jpg',heatmap)