import cv2
import numpy as np
import os
from random import shuffle
from tqdm import tqdm
import matplotlib.pyplot as plt
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression


IMG_SIZE = 50
LR = 1e-3
MODEL_NAME = 'Cat&House'
###############################################################


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
################################################################


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

##################################################################


t_data = create_train_data(["../black cat snow", "../red cat snow", "../black graffiti house", "../white graffiti house", "../Other house", "../brown cat snow"])

data = create_test_data(["../test"])


X_train = np.array([i[0] for i in t_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y_train = [i[1] for i in t_data]

X_test = np.array([i[0] for i in data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y_test = np.array([i[1] for i in data])
print(y_test.shape)

# Model ########################################################

convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name='input')
convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)
convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)
convnet = conv_2d(convnet, 128, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)
convnet = conv_2d(convnet, 64, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)
convnet = conv_2d(convnet, 32, 5, activation='relu')
convnet = max_pool_2d(convnet, 5)
convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)
convnet = fully_connected(convnet, 2, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')
model = tflearn.DNN(convnet, tensorboard_dir='log', tensorboard_verbose=0)
model.fit({'input': X_train}, {'targets': y_train}, n_epoch=10,
          validation_set=({'input': X_test}, {'targets': y_test}),
          snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

# Plot Result ########################################################

fig = plt.figure(figsize=(16, 12))
for num, data in enumerate(data[:16]):

    img_num = data[1]
    img_data = data[0]

    y = fig.add_subplot(4, 4, num + 1)
    orig = img_data
    data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
    model_out = model.predict([data])[0]

    if np.argmax(model_out) == 1:
        str_label = 'House'
    else:
        str_label = 'Cat'

    y.imshow(orig, cmap='gray')
    plt.title(str_label)
    y.axes.get_xaxis().set_visible(False)
    y.axes.get_yaxis().set_visible(False)
plt.show()

########################################################################
