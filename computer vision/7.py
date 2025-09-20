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

# Apply Gaussian Blur (15x15 kernel)
blur = cv2.GaussianBlur(img, (15, 15), 0)

# Show both
cv2.imshow("Original", img)
cv2.imshow("Blurred", blur)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save the blurred image
cv2.imwrite("blurred_output.jpg", blur)
