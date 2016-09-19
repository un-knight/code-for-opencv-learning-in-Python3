import argparse
import numpy as np
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the photo')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow("Origin", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab)

cv2.waitKey(0)
cv2.destroyAllWindows()