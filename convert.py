from ultralytics import YOLO

model = YOLO('./runs/detect/yolov8n-scoreboard15/weights/best.pt')  # load a pretrained model (recommended for training)

model.export(format='onnx')  # export the model to ONNX format