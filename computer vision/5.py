from PIL import Image
import pillow_avif  # make sure pillow-avif-plugin is installed
import cv2
import numpy as np

# Load AVIF image using Pillow
pil_img = Image.open(r"C:\Users\HP-PC\OneDrive\Documents\apple.avif")

# Convert to OpenCV format
img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

# Check if the image loaded correctly
if img is None:
    print("Error: Could not read image.")
    exit()

# Resize image (width=300, height=300)
resized = cv2.resize(img, (300, 300))

# Show both
cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save the resized image
cv2.imwrite("resized_output.jpg", resized)
