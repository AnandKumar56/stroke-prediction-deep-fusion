from django.db import models
#from keras.models import load_model
#import cv2
import numpy as np
import pickle
#from tensorflow.keras.preprocessing import image
#import tensorflow as tf
import json
from PIL import Image
import joblib
import numpy as np


cnn = pickle.load(open('./cnn.pkl', 'rb'))
lstm = pickle.load(open('./lstm.pkl', 'rb'))
cnn_lstm = pickle.load(open('./cnn_lstm.pkl', 'rb'))

def predict(lst, algo):
    test = np.array(lst)
    if algo == 'lstm':
        test = np.reshape(test, (1, 1, -1))  # (batch, timesteps, features)
        y_pred = lstm.predict(test)
        return y_pred
    else:
        test = np.reshape(test, (1, -1))  # (batch, features)
        if algo == 'cnn':
            y_pred = cnn.predict(test)
            return y_pred
        else:
            y_pred = cnn_lstm.predict(test)
            return y_pred