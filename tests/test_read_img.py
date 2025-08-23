import pytest # type: ignore
import numpy as np
from src.model import read_img
from PIL import Image
import cv2
import os

def test_read_jpg_file(tmp_path):
    """
    Verifica que read_jpg_file procese un JPG y retorne (np.ndarray, PIL.Image).
    """
    dummy_img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    jpg_path = tmp_path / "dummy.jpg"
    cv2.imwrite(str(jpg_path), dummy_img)

    img_array, img_pil = read_img.read_jpg_file(str(jpg_path))

    assert isinstance(img_array, np.ndarray)
    assert img_array.shape[0] == 100 and img_array.shape[1] == 100
    assert isinstance(img_pil, Image.Image)


def test_read_dicom_file(monkeypatch):
    """
    Verifica que read_dicom_file use pydicom.dcmread y retorne (np.ndarray, PIL.Image).
    Usamos monkeypatch para simular un archivo DICOM.
    """

    class DummyDicom:
        def __init__(self):
            self.pixel_array = np.random.randint(0, 255, (128, 128), dtype=np.uint16)

    monkeypatch.setattr("pydicom.dcmread", lambda path: DummyDicom())

    img_array, img_pil = read_img.read_dicom_file("fake_path.dcm")

    assert isinstance(img_array, np.ndarray)
    assert img_array.shape == (128, 128, 3)  
    assert isinstance(img_pil, Image.Image)
