from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")

def detect_objects(frame):
    results = model(frame)[0]
    players = []
    ball = None
    for box in results.boxes:
        cls = int(box.cls[0])
        x1,y1,x2,y2 = box.xyxy[0]
        if cls == 0:
            players.append([int(x1),int(y1),int(x2),int(y2)])
        if cls == 32:
            ball = [int(x1),int(y1),int(x2),int(y2)]
    return players, ball