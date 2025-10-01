import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("test.png")
if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
else:
    raise ValueError("Could not load image")

edges = cv2.Canny(gray, 100, 200)

orb = cv2.ORB_create()
kp, desc = orb.detectAndCompute(gray, None)
annotatedImage = cv2.drawKeypoints(
    img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

plt.imshow(cv2.cvtColor(annotatedImage, cv2.COLOR_BGR2RGB))
plt.show()
