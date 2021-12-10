import numpy as np
import cv2

# Contoh 1
img = cv2.imread('fundusimage.jpg')
RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Komponen R', RGB[:, :, 0])
cv2.imshow('Komponen G', RGB[:, :, 1])
cv2.imshow('Komponen B', RGB[:, :, 2])
cv2.imshow('Citra Warna', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Contoh 2
# img = cv2.imread('fundusimage.jpg')
# HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('Komponen H', HSV[:, :, 0])
# cv2.imshow('Komponen S', HSV[:, :, 1])
# cv2.imshow('Komponen V', HSV[:, :, 2])
# cv2.imshow('Citra Warna HSV', HSV)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Contoh 3
# img = cv2.imread('fundusimage.jpg')
# LAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow('Komponen L', LAB[:, :, 0])
# cv2.imshow('Komponen A', LAB[:, :, 1])
# cv2.imshow('Komponen B', LAB[:, :, 2])
# cv2.imshow('Citra Warna LAB', LAB)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
