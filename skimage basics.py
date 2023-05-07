"""
Skimage Basics
"""
from skimage import io, color
from skimage.transform import rescale,resize
from matplotlib import pyplot as plt
img_float = io.imread('om.jpg', as_gray = True) #float image
img_int = io.imread('om.jpg') #int image
img_rescaled = rescale(img_int, 1/4)
img_resize = resize(img_int,(200,200))
plt.imshow(img_float)
plt.imshow(img_int)
plt.imshow(img_rescaled)
plt.imshow(img_resize)

