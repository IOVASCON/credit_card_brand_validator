from card_brand_identifier import get_card_brand
from luhn_check import luhn_check

def main():
    card_number = input("Digite o número do cartão de crédito: ")
    
    # Identifica a bandeira
    brand = get_card_brand(card_number)
    print(f"Bandeira identificada: {brand}")
    
    # Validação com o Algoritmo de Luhn (opcional)
    if luhn_check(card_number):
        print("O cartão passou na verificação de Luhn (válido).")
    else:
        print("O cartão NÃO passou na verificação de Luhn (inválido).")

if __name__ == '__main__':
    main()
