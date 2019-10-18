from flask import (Flask,request,jsonify)
from flask_cors import CORS,cross_origin
import urllib.request
import os
import time
import cv2
import sys
import numpy as np
import tensorflow as tf

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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


def classify(path):
    img_size = 128
    X = preProcess(path, img_size)
    y = model.predict(X)
    y = list(y[0])
    print(y)
    return y.index(max(y))

classes = ['batman', 'wonder woman', 'green lantern', 'superman', 'flash']

@app.route('/')
def main():
    image_url = request.args.get("image_url", "")
    if image_url == "" :
        return jsonify({
            'status': 400,
            'message': 'Bad Request'
        }), 400

    file_name = str(time.time())+".jpg"
    urllib.request.urlretrieve(image_url, file_name)

    result = classify(file_name)

    os.remove(file_name)

    return jsonify({
            'message': classes[result]
        })

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True) 
