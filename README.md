# Fabric Defect Detection & Length Measurement

This project uses a YOLO-based deep learning model to detect defects in fabric while it is being rolled on a roller. Additionally, the script estimates the length of the fabric rolled with and without defects in real-time.

## Features

- Detects fabric defects using a YOLO model.
- Calculates the total length of the fabric rolled.
- Separates defect-free fabric length from defective fabric length.
- Displays real-time video feed with defect annotations and length information.

## Requirements

- Python 3.8+
- OpenCV (`cv2`)
- Ultralytics YOLO
- Webcam or an external camera for scanning the fabric

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/SintreHere/FabricImageDataset.git
   cd FabricImageDataset
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python ultralytics
   ```
3. Place your trained YOLO model in the specified path and update the script accordingly.

## Usage

Run the script:

```sh
yolo_webcam.py
```
or 

```sh
yolo_webcam2.py
```
or

```sh
yolo_webcam3.py
```

Press `q` to exit the detection window.

## Configuration

Modify these parameters in `yolo_webcam2.py` to match your setup:

- **Roller Diameter (****`ROLLER_DIAMETER`****)**: Diameter of the roller in cm.
- **Fabric Speed (****`FABRIC_SPEED_CM_S`****)**: Speed at which the fabric moves in cm/s.

## Output

The script displays:

- Annotated video feed with defect detection.
- Real-time length measurement of fabric rolled with and without defects.
- Final fabric length printed in the console upon exit.

## Future Improvements

- Integration with a rotary encoder for precise fabric length measurement.
- Defect classification based on severity.
- Cloud-based storage of detected defect data.

## License

This project is open-source and available under the MIT License.

---

Developed by [Your Name]



