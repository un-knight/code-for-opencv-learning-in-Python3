import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Path to Photo")
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Original", img)

canny = cv2.Canny(img, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
