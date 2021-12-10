import cv2
import numpy as np

# Contoh 6.1
# img = cv2.imread('xray.jpeg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
# # prewitt
# kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
# kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
# img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
# img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
# cv2.imshow("Original Image", img)
# cv2.imshow("Prewitt X", img_prewittx)
# cv2.imshow("Prewitt Y", img_prewitty)
# cv2.imshow("Prewitt", img_prewittx + img_prewitty)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Contoh 6.2
# img = cv2.imread('xray.jpeg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
# # sobel
# img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=5)
# img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=5)
# img_sobel = img_sobelx + img_sobely
# cv2.imshow("Original Image", img)
# cv2.imshow("Sobel X", img_sobelx)
# cv2.imshow("Sobel Y", img_sobely)
# cv2.imshow("Sobel", img_sobel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Contoh 6.3
img = cv2.imread('xray.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
# sobel
ddepth = cv2.CV_16S
kernel_size = 3
img_laplacian = cv2.Laplacian(img_gaussian, ddepth, ksize=kernel_size)
cv2.imshow("Original Image", img)
cv2.imshow("Laplacian", np.uint8(img_laplacian))
cv2.waitKey(0)
cv2.destroyAllWindows()
