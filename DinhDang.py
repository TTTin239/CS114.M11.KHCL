import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("paris1.jpg")
np_img = np.array(img)
print(f'Kich thuoc ảnh: {np_img.shape}')
plt.imshow(img[:,:,::-1])
plt.show()