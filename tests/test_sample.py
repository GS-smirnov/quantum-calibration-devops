# tests/test_sample.py

import numpy as np
import pytest

def test_dummy():
    # Простой тест: проверка равенства массивов
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    assert np.array_equal(a, b)

# Пример теста для проверки одной из функций  калибровочного кода.
# в проекте присутствует функция create_and_train_model, можно написать:
#
from src.your_module import create_and_train_model

def test_create_and_train_model_returns_model_and_history():
    # Создание небольшого набора данных для тестирования
    X_dummy = np.random.rand(10, 3)
    Y_dummy = np.random.rand(10, 1)
    # Разделение на обучающую и тестовую выборки (для теста можно использовать те же данные)
    model, history = create_and_train_model(X_dummy, Y_dummy, X_dummy, Y_dummy, output_index=0)
    # Проверка, что возвращается объект модели и история обучения не пустая
    assert model is not None
    assert history.history['loss'], "История обучения должна содержать значение ошибки"
