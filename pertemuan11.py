import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('dauntomat.jpg')# "gunung.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixel_values = image.reshape((-1, 3))
pixel_values = np.float32(pixel_values)
print(pixel_values.shape)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 2
_, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
centers[0] = np.array([0, 0, 0])  # Ubah BG jadi Hitam
labels = labels.flatten()
print(centers, labels)
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(image.shape)

# for i in range(len(image)):
#     for j in range(len(image[0])):
#         if sum(segmented_image[i, j]) == 0:
#             image[i, j] = np.zeros(3)
# plt.imshow(image)
plt.imshow(segmented_image)
plt.show()
