import pytest
from src.card_brand_identifier import get_card_brand

def test_visa_16():
    # Visa com 16 dígitos deve ser identificado como "Visa (16 dígitos)"
    card = "4123456789012345"
    assert get_card_brand(card) == "Visa (16 dígitos)"

def test_visa_generic():
    # Exemplo com 13 dígitos para Visa (não se enquadra como 16 dígitos)
    card = "4123456789012"
    assert get_card_brand(card) == "Visa"

def test_mastercard():
    card = "5123456789012345"  # Prefixo 51
    assert get_card_brand(card) == "MasterCard"

def test_american_express():
    card = "341234567890123"  # Prefixo 34
    assert get_card_brand(card) == "American Express"

def test_diners_club():
    card = "36123456789012"  # Prefixo 36
    assert get_card_brand(card) == "Diners Club"

def test_discover():
    card = "6011123456789012"  # Prefixo 6011
    assert get_card_brand(card) == "Discover"

def test_jcb():
    card = "3528123456789012"  # Prefixo 35
    assert get_card_brand(card) == "JCB"

def test_hipercard():
    card = "6062123456789012"  # Prefixo 6062
    assert get_card_brand(card) == "Hipercard"

def test_aura():
    card = "5012345678901234"  # Prefixo 50 (exemplo fictício)
    assert get_card_brand(card) == "Aura"

def test_enroute():
    card = "2014123456789012"  # Prefixo 2014
    assert get_card_brand(card) == "EnRoute"

def test_voyage():
    card = "8699123456789012"  # Prefixo 8699
    assert get_card_brand(card) == "Voyage"

def test_unknown():
    card = "1234567890123456"
    assert get_card_brand(card) == "Desconhecida"
