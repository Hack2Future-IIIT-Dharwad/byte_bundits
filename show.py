<<<<<<< HEAD
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('output_image copy.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, threshold1=30, threshold2=100)
plt.figure(figsize=(10,10))
plt.imshow(edges, cmap='gray')
plt.title('Wireframe Model')
plt.show()
=======
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('output_image copy.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, threshold1=30, threshold2=100)
plt.figure(figsize=(10,10))
plt.imshow(edges, cmap='gray')
plt.title('Wireframe Model')
plt.show()
>>>>>>> 88f1ca129313f9b4f38c0d71d8d3f5eca2005956
