import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import pandas as pd

# 提高Pillow处理图片的最大像素限制
Image.MAX_IMAGE_PIXELS = None  # None表示没有限制

def get_exif_data(image):
    """提取图片的EXIF数据"""
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data

def get_lat_lon(exif_data):
    """从EXIF数据中提取经纬度信息"""
    if 'GPSInfo' in exif_data:
        gps_info = exif_data['GPSInfo']
        gps_latitude = gps_info.get('GPSLatitude')
        gps_latitude_ref = gps_info.get('GPSLatitudeRef')
        gps_longitude = gps_info.get('GPSLongitude')
        gps_longitude_ref = gps_info.get('GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = convert_to_degrees(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat

            lon = convert_to_degrees(gps_longitude)
            if gps_longitude_ref != "E":
                lon =  lon

            return lat, lon
    return None, None

def convert_to_degrees(value):
    """将GPS坐标转换为度"""
    d, m, s = value
    return d + (m / 60.0) + (s / 3600.0)

def extract_info_from_images(folder_path):
    """提取文件夹中所有图片的名字和经纬度信息"""
    data = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # 去除文件名中的.jpg扩展名
            base_filename = os.path.splitext(filename)[0]
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)
            exif_data = get_exif_data(image)
            lat, lon = get_lat_lon(exif_data)
            data.append([base_filename, lat, lon])  # 使用没有扩展名的文件名
    return data

# 修改为你的图片文件夹路径
folder_path = 'C:\\Users\\Apexmo\\OneDrive\\Desktop\\photo'
data = extract_info_from_images(folder_path)

# 将数据保存到Excel文件
df = pd.DataFrame(data, columns=['照片名', '纬度', '经度'])
excel_path = os.path.join(folder_path, 'results.xlsx')
df.to_excel(excel_path, index=False)

print(f'Excel文件已保存到 {excel_path}')
