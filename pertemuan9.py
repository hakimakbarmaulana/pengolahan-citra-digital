import cv2
import numpy as np
from matplotlib import pyplot as plt

# Contoh 9.1
# img = cv2.imread('morp.png', 0)
# ret, thresh = cv2.threshold(img, 127, 225, cv2.THRESH_BINARY)
# kernel = np.ones((5, 5), np.uint8)
# dilasi = cv2.dilate(thresh, kernel, iterations=1)
# plt.subplot(131), plt.imshow(img, cmap='gray')
# plt.title('Citra Awal'), plt.xticks([]), plt.yticks([])
# plt.subplot(132), plt.imshow(thresh, cmap='gray')
# plt.title('Citra Biner'), plt.xticks([]), plt.yticks([])
# plt.subplot(133), plt.imshow(dilasi, cmap='gray')
# plt.title('Hasil Dilasi'), plt.xticks([]), plt.yticks([])
# plt.show()


# Contoh 9.2
# img = cv2.imread('morp.png', 0)
# ret, thresh = cv2.threshold(img, 127, 225, cv2.THRESH_BINARY)
# kernel = np.ones((5, 5), np.uint8)
# erosi = cv2.erode(thresh, kernel, iterations=1)
# plt.subplot(131), plt.imshow(img, cmap='gray')
# plt.title('Citra Awal'), plt.xticks([]), plt.yticks([])
# plt.subplot(132), plt.imshow(thresh, cmap='gray')
# plt.title('Citra Biner'), plt.xticks([]), plt.yticks([])
# plt.subplot(133), plt.imshow(erosi, cmap='gray')
# plt.title('Hasil Erosi'), plt.xticks([]), plt.yticks([])
# plt.show()


# Contoh 9.3
# img = cv2.imread('morp.png', 0)
# ret, thresh = cv2.threshold(img, 127, 225, cv2.THRESH_BINARY)
# kernel = np.ones((3, 3), np.uint8)
# thresh = 255 - thresh
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
# plt.subplot(131), plt.imshow(img, cmap='gray')
# plt.title('Citra Awal'), plt.xticks([]), plt.yticks([])
# plt.subplot(132), plt.imshow(thresh, cmap='gray')
# plt.title('Citra Biner hasil operasi negatif'), plt.xticks([]),
# plt.yticks([])
# plt.subplot(133), plt.imshow(opening, cmap='gray')
# plt.title('Hasil Operasi Opening'), plt.xticks([]), plt.yticks([])
# plt.show()

# Contoh 9.4
img = cv2.imread('morp.png', 0)
ret, thresh = cv2.threshold(img, 127, 225, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Citra Awal'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(thresh, cmap='gray')
plt.title('Citra Biner'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(closing, cmap='gray')
plt.title('Hasil Operasi Closing'), plt.xticks([]), plt.yticks([])
plt.show()
