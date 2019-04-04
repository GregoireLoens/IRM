import os
import cv2
import numpy as np
from random import shuffle
from tqdm import tqdm


IMG_SIZE = 50
LR = 1e-3


def create_train_data(link):
    training_data = []
    label = []
    for elem in link:
        if elem.find("cat") > 0:
            label = np.array([1, 0])
        if elem.find("house") > 0:
            label = np.array([0, 1])

        for img in tqdm(os.listdir(elem)):
            path = os.path.join(elem, img)
            img_data = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
            training_data.append([np.array(img_data), label]),

    shuffle(training_data)
    return training_data


def create_test_data(link):
    testing_data = []
    i = 1
    for elem in link:
        for img in tqdm(os.listdir(elem)):
            path = os.path.join(elem, img)
            try:
                img_data = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
                testing_data.append([np.array(img_data), [i, 2]])
                i = i + 1
            except Exception:
                print("Error on image")
    shuffle(testing_data)
    return testing_data