# DC-comics-logo-classifier
An image classifier that classifies logo of DC characters.

Note: Tensorflow 2.0 version was used

Training was done with the help of Google Colab.
Current Accuracy of model is 80%. I will be working to improve it.

Total 1177 images were scraped and 80% were used for training while 20% for testing.

## Currently model consist of five classes namely
Batman,
Wonder Woman,
Green Lantern,
Superman,
Flash

# How to run ?
run classify.py file and pass path of image file
for eg:
  python classify.py bat.jpg
  
here only filename is mentioned because both are in same directory
i have provided some sample images as well
comic.h5 is our saved model

# convert png to jpg
This file helps to convert .png to .jpg
run file png2jpg.py 
make sure to change filename in script.
