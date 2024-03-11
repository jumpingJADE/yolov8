from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("C:\\mq\\yolov8\\code\\ultralytics\\runs\\detect\\train11\\weights\\best.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="0")
results = model.predict(source="C:\\mq\\yolov8\\dataset\\20231024\\20231024\\five jiaci", show=False, save = True, save_txt = True) # Display preds. Accepts all YOLO predict arguments
