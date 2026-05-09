from ultralytics import YOLO
import cv2
import serial
import time


MODEL_PATH   = "best.onnx"
SERIAL_PORT  = "COM3"
BAUD_RATE    = 9600

def get_largest_box(results):
    #bounding box with the largest area
    largest = None
    largest_area = 0
    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        area = (x2 - x1) * (y2 - y1)
        if area > largest_area:
            largest_area = area
            largest = (x1, y1, x2, y2)
    return largest

def box_center(box):
    x1,y1,x2,y2 = box
    return (x1 + x2) / 2, (y1 + y2) / 2

def map_to_servo(value, in_min, in_max, out_min=30, out_max=150):
    #coordinate to angle
    value = max(in_min, min(in_max, value))  # clamp
    return int((value - in_min) / (in_max - in_min) * (out_max - out_min) + out_min)

def main():
    model = YOLO(MODEL_PATH)
    cap   = cv2.VideoCapture(0)

    ret, test_frame = cap.read()
    if not ret:
        raise RuntimeError("Could not read from webcam")
    frame_h, frame_w = test_frame.shape[:2]
    print(f"resolution: {frame_w}x{frame_h}")

    # Connect to Arduino
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    print("Connected to Arduino")
    print("Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.25, verbose=False)#low conf for now
        annotated = results[0].plot()

        box = get_largest_box(results)
        if box is not None:
            cx, cy = box_center(box)

            # Map center pixel to servo angle
            pan  = map_to_servo(cx, 0, frame_w, out_min=30, out_max=150)
            tilt = map_to_servo(cy, 0, frame_h, out_min=150, out_max=30)#inverted Y

            command = f"{pan},{tilt}\n"
            arduino.write(command.encode())

            #crosshair
            cv2.circle(annotated, (int(cx), int(cy)), 6, (0, 0, 255), -1)

        cv2.imshow("Servo Tracker", annotated)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    arduino.close()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
