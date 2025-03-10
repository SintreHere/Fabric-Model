#This is for a test image. Change the Image link and run the script

import cv2
from ultralytics import YOLO

# Load the YOLO model
model_path = "/Users/flyair/Desktop/Fabric-Model1/best.pt"
model = YOLO(model_path)

# Path to the image
image_path = "WhatsApp Image 2025-01-29 at 14.35.04.jpeg"

# Load the image
image = cv2.imread(image_path)
if image is None:
    print("Failed to load the image. Please check the path.")
else:
    # Run inference on the image
    results = model(image)

    # Visualize results on the image
    annotated_image = results[0].plot()

    # Display the annotated image
    cv2.imshow("YOLOv11 Object Detection", annotated_image)
    
    # Wait until a key is pressed, then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
