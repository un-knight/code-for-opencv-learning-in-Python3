import cv2
import numpy as np


def translate(img, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return shifted


def rotate(img, angle, center=None, scale=1.0):
    (h, w) = img.shape[:2]
    if center is None:
        center = (w/2, h/2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(img, M, (w, h))

    return rotated


def resized(img, height=None, width=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = img.shape[:2]

    if height is None and width is None:
        return img
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)
    else:
        r = width / float(w)
        dim = (width, int(h*r))
    resized = cv2.resize(img, dim, interpolation=inter)
    return resized
