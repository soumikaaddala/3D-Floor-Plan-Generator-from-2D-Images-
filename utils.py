import cv2
import numpy as np

def preprocess_image(img):
    # Convert to grayscale and resize
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (256, 256))
    return resized

def generate_3d_output(preprocessed_img):
    # Simulated 3D-like output (adds blue tint for illustration)
    img_color = cv2.cvtColor(preprocessed_img, cv2.COLOR_GRAY2BGR)
    img_color[:, :, 0] = 255  # Add blue to simulate 3D visualization
    return img_color
