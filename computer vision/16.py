import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load image
file_path = r"C:\Users\HP-PC\OneDrive\Documents\faces.jpeg"
if not os.path.exists(file_path):
    print("Error: File does not exist!")
    exit()

# Read in grayscale
img = cv2.imread(file_path, 0)

if img is None:
    print("Error: Could not read image.")
    exit()

# Apply binary inverse threshold
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# Create kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Apply erosion and dilation
erosion = cv2.erode(thresh, kernel, iterations=1)
dilation = cv2.dilate(thresh, kernel, iterations=1)

# Display results using Matplotlib
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(thresh, cmap='gray')
plt.title("Original Threshold")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(erosion, cmap='gray')
plt.title("Erosion")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(dilation, cmap='gray')
plt.title("Dilation")
plt.axis('off')

plt.show()
