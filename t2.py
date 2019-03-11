import concurrent.futures
import numpy as np

import keras.backend as K
from keras.layers import Dense
from keras.models import Sequential

import tensorflow as tf
from tensorflow.python.client import device_lib

def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']

xdata = np.random.randn(100, 8)
ytrue = np.random.randint(0, 2, 100)

def fit(gpu):
    with tf.Session(graph=tf.Graph()) as sess:
        K.set_session(sess)
        with tf.device(gpu):
            model = Sequential()
            model.add(Dense(12, input_dim=8, activation='relu'))
            model.add(Dense(8, activation='relu'))
            model.add(Dense(1, activation='sigmoid'))

            model.compile(loss='binary_crossentropy', optimizer='adam')
            model.fit(xdata, ytrue, verbose=0)

            return model.evaluate(xdata, ytrue, verbose=0)

gpus = get_available_gpus()
with concurrent.futures.ThreadPoolExecutor(len(gpus)) as executor:
    results = [x for x in executor.map(fit, gpus)]
print('results: ', results)