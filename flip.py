import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to file')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow('Original', img)

flipped = cv2.flip(img, 1)
cv2.imshow('Flipped Horizontally', flipped)
cv2.waitKey(0)