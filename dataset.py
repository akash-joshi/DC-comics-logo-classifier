#latest
import cv2
import os
from sklearn.utils import shuffle
import numpy as np


def loadTrain(trainPath, classes, imageSize):
    images = []
    cls = []
    labels = []
    imageNames = []

    print("Reading Training Data")
    print("Path : ", trainPath)
    print("classes : ", classes)
    print("Image Size : ", imageSize)

    for field in classes:

        index = classes.index(field)
        print("Index : ", index, " Class : ", classes[index])
        # index will act as label
        # now build path to particular class
        path = os.path.join(trainPath, field)
        # now list all images in this folder
        print("For class and path --> ", path)
        for image in os.listdir(path):
            cv_img = cv2.imread(os.path.join(path, image))
            # resize
            cv_img = cv2.resize(cv_img, (imageSize, imageSize))
            cv_img = cv_img.astype(np.float64)
            # normalize
            cv_img = np.multiply(cv_img, 1.0 / 255.0)
            images.append(cv_img)  # add to image list
            # add label to image
            label = index#np.zeros(len(classes))
            #label[index] = 1.0  # one hot vector encoding
            labels.append(label)  # label added to list
            imbase = os.path.basename(image)  # base folder
            imageNames.append(imbase)
            cls.append(field)
    # make all list numpy arrays
    images = np.array(images)
    labels = np.array(labels)
    imageNames = np.array(imageNames)
    cls = np.array(cls)

    return images, labels, imageNames, cls


class DataSet(object):

    def __init__(self, images, labels, imageNames, cls):
        self._num_examples = images.shape[0]

        self._images = images
        self._labels = labels
        self._imageNames = imageNames
        self._cls = cls
        self._epochs_done = 0
        self._index_in_epoch = 0

    @property
    def images(self):
        return self._images

    @property
    def labels(self):
        return self._labels

    @property
    def img_names(self):
        return self._imageNames

    @property
    def cls(self):
        return self._cls

    @property
    def num_examples(self):
        return self._num_examples

    @property
    def epochs_done(self):
        return self._epochs_done

    def getData(self):
        return self._images, self._labels, self._imageNames, self._cls

    def next_batch(self, batch_size):
        """Return the next `batch_size` examples from this data set."""
        start = self._index_in_epoch
        self._index_in_epoch += batch_size

        if self._index_in_epoch > self._num_examples:
            # After each epoch we update this
            self._epochs_done += 1
            start = 0
            self._index_in_epoch = batch_size
            assert batch_size <= self._num_examples
        end = self._index_in_epoch

        return self._images[start:end], self._labels[start:end], self._imageNames[start:end], self._cls[start:end]


def readData(trainPath, classes, imageSize, validationSize):
    class DataSets(object):
        pass

    data_sets = DataSets()

    images, labels, imageNames, cls = loadTrain(trainPath, classes, imageSize)
    images, labels, imageNames, cls = shuffle(images, labels, imageNames, cls)
    if isinstance(validationSize, float):
        validationSize = int(validationSize * images.shape[0])

    validationImages = images[:validationSize]
    validationLabels = labels[:validationSize]
    validationImageNames = imageNames[:validationSize]
    validationCls = cls[:validationSize]

    trainImages = images[validationSize:]
    trainLabels = labels[validationSize:]
    trainImgNames = imageNames[validationSize:]
    trainCls = cls[validationSize:]

    data_sets.train = DataSet(trainImages, trainLabels, trainImgNames, trainCls)
    data_sets.valid = DataSet(validationImages, validationLabels, validationImageNames, validationCls)

    return data_sets
