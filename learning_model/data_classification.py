import os
import cv2
import numpy as np
from random import shuffle
from tqdm import tqdm


IMG_SIZE = 50
LR = 1e-3


def create_train_data(lt):
    training_data = []
    label = []

    try:
        for elem in lt:
            if elem[0].find("painting") > 0:
                label = np.array([1, 0])
            if elem[0].find("picture") > 0:
                label = np.array([0, 1])
            img_data = cv2.imread(elem[0], cv2.IMREAD_GRAYSCALE)
            img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
            training_data.append([np.array(img_data), label]),
    except Exception:
        print("Error on image")

    shuffle(training_data)
    return training_data


def create_test_data(lt):
    testing_data = []
    i = 1
    for elem in lt:
        try:
            img_data = cv2.imread(elem[0], cv2.IMREAD_GRAYSCALE)
            img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
            testing_data.append([np.array(img_data), [i, 2]])
            i = i + 1
        except Exception:
            print("Error on image")
    shuffle(testing_data)
    return testing_data