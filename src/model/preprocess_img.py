# 1. Importaciones estándar de Python
# (No hay en este caso)

# 2. Importaciones de bibliotecas de terceros
import cv2
import numpy as np

# 3. Importaciones locales
# (No hay en este caso)

"""
Este módulo contiene funciones para el preprocesamiento de imágenes.
Incluye redimensionamiento, conversión a escala de grises, CLAHE, 
normalización y ajuste de dimensiones para deep learning.
"""

def preprocess(array):
    """
    Preprocesa una imagen: redimensiona, convierte a escala de grises,
    aplica CLAHE, normaliza y expande dimensiones.
    """
    array = cv2.resize(array , (512 , 512))
    array = cv2.cvtColor(array, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4,4))
    array = clahe.apply(array)
    array = array/255
    array = np.expand_dims(array,axis=-1)
    array = np.expand_dims(array,axis=0)
    return array