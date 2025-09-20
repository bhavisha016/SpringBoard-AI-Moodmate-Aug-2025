import cv2
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

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Convert BGR to RGB for Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(img_rgb)
plt.axis('off')
plt.title("Contours")
plt.show()
