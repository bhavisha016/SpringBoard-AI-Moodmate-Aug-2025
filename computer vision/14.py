import cv2
import numpy as np
import matplotlib.pyplot as plt
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

# Initialize mask and models for grabCut
mask = np.zeros(img.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# Define rectangle around foreground object
rect = (50, 50, img.shape[1]-50, img.shape[0]-50)  # Adjust rectangle to image size

# Apply grabCut algorithm
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Create mask for foreground
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
result = img * mask2[:, :, np.newaxis]

# Convert BGR to RGB for Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Display original and foreground-extracted images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(result_rgb)
plt.title("Foreground Extracted")
plt.axis('off')

plt.show()
