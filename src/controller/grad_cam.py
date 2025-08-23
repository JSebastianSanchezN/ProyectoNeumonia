import cv2
import numpy as np
import tensorflow as tf

from ..model import preprocess_img
from ..model import load_model


def grad_cam(array):
    """
    Genera un mapa de activación Grad-CAM para resaltar las
    regiones de la imagen que contribuyen más a la predicción
    de la red neuronal.

    Parámetros
    ----------
    array : numpy.ndarray
        Imagen de entrada en formato de arreglo.

    Retorna
    -------
    numpy.ndarray
        Imagen de entrada con el mapa de calor superpuesto
        en formato RGB.
    """
    # Preprocesar la imagen antes de pasarla al modelo
    img = preprocess_img.preprocess(array)

    # Cargar el modelo entrenado
    model = load_model.model()

    # Crear un modelo que retorne la salida de la capa conv
    grad_model = tf.keras.models.Model(
        model.inputs,
        [model.get_layer("conv10_thisone").output, model.output]
    )

    # Calcular gradientes respecto a la predicción de interés
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model([img])
        if isinstance(preds, list):  # Asegurar formato tensor
            preds = preds[0]

        pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    # Gradientes de la clase respecto a la salida conv
    grads = tape.gradient(class_channel, last_conv_layer_output)

    # Promediar gradientes espaciales
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    # Multiplicar los canales de activación por sus gradientes
    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    # Normalizar entre 0 y 1
    heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-9)
    heatmap = heatmap.numpy()

    # Redimensionar y aplicar colormap
    heatmap = cv2.resize(heatmap, (512, 512))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)

    # Superponer el heatmap sobre la imagen original
    img2 = cv2.resize(array, (512, 512))
    hif = 0.8  # Factor de transparencia
    transparency = heatmap * hif
    transparency = transparency.astype(np.uint8)

    superimposed_img = cv2.add(transparency, img2)
    superimposed_img = superimposed_img.astype(np.uint8)

    return superimposed_img[:, :, ::-1]
