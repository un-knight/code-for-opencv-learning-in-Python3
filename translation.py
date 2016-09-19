import argparse
import cv2
from func import imutils


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow("Original", img)
cv2.waitKey(0)

rotated = imutils.rotate(img, 45)
cv2.imshow("Rotated 45 degree.", rotated)
cv2.waitKey(0)