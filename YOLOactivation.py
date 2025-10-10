#!/usr/bin/env python3
import sys
import time
import cv2
import numpy as np

# Picamera2 for libcamera-based Raspberry Pi cameras
from picamera2 import Picamera2

# Ultralytics YOLO (supports YOLOv5/YOLOv8 .pt models)
from ultralytics import YOLO

def main(model_path: str, preview_size=(320, 320), inference_size=(640, 640)):
    # Load YOLO model
    model = YOLO(model_path)

    # Initialize camera
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"size": preview_size, "format": "RGB888"})
    picam2.configure(config)
    picam2.start()
    time.sleep(0.2)  # small warm-up

    window_name = "YOLO Live Preview"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    try:
        while True:
            # Capture frame as numpy array (RGB)
            frame = picam2.capture_array()

            # Optionally resize for inference speed vs accuracy
            input_frame = cv2.resize(frame, inference_size)

            # Run inference (set conf as needed; disable GPU on Pi)
            results = model.predict(
                source=input_frame,
                imgsz=inference_size[0],
                device="cpu",
                conf=0.25,
                verbose=False
            )

            # Get annotated image from results (Ultralytics helper)
            # results[0].plot() returns an RGB image with boxes/labels
            annotated = results[0].plot()

            # Convert RGB -> BGR for OpenCV display
            annotated_bgr = cv2.cvtColor(annotated, cv2.COLOR_RGB2BGR)

            # Show in window
            cv2.imshow(window_name, annotated_bgr)

            # Quit on 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cv2.destroyAllWindows()
        picam2.stop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 yolo_picam2_live.py /path/to/your_model.pt")
        sys.exit(1)
    main(sys.argv[1])
