from matplotlib import pyplot as plt
import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to Photo')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow("Origin", img)

channels = cv2.split(img)
fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[1], channels[0]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([channels[0], channels[2]], [0, 1],
                    None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

print("2D histogram shape: %s, with %d values" %
      (hist.shape, hist.flatten().shape[0]))

plt.show()
cv2.waitKey(0)