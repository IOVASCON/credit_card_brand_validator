import pytest
from src.luhn_check import luhn_check

def test_luhn_valid():
    # Número de cartão válido (exemplo para teste)
    card = "4532015112830366"  # Este é um exemplo de número válido pelo algoritmo de Luhn
    assert luhn_check(card) is True

def test_luhn_invalid():
    # Alterando o último dígito para tornar inválido
    card = "4532015112830367"
    assert luhn_check(card) is False
