from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

model.train(data='./data/data.yaml', epochs=20, imgsz=720, batch=8, name='yolov8n-scoreboard')  # train the model

model.export(format='onnx')  # export the model to ONNX format