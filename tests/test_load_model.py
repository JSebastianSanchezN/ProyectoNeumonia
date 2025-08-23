import pytest # type: ignore
from src.model import load_model

def test_load_model_returns_keras_model(monkeypatch):
    """
    Verifica que load_model.model() retorne un objeto tf.keras.Model.
    """

    class DummyModel:
        pass

    monkeypatch.setattr("tensorflow.keras.models.load_model", lambda *args, **kwargs: DummyModel())

    model = load_model.model()
    assert isinstance(model, DummyModel)
