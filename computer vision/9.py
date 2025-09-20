from PIL import Image
import pillow_avif  # make sure pillow-avif-plugin is installed
import cv2
import numpy as np

# Load AVIF image using Pillow
pil_img = Image.open(r"C:\Users\HP-PC\OneDrive\Documents\apple.avif")

# Convert to OpenCV format
img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply binary threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Show results
cv2.imshow("Original", gray)
cv2.imshow("Thresholded", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
