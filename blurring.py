import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to Photo')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow("Original", img)

# Averaging blurring
"""
blurred = np.hstack([
    cv2.blur(img, (3, 3)),
    cv2.blur(img, (5, 5)),
    cv2.blur(img, (7, 7))
])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)
"""

# Gaussian blurring
"""
blurred = np.hstack([
    cv2.GaussianBlur(img, (3, 3), 0),
    cv2.GaussianBlur(img, (5, 5), 0),
    cv2.GaussianBlur(img, (7, 7), 0),
])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)
"""

# Median blurring
"""
blurred = np.hstack([
    cv2.medianBlur(img, 3),
    cv2.medianBlur(img, 5),
    cv2.medianBlur(img, 7),
])
cv2.imshow("Median", blurred)
cv2.waitKey(0)
"""

# Bilateral blurring
blurred = np.hstack([
    cv2.bilateralFilter(img, 5, 21, 21),
    cv2.bilateralFilter(img, 7, 31, 31),
    cv2.bilateralFilter(img, 9, 41, 41)
])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)
