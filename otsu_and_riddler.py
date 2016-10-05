import mahotas
import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Pat to Photo')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Image", img)

T = mahotas.thresholding.otsu(blurred)
# print("Otsu's threshold: %d" % T)

