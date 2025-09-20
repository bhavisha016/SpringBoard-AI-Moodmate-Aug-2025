from PIL import Image
import pillow_avif  # make sure pillow-avif-plugin is installed
import cv2
import numpy as np

# Load AVIF image using Pillow
pil_img = Image.open(r"C:\Users\HP-PC\OneDrive\Documents\apple.avif")

# Convert to OpenCV format
img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

# Check if image loaded correctly
if img is None:
    print("Error: Could not read image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show both
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save grayscale image
cv2.imwrite("grayscale_output.jpg", gray)
