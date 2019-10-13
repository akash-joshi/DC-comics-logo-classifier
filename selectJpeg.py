print("Selecting jpg")
import os
import shutil

raw = 'wonderwoman' # folder one
raw_jpeg = 'jpg_' + raw # folder two

current_dir = os.getcwd()
os.mkdir(os.path.join(current_dir,raw_jpeg))
image_path = os.path.join(current_dir,raw)

for file in os.listdir(os.path.join(current_dir,raw)):
    if file.endswith(".jpg"):
        print(file)
        shutil.copy(os.path.join(image_path,file),os.path.join(current_dir,raw_jpeg))

