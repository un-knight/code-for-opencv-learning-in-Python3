import argparse
import cv2
import numpy as np
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to Photo')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(gray)

cv2.imshow("Histogram Equalization", np.hstack([gray, eq]))

plt.figure()
plt.title("Equalization Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

colors = ('b', 'g', 'r')
for (image, color) in zip((gray, eq), colors):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
