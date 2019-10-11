import os
import cv2
import sys
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('comic.h5')


def preProcess(path, img_size):
    images = []
    cv_img = cv2.imread(path)
    cv_img = cv2.resize(cv_img, (img_size, img_size))
    cv_img = cv_img.astype(np.float64)
    images.append(cv_img)
    images = np.array(images)
    images = images / 255.0
    X = images
    print("Shape : ", X.shape)
    return X


def classify():
    path = os.path.join(os.getcwd(), sys.argv[1])
    img_size = 128
    X = preProcess(path, img_size)
    y = model.predict(X)
    y = list(y[0])
    print(y)
    return y.index(max(y))


print("Result")
result = classify()
classes = ['batman', 'wonder woman', 'green lantern', 'superman', 'flash']

print("-*-*-*-*-*-*-*-*-")
print()
print("predicted class : ",classes[result])
print()
print("-*-*-*-*-*-*-*-*-")