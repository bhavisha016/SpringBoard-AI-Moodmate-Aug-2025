import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# Load image
file_path = r"C:\Users\HP-PC\OneDrive\Documents\faces.jpeg"
if not os.path.exists(file_path):
    print("Error: File does not exist!")
    exit()

img = cv2.imread(file_path)

if img is None:
    print("Error: Could not read image.")
    exit()

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define blue color range
lower_blue = (100, 150, 0)
upper_blue = (140, 255, 255)

# Create mask for blue color
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply mask to original image
result = cv2.bitwise_and(img, img, mask=mask)

# Convert BGR to RGB for Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Display images
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title("Mask")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(result_rgb)
plt.title("Filtered")
plt.axis('off')

plt.show()
