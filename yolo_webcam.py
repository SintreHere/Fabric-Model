#This is Web Cammera operated Script

import cv2
from ultralytics import YOLO

# Load the YOLO model
model_path = "/Users/flyair/Desktop/Fabric-Model1/best.pt"
model = YOLO(model_path)

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run inference
    results = model(frame)

    # Visualize results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLOv11n Object Detection", annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
