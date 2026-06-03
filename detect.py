from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("videos/store.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0]
    )

    annotated = results[0].plot()

    cv2.imshow("Store", annotated)

    if cv2.waitKey(1) == 27:
        break

cap.release()