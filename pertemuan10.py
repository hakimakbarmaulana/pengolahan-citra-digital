import cv2
import numpy as np
from matplotlib import pyplot as plt

# Contoh 10.1
# img = cv2.imread('dauntomat.jpg', 0)
# ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow('Citra Gray', img)
# cv2.imshow('Citra Biner', thresh1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Contoh 10.1 manual
# img = cv2.imread('dauntomat.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# br = len(gray)
# kl = len(gray[0, :])
# Y = np.zeros([br, kl])
# for i in range(br):
#     for j in range(kl):
#         if gray[i, j] < 128:
#             Y[i, j] = 0
#         else:
#             Y[i, j] = 255
# Y = np.uint8(Y)
# cv2.imshow('Citra Gray', img)
# cv2.imshow('Citra Biner', Y)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Contoh 10.2
img = cv2.imread('dauntomat.jpg', 0)
# global thresholding
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Otsu's thresholding
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
plt.show()
