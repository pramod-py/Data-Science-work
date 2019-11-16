import cv2
import numpy as np

img1 = cv2.imread("road.jpg")
img2 = cv2.imread("car.jpg")
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
print(img1[0, 0])
print(img2[0, 0])
weighted = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
ret, mask = cv2.threshold(img2_gray, 252, 255, cv2.THRESH_BINARY_INV)
sum = cv2.add(img2, img1)
cv2.imshow("sum", sum)
cv2.imshow("threshold", mask)
cv2.imshow("img2gray", img2_gray)
cv2.imshow("weighted", weighted)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()