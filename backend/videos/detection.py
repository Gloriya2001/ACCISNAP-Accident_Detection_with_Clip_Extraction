from ultralytics import YOLO

def detect_accidents(video_path):
    model = YOLO('yolov8n.pt')  # Load YOLOv8 model
    results = model(video_path)
    return results  # This returns the detected results
