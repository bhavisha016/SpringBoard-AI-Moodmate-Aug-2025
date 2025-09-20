from PIL import Image
import cv2
import numpy as np

# Load image using Pillow
pil_img = Image.open("C://Users//HP-PC//OneDrive//Documents//apple.avif")

# Convert to OpenCV format
img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

if img is None:
    print("Error: Could not read image.")
else:
    # Flip vertically (0), horizontally (1), or both (-1)
    flip_vertical = cv2.flip(img, 0)
    flip_horizontal = cv2.flip(img, 1)
    flip_both = cv2.flip(img, -1)

    # Show results
    cv2.imshow("Original", img)
    cv2.imshow("Flipped Vertically", flip_vertical)
    cv2.imshow("Flipped Horizontally", flip_horizontal)
    cv2.imshow("Flipped Both", flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
