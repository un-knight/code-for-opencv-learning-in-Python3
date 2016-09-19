import argparse
import cv2
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to file')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('Original', img)

M = np.ones(img.shape, dtype='uint8') * 100
added = cv2.add(img, M)
cv2.imshow("Added", added)

M = np.ones(img.shape, dtype='uint8') * 50
sub = cv2.subtract(img, M)
cv2.imshow("Substracted", sub)
cv2.waitKey(0)