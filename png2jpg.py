import os
import cv2

file = 'bat2.png' #filename
path = os.path.join(os.getcwd(),file)
img = cv2.imread(path)
cv2.imwrite(path[:-3] + 'jpg', img)