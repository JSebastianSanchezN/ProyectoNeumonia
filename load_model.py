import tensorflow as tf
from tensorflow.keras import models # type: ignore

def model():
    model = tf.keras.models.load_model('conv_MLP_84.h5', compile=False)
    return model