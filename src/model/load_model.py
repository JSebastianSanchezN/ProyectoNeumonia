import tensorflow as tf
from tensorflow.keras import models  # type: ignore


def model():
    """
    Carga y retorna el modelo entrenado almacenado en 'conv_MLP_84.h5'.

    Returns
    -------
    tf.keras.Model
        Modelo cargado listo para usarse en predicciones.
    """
    model = tf.keras.models.load_model("conv_MLP_84.h5", compile=False)
    return model
