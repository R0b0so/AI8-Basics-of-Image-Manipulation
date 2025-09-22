import cv2
import matplotlib.pyplot as plt

image = cv2.imread("tree.jpg")
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RBG Image")
plt.show()

Image_Gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(Image_Gray, cmap="gray")
plt.title("Gray Image")
plt.show()

cropped_image=image[100:500,400:800]
image_cropped = cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(image_cropped)
plt.title("Cropped Image")
plt.show()