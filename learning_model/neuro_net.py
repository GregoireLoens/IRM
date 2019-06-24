import numpy as np
from learning_model.data_classification import create_test_data, create_train_data
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import matplotlib.pyplot as plt


IMG_SIZE = 50
LR = 1e-3
MODEL_NAME = 'P&P'


def exec_model(train, val):
    training_data = create_train_data(train)

    validation_data = create_test_data(val)

    data = create_test_data("./example")

    X_train = np.array([i[0] for i in training_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    y_train = [i[1] for i in training_data]

    X_val = np.array([i[0] for i in validation_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    y_val = np.array([i[1] for i in validation_data])

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
          validation_set=({'input': X_val}, {'targets': y_val}),
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
            str_label = 'Picture'
        else:
            str_label = 'Paint'

        y.imshow(orig, cmap='gray')
        plt.title(str_label)
        y.axes.get_xaxis().set_visible(False)
        y.axes.get_yaxis().set_visible(False)
    plt.show()

    return model


