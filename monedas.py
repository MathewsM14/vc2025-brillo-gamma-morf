import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.imread('monedas.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img1_gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)

blur = cv2.GaussianBlur(img1_gray, (7, 7), 0)
_, imgbin = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.imshow(imgbin, cmap='gray')

imgbin2 = 255 - imgbin
plt.figure(figsize=(10, 5))
plt.imshow(imgbin2, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

imgbin2_erosion = cv2.erode(imgbin2, np.ones((5, 5), np.uint8), iterations=4)
plt.figure(figsize=(10, 5))
plt.imshow(imgbin2_erosion, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

_, markers = cv2.connectedComponents(imgbin2_erosion)
np.unique(markers)

plt.figure(figsize=(10, 5))
plt.imshow(markers, cmap='nipy_spectral', vmin=0, vmax=24)
plt.axis('off')