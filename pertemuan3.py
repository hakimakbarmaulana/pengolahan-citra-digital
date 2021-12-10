import numpy as np
import cv2


# Contoh 3.1
# img = cv2.imread('bakteri2.jpeg')
# Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Citra Gray Scale', Gray)
# br = len(Gray)
# kl = len(Gray[0])
# CitraNegatif = np.uint8(np.zeros([br, kl]))
# for i in range(br):
#     for j in range(kl):
#         CitraNegatif[i, j] = 255 - Gray[i, j]
# cv2.imshow('Citra Negatif', CitraNegatif)
# cv2.waitKey(0)


# Contoh 3.2
# img = cv2.imread('bakteri2.jpeg')
# cv2.imshow('Citra Asal', img)
# br = len(img[:, :, 0])
# kl = len(img[0, :, 0])
# Z = np.zeros([br, kl, 3])
# c = 1
# n = 1.1
# for i in range(br):
#     for j in range(kl):
#         for k in range(3):
#             Z[i, j, k] = c * float(img[i, j, k]) ** n
#         if Z[i, j, k] >= 255:
#             Z[i, j, k] = 255
# Z = np.uint8(Z)
# cv2.imshow('Citra Perbaikan Gamma', Z)
# cv2.waitKey(0)


# Contoh 3.3
img = cv2.imread('bakteri2.jpeg')
cv2.imshow('Citra Asal', img)
br = len(img[:, :, 0])
kl = len(img[0, :, 0])
Z = np.zeros([br, kl, 3])
c = 30
for i in range(br):
    for j in range(kl):
        for k in range(3):
            Z[i, j, k] = c * np.log(1 + float(img[i, j, k]))
Z = np.uint8(Z)
cv2.imshow('Citra hasil log', Z)
cv2.waitKey(0)
