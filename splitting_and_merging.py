import argparse
import numpy as np
import cv2


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the photo')
args = vars(ap.parse_args())

img = cv2.imread(args['image'])
cv2.imshow("Origin", img)

(B, G, R) = cv2.split(img)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

zeros = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()