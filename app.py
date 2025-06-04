import cv2
import os
from utils import preprocess_image, generate_3d_output

# Define paths
input_path = "sample/floorplan.jpg"
output_path = "sample/floorplan_3d_output.jpg"

# Load image
image = cv2.imread(input_path)
if image is None:
    print("❌ Could not load image. Check the input path.")
    exit()

# Process image
preprocessed = preprocess_image(image)
output_image = generate_3d_output(preprocessed)

# Save result
cv2.imwrite(output_path, output_image)
print(f"✅ 3D floor plan saved to: {output_path}")
