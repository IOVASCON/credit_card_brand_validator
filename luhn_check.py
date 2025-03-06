def luhn_check(card_number: str) -> bool:
    """
    Retorna True se o 'card_number' passar no algoritmo de Luhn, False caso contrário.
    """
    # Remove espaços e hífens do número
    num = card_number.replace(" ", "").replace("-", "")
    
    total = 0
    reverse_digits = num[::-1]
    
    for i, digit in enumerate(reverse_digits):
        d = int(digit)
        # Dobra a cada segundo dígito (começando do índice 1)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    
    return (total % 10 == 0)
