import os

raw = 'wonderwoman'
folderName = 'jpg_' + raw
raw_jpg = os.path.join(os.getcwd(),folderName)

for i, filename in enumerate(os.listdir(raw_jpg)):
    os.rename(os.path.join(raw_jpg,filename),os.path.join(raw_jpg,str(i+1) + ".jpg"))