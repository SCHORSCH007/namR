from PIL import Image
from PIL.ExifTags import TAGS
import rawpy
import os

def jpeg_raw_strategy(file_path: str, wrapper:str=None, description:str=""):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension in ['.jpg', '.jpeg']:
        date_time = get_jpeg_datetime(file_path)
    elif file_extension in ['.cr2', '.nef', '.arw', '.dng']:
        date_time = get_raw_datetime(file_path)
    else:
        raise ValueError("Unsupported file format. Use JPEG or common RAW formats (CR2, NEF, ARW, DNG).")
    
    if date_time:
        if description:
            return f"{date_time}_{description.replace(" ","_")}"
        else:
            return f"{date_time}"
    else: 
        return None
    

def get_jpeg_datetime(file_path):
    image = Image.open(file_path)
    exif_data = image._getexif()

    if exif_data is None:
        return None

    for tag, value in exif_data.items():
        decoded_tag = TAGS.get(tag, tag)
        if decoded_tag == 'DateTimeOriginal':
            return value

    return None

def get_raw_datetime(file_path):
    with rawpy.imread(file_path) as raw:
        metadata = raw.metadata

        if metadata.datetime is not None:
            return metadata.datetime

    return None
