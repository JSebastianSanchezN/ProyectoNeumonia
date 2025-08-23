# 1. Importaciones estándar de Python
# (No hay en este caso)

# 2. Importaciones de bibliotecas de terceros
import tensorflow as tf
from tensorflow.keras import models  # type: ignore

# 3. Importaciones locales
# (No hay en este caso)

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
