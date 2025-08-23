import pytest  # type: ignore
import numpy as np
from src.model import preprocess_img

def test_preprocess_output_shape():
    """
    Verifica que la función preprocess() transforme correctamente
    una imagen de entrada al tamaño y formato esperado para el modelo.

    Caso de prueba:
    - Se genera una imagen aleatoria de tamaño (256, 256, 3).
    - Después del preprocesamiento, se espera que la salida sea
      un tensor con dimensiones (1, 512, 512, 1).
    """
    # Crear imagen dummy con valores entre 0 y 255
    dummy_img = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)

    # Aplicar preprocesamiento
    result = preprocess_img.preprocess(dummy_img)

    # Comprobar que la salida tenga el shape correcto
    assert result.shape == (1, 512, 512, 1)


def test_preprocess_output_range():
    """
    Verifica que los valores de la imagen procesada estén
    correctamente normalizados en el rango [0.0, 1.0].

    Caso de prueba:
    - Se genera una imagen aleatoria de tamaño (128, 128, 3).
    - Después del preprocesamiento, todos los valores deben ser
      mayores o iguales a 0.0 y menores o iguales a 1.0.
    """
    # Crear imagen dummy con valores entre 0 y 255
    dummy_img = np.random.randint(0, 255, (128, 128, 3), dtype=np.uint8)

    # Aplicar preprocesamiento
    result = preprocess_img.preprocess(dummy_img)

    # Comprobar que todos los valores estén dentro del rango válido
    assert result.min() >= 0.0
    assert result.max() <= 1.0
