import numpy as np
import os
import cv2
import statistics as st


# Contoh 5.1
img = cv2.imread('Xraynoisy.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Citra Asal', gray)
br = len(img)
kl = len(img[0])
ZZ = np.zeros([br, kl])
n = 11
H = 1 / (n**2) * np.ones([br, kl])
print(H)
for i in range(br - n):  # =2:br-3
    I = i + int(n/2)
    for j in range(kl - n):  # j=2:kl-3
        J = j + int(n/2)
        LL = 0
        for k in range(n):  # k=-2:2
            K = int(n/2) - k
            for l in range(n):  # l=-2:2
                L = int(n/2) - l
                LL = LL + H[int(n/2) + K, int(n/2) + L] * gray[I + K, J + L]
        ZZ[i, j] = LL
print("ZZ", ZZ)
ZZ = np.uint8(ZZ)
print(ZZ)
cv2.imshow('Citra hasil fiter rata-rata', ZZ)
cv2.imwrite('xraymean11.jpg', ZZ)
cv2.waitKey(0)


# Contoh 5.2
# img = cv2.imread('Xraynoisy.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Citra Asal', gray)
# br = len(img)
# kl = len(img[0])
# ZZ = np.zeros([br, kl])
# n = 11
# for i in range(br - n):  # i=2:br-3
#     I = i + int(n/2)
#     for j in range(kl - n):  # j=2:kl-3
#         J = j + int(n/2)  # i + 1  #
#         LL = np.zeros(n**2)
#         m = 0
#         for k in range(n):  # k=-2:2
#             K = int(n/2) - k
#             for l in range(n):  # l=-2:2
#                 L = int(n/2) - l
#                 LL[m] = gray[I + K, J + L]  # [i + K, j + L]
#                 m = m + 1
#             LL = np.sort(LL)
#             Med = st.median(LL)
#         ZZ[i, j] = Med
# print("ZZ", ZZ)
# ZZ = np.uint8(ZZ)
# print(ZZ)
# cv2.imshow('Citra hasil fiter median', ZZ)
# cv2.imwrite('xraymed11.jpg', ZZ)
# cv2.waitKey(0)
