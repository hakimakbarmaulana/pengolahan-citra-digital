import numpy as np
import os
import cv2
import matplotlib.pyplot as plt


# Contoh 4.1
# img = cv2.imread('xray.jpeg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Citra Asal', gray)
# br = len(img)
# kl = len(img[0])
# Z = np.zeros([br, kl])
# Min = float(np.min(gray))
# print("Min=", Min)
# Max = float(np.max(gray))
# print("Max=", Max)
# S = Max - Min  # Min - Max  #
# for i in range(br):
#     for j in range(kl):
#         Z[i, j] = (float(gray[i, j]) - Min) / S * 255
# Z = np.uint8(Z)
# print("Z=\n", Z)
# cv2.imshow('Citra hasil Contrast Streaching', Z)
# cv2.waitKey(0)


# Contoh 4.2
# def hist(kmp):
#     brs = len(kmp)
#     klm = len(kmp[0, :])
#     H = np.zeros(256)
#     for i in range(brs):
#         for j in range(klm):
#             for k in range(256):
#                 if kmp[i][j] == k:
#                     H[k] = H[k] + 1
#     n = brs * klm
#     for k in range(256):
#         H[k] = H[k] / n
#     return H
#
#
# img = cv2.imread('datadaun.jpeg')
# RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# R = RGB[:, :, 0]
# G = RGB[:, :, 1]
# B = RGB[:, :, 2]
# Bin = np.zeros(256)
# for i in range(256):
#     Bin[i] = i
# HistR = hist(R)
# HistG = hist(G)
# HistB = hist(B)
# plt.plot(Bin, HistR, '-r')
# plt.plot(Bin, HistG, '-g')
# plt.plot(Bin, HistB, '-b')
# plt.xlabel('Nilai Piksel')
# plt.ylabel('Frekuensi')
# plt.title('Histogram untuk Citra')
# plt.legend(["Komponen R", "Komponen G", "Komponen B"])
# plt.show()
# cv2.imshow("Citra Warna", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Contoh 4.3
img = cv2.imread('xray.jpeg')
Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Bin = np.zeros(256)
for i in range(256):
    Bin[i] = i
plt.figure(1)
n, bins, patches = plt.hist(Gray.ravel(), bins=Bin, color='#0504aa', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Nilai Piksel')
plt.ylabel('Frekuensi')
plt.title('Histogram untuk Komponen Gray Scale Sebelum Perataan Histogram')
cv2.imshow('Citra Awal', Gray)
Grayrata = cv2.equalizeHist(Gray)
plt.figure(2)
n, bins, patches = plt.hist(Grayrata.ravel(), bins=Bin, color='#0504aa', alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Nilai Piksel')
plt.ylabel('Frekuensi')
plt.title('Histogram untuk Komponen Gray Scale Setelah Perataan Histogram')
cv2.imshow('Hasil Perataan', Grayrata)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
