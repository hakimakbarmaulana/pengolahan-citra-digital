import cv2
import numpy as np

# kode program 1.1
# img = cv2.imread('bakteri1.jpeg')
# cv2.imshow('Menampilkan Citra', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# kode program 1.2
# img = cv2.imread('bakteri1.jpeg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Menampilkan Citra', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# kode program 1.3
# img = cv2.imread('bakteri1.jpeg')
# IM = (0.2989 * img[:, :, 0] + 0.5870 * img[:, :, 1] + 0.1141 * img[:, :, 2])
# IM = IM.astype(np.uint8)
# print(IM)
# cv2.imshow('Menampilkan Citra 1', IM)
# cv2.waitKey(0)

# Show 2 gambar
# img1 = cv2.imread('bakteri1.jpeg')
# img2 = cv2.imread('bakteri2.jpeg')
# cv2.imshow('Menampilkan Citra 1', img1)
# cv2.imshow('Menampilkan Citra 2', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Save gambar
# img = cv2.imread('bakteri1.jpeg')
# IM = (0.2989 * img[:, :, 0] + 0.5870 * img[:, :, 1] + 0.1141 * img[:, :, 2])
# IM = IM.astype(np.uint8)
# print(IM)
# cv2.imshow('Menampilkan Citra 1', IM)
# cv2.imwrite("bakterigray.jpg", IM)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# operasi dasar
img = cv2.imread('bakteri1.jpeg')
cv2.imshow('Menampilkan Citra Asal', img)  # menampilkan citra
cerah = int(input("Tingkat Kecerahan:"))
br = len(img[:, :, 0])
kl = len(img[0, :, 0])
for i in range(br):
    for j in range(kl):
        img[i, j, :] = img[i, j, :] + cerah
        if (img[i, j, 0] > 255):
            img[i, j, 0] = 255
        if (img[i, j, 1] > 255):
            img[i, j, 1] = 255
        if (img[i, j, 2] > 255):
            img[i, j, 2] = 255
cv2.imshow('Menampilkan Citra Cerah', img)
cv2.imwrite("bakterigray.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
