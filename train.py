import sys
sys.path.append("./ultralytics")
from ultralytics import YOLO

from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML

# Train the model
model.train(data='face.yaml', epochs=100, imgsz=640)