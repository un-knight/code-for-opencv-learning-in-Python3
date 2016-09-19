import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Original', image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - red: %d, green: %d, blue: %d\n" % (r, g, b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - red: %d, green: %d, blue: %d\n" % (r, g, b))

sub_image = image[0:100, 0:100]
cv2.imshow('sub image', sub_image)

image[0:100, 0:100] = (0, 255, 0)
cv2.imshow('Changed', image)
cv2.waitKey(0)
