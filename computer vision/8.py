from PIL import Image
import pillow_avif  # make sure pillow-avif-plugin is installed
import cv2
import numpy as np

# Load AVIF image using Pillow
pil_img = Image.open(r"C:\Users\HP-PC\OneDrive\Documents\apple.avif")

# Convert to OpenCV format
img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

# Create a blank canvas (500x500) if you want to draw shapes on top
canvas = np.zeros((500, 500, 3), dtype="uint8")

# Draw shapes on canvas
cv2.line(canvas, (0, 0), (500, 500), (255, 0, 0), 5)
cv2.rectangle(canvas, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.circle(canvas, (300, 300), 80, (0, 0, 255), -1)

# Add text
cv2.putText(canvas, "OpenCV Demo", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Show results
cv2.imshow("Original Image", img)
cv2.imshow("Shapes and Text", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
