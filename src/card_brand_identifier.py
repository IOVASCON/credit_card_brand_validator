def get_card_brand(card_number: str) -> str:
    """
    Identifica a bandeira do cartão com base em prefixos, tamanho e/ou regras específicas.
    Retorna o nome da bandeira ou 'Desconhecida'.
    """
    # Remove espaços e hífens do número do cartão
    num = card_number.replace(" ", "").replace("-", "")
    length = len(num)
    
    # VISA 16 Dígitos (verificação específica antes de "Visa" genérico)
    if num.startswith("4") and length == 16:
        return "Visa (16 dígitos)"
    
    # Visa genérico (para outros comprimentos, como 13 dígitos)
    if num.startswith("4"):
        return "Visa"
    
    # MasterCard (prefixos 51 a 55 ou 2221 a 2720)
    if (length >= 2 and num[:2] in ["51", "52", "53", "54", "55"]) or (length >= 4 and 2221 <= int(num[:4]) <= 2720):
        return "MasterCard"
    
    # American Express (prefixos 34 ou 37)
    if length >= 2 and num[:2] in ["34", "37"]:
        return "American Express"
    
    # Diners Club (prefixos 300-305, 309, 36, 38, 39)
    if length >= 2 and (num.startswith("36") or num.startswith("38") or num.startswith("39")):
        return "Diners Club"
    if length >= 3:
        prefix_3 = int(num[:3])
        if 300 <= prefix_3 <= 305 or num.startswith("309"):
            return "Diners Club"
    
    # Discover (prefixos 6011, 65 ou 644-649)
    if num.startswith("6011") or num.startswith("65"):
        return "Discover"
    if length >= 3:
        prefix_3 = int(num[:3])
        if 644 <= prefix_3 <= 649:
            return "Discover"
    
    # JCB (prefixo 35)
    if num.startswith("35"):
        return "JCB"
    
    # Hipercard (prefixo 6062)
    if num.startswith("6062"):
        return "Hipercard"
    
    # Aura (exemplo fictício: prefixo '50')
    if num.startswith("50"):
        return "Aura"
    
    # EnRoute (prefixos 2014 ou 2149)
    if length >= 4 and num[:4] in ["2014", "2149"]:
        return "EnRoute"
    
    # Voyage (exemplo fictício: prefixo 8699)
    if length >= 4 and num.startswith("8699"):
        return "Voyage"
    
    return "Desconhecida"
