from ultralytics import YOLO

# Load a model
#创建yolo模型
model = YOLO('C:\\mq\\yolov8\\code\\ultralytics\yolo\\v8\\MyDataSet\\MyYolov8.yaml')  # build a new model from YAML

#加载提前训练好的模型
model = YOLO('C:\\mq\\yolov8\\code\\ultralytics\\runs\\detect\\train3\\weights\\best.pt')

#使用 yaml文件 3个epochs
results = model.train(data = 'C:\\mq\\yolov8\\code\\ultralytics\\yolo\\v8\\MyDataSet\\MyCoco128.yaml', epochs = 300)

#评估模型表现
results = model.val()

#Performs objects detection on an image using the model
results = model('https://ultralytics.com/images/bus.jpg')

# 以ONNX模式导出模型
success = model.export(format = 'onnx')