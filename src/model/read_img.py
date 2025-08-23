"""
Este módulo contiene funciones para la lectura y procesamiento de imágenes
en formato DICOM y JPG. Ambas funciones retornan la imagen procesada en un 
array NumPy y en un objeto PIL para su visualización.
"""

import pydicom
import numpy as np
from PIL import ImageTk, Image
import cv2

def read_dicom_file(path):
    """Lee un archivo DICOM y retorna la imagen procesada en RGB y en formato PIL."""
    img = pydicom.dcmread(path)
    img_array = img.pixel_array
    img2show = Image.fromarray(img_array)
    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
    return img_RGB, img2show

def read_jpg_file(path):
    """Lee un archivo JPG y retorna la imagen procesada y en formato PIL."""
    img = cv2.imread(path)
    img_array = np.asarray(img)
    img2show = Image.fromarray(img_array) 
    img2 = img_array.astype(float) 
    img2 = (np.maximum(img2,0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    return img2, img2show   