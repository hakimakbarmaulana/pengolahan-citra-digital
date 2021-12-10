import cv2
import numpy as np
import flevelset as lv
import time


img = cv2.imread('data1.png')  # 'fruit-selection-white-background.jpg')  #
# img = cv2.resize(img, None, fx=1/5, fy=1/5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
br, kl = len(gray), len(gray[0])
tms = 0.2
it_in = 15
it_out = 50
sig = 1.5
img_s = cv2.GaussianBlur(gray, (15, 15), sig)


def grad(x):
    return np.array(np.gradient(x))


def norm(x, axis=0):
    return np.sqrt(np.sum(np.square(x), axis=axis))


def stopping_fun(x):
    return 1. / (1. + norm(grad(x))**2)


g = stopping_fun(img_s)
c0 = 2
phi = c0*np.ones((br, kl))
phi[5:-5, 5:-5] = -c0

tresh0 = lambda x: 255 if x <= 2 else 0
tresh = np.vectorize(tresh0)

for i in range(it_out):
    phi = lv.levelset(phi, g, tms, it_in)
    gbr = tresh(phi)
    cv2.imshow('Iterasi', np.uint8(gbr))
    cv2.waitKey(1)
    time.sleep(0.1)
cv2.destroyAllWindows()

cv2.imshow('Citra asal', img)
cv2.imshow('Citra segment', np.uint8(gbr))
cv2.waitKey(0)
cv2.destroyAllWindows()
