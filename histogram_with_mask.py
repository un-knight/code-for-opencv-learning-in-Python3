from matplotlib import pyplot as plt
import cv2
import numpy as np
import argparse


def plot_histogram(img, title, mask=None):
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    channels = cv2.split(img)
    colors = ('b', 'g', 'r')
    for (channel, color) in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--image', required=True, help='Path to Photo')
    args = vars(ap.parse_args())

    img = cv2.imread(args['image'])
    cv2.imshow("Original", img)
    plot_histogram(img, "Histogram for Original Image")

    mask = np.zeros(img.shape[:2], dtype='uint8')
    cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
    cv2.imshow("Mask", mask)

    masked = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Applying the mask", masked)

    plot_histogram(masked, "Histogram for Masked Image", mask)
    plt.show()
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
