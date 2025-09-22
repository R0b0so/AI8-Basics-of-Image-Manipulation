import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread("tree.jpg")
(h,w,c)=image.shape
print(image.shape)
center = (w//2, h//2)
M=cv2.getRotationMatrix2D(center,145,1.0)
rotated = cv2.warpAffine(image,M,(w,h))
rotated_image=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_image)
plt.title("Rotated Image")
plt.show()

brightness_matrix = np.ones(image.shape,dtype="uint8")*75
brighter = cv2.add(image, brightness_matrix)
brighter_image = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_image)
plt.title("Brighter Image")
plt.show()

