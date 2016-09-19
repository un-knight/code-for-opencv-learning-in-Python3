import argparse
import numpy as np
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow("Origin", img)

mask = np.zeros(img.shape[:2], dtype='uint8')
(cX, cY) = (int(mask.shape[1]/2), int(mask.shape[0]/2))
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)
