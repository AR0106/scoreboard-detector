import cv2

model = cv2.dnn.readNetFromONNX("scoreboard-model.onnx")

model.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
model.setPreferableTarget(cv2.dnn.DNN_BACKEND_DEFAULT)

image = cv2.imread("test.jpg")
blob = cv2.dnn.blobFromImage(image, scalefactor=1/255.0, size=(736, 736), swapRB=True, crop=False)

model.setInput(blob)
outputs = model.forward()

cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()