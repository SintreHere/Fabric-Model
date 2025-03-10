#This script has fabric cloth measurement analytics using the roller speed and dimensions

import cv2
from ultralytics import YOLO
import time

# Constants
ROLLER_DIAMETER = 10.0  #in cm 
ROLLER_CIRCUMFERENCE = ROLLER_DIAMETER * 3.1416  
FABRIC_SPEED_CM_S = 10.0  # cm/s 

# Variables
total_length_with_defects = 0.0 
total_length_without_defects = 0.0 
start_time = time.time() 

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
    detections = results[0].boxes  # Detected objects (bounding boxes)

    # Check for defects
    has_defect = len(detections) > 0

    # Calculate elapsed time since the last frame
    elapsed_time = time.time() - start_time
    start_time = time.time()

    # Calculate the fabric rolled in this frame
    rolled_length = FABRIC_SPEED_CM_S * elapsed_time  # Length in cm

    # Update total lengths based on defects
    if has_defect:
        total_length_with_defects += rolled_length
    else:
        total_length_without_defects += rolled_length

    # Visualize results on the frame
    annotated_frame = results[0].plot()

    # Add length information to the frame
    cv2.putText(
        annotated_frame,
        f"Length with Defects: {total_length_with_defects:.2f} cm",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2,
    )
    cv2.putText(
        annotated_frame,
        f"Length without Defects: {total_length_without_defects:.2f} cm",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2,
    )

    # Display the annotated frame
    cv2.imshow("YOLOv11n Object Detection", annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Final output
print(f"Total Fabric Length with Defects: {total_length_with_defects:.2f} cm")
print(f"Total Fabric Length without Defects: {total_length_without_defects:.2f} cm")
