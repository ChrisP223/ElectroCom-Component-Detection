from ultralytics import YOLO
import cv2

model = YOLO("best.onnx",task='detect')
print(model.names)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    results = model(frame,conf=0.25,verbose=False)
    annotated = results[0].plot()
    cv2.imshow("YOLOv8", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
