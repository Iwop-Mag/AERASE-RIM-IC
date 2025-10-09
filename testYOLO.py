import cv2
from ultralytics import YOLO

# Load YOLOv11n model (downloads automatically if not present)
model = YOLO("yolo11n.pt")

# Open camera (0 = default USB webcam; for Pi Camera, use 'cv2.VideoCapture(0)' if using libcamera-compat)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO inference
    results = model(frame)

    # Get annotated frame (YOLO draws boxes + labels automatically)
    annotated_frame = results[0].plot()

    # Or manually draw bounding boxes with class + confidence
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])   # bounding box coords
        conf = float(box.conf[0])                # confidence
        cls = int(box.cls[0])                    # class id
        label = f"{model.names[cls]} {conf:.2f}"

        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(annotated_frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("YOLOv11n on Raspberry Pi", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()