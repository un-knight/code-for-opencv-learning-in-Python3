from func import imutils
import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to file.")
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow("Origin", img)
cv2.waitKey(0)
cv2.imshow("Resized", imutils.resized(img, width=50))
cv2.waitKey(0)