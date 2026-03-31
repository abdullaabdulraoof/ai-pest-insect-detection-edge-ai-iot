from ultralytics import YOLO
import cv2
import time

from relay_control import fan_on, fan_off
from buzzer_alert import buzzer_on, buzzer_off
from config import MODEL_PATH, CAMERA_INDEX

print("Loading AI Model...")
model = YOLO(MODEL_PATH)

print("Starting Camera...")
cap = cv2.VideoCapture(CAMERA_INDEX)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    results = model(frame)

    insect_detected = False

    for r in results:
        if len(r.boxes) > 0:
            insect_detected = True

    if insect_detected:
        print("Insect detected!")
        buzzer_on()
        fan_on()
    else:
        buzzer_off()
        fan_off()

    annotated_frame = results[0].plot()
    cv2.imshow("AI Pest Detection System", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
