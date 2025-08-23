import numpy as np
import tensorflow as tf

from ..controller import grad_cam
from ..model import preprocess_img
from ..model import load_model


def predict(array):
    """
    Realiza la predicción de una imagen dada utilizando un modelo CNN.

    Pasos:
    1. Preprocesa la imagen de entrada para ajustarla al formato del modelo.
    2. Carga el modelo y obtiene la predicción de la clase y la probabilidad.
    3. Genera un mapa Grad-CAM para visualizar las regiones importantes.

    Parámetros
    ----------
    array : np.ndarray
        Imagen de entrada en formato de arreglo NumPy.

    Retorna
    -------
    tuple
        label : str
            Etiqueta de la clase predicha.
        proba : float
            Probabilidad de la predicción (en porcentaje).
        heatmap : np.ndarray
            Imagen con el mapa de calor Grad-CAM superpuesto.
    """
    # 1. Preprocesar imagen: devuelve batch en el formato correcto
    batch_array_img = preprocess_img.preprocess(array)

    # 2. Cargar modelo y predecir clase y probabilidad
    model = load_model.model()
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100

    label = ""
    if prediction == 0:
        label = "bacteriana"
    if prediction == 1:
        label = "normal"
    if prediction == 2:
        label = "viral"

    # 3. Generar Grad-CAM: imagen con mapa de calor superpuesto
    heatmap = grad_cam.grad_cam(array)

    return (label, proba, heatmap)
