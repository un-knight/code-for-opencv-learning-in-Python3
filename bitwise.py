import cv2
import numpy as np

rectangle = np.zeros((300, 300), dtype='uint8')
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype='uint8')
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)


bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("And", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Or", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("Xor", bitwiseXor)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("Not", bitwiseNot)

cv2.waitKey(0)