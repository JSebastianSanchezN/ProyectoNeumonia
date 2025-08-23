import pytest  # type: ignore
import numpy as np
import sys, types


sys.modules["tkcap"] = types.ModuleType("tkcap")
sys.modules["tkinter.tix"] = types.ModuleType("tkinter.tix")
sys.modules["pyautogui"] = types.ModuleType("pyautogui")
sys.modules["mouseinfo"] = types.ModuleType("mouseinfo")

from src.view import detector_neumonia


class DummyIntegrator:
    @staticmethod
    def predict(array):
        return "Neumonía", 87.5, np.zeros((250, 250, 3), dtype=np.uint8)


class DummyText:
    """Mock de los widgets Tkinter (Text)."""
    def image_create(self, *args, **kwargs):
        return None
    def insert(self, *args, **kwargs):
        return None


def test_run_model(monkeypatch):
    """
    Verifica que run_model llame a integrator.predict y genere resultados
    sin depender de una interfaz gráfica real.
    """

    def dummy_init(self):
        self.array = np.zeros((128, 128, 3), dtype=np.uint8)
        self.text_img2 = DummyText()
        self.text2 = DummyText()
        self.text3 = DummyText()

    monkeypatch.setattr(detector_neumonia.App, "__init__", dummy_init)
    monkeypatch.setattr(detector_neumonia, "integrator", DummyIntegrator)
    monkeypatch.setattr(detector_neumonia.ImageTk, "PhotoImage", lambda x: x)

    app = detector_neumonia.App()
    app.run_model()

    assert app.label == "Neumonía"
    assert isinstance(app.proba, float)
    assert app.proba == 87.5
    assert isinstance(app.heatmap, np.ndarray)
