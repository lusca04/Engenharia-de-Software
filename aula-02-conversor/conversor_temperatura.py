# RF01: O sistema deve converter temperaturas de Celsius para Fahrenheit
# RF02: O sistema deve converter temperaturas de Fahrenheit para Celsius
# RF03: O sistema deve exibir o resultado formatado com unidades visíveis (°C / °F)
                                                                         
# RNF01 (Usabilidade): A interface deve ser intuitiva, com seleção clara da direção de conversão e resultado imediato
# RNF02 (Confiabilidade): O sistema deve validar entradas, aceitando apenas valores numéricos e exibindo mensagem de erro amigável em caso inválido

# ====================================
# CONVERSOR DE TEMPERATURA
# Exercício - Engenharia de Software
# ====================================

def celsius_para_fahrenheit(celsius):
    """
    RF01: Converter Celsius para Fahrenheit
    Fórmula: F = (C × 9/5) + 32
    """
    return (celsius * 9 / 5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """
    RF02: Converter Fahrenheit para Celsius
    Fórmula: C = (F - 32) × 5/9
    """
    return (fahrenheit - 32) * 5 / 9

def celsius_para_kelvin(celsius):
    """BÔNUS: Converter Celsius para Kelvin"""
    return celsius + 273.15

def entrada_numerica(prompt):
    """
    RNF01: Validação de entrada — só aceita números
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite apenas um número (ex: 25 ou 98.6).\n")

# ====================================
# PROGRAMA PRINCIPAL
# ====================================
while True:
    print("=" * 40)
    print("  CONVERSOR DE TEMPERATURA")
    print("=" * 40)
    print("Escolha a conversão:")
    print("  1 - Celsius → Fahrenheit")
    print("  2 - Fahrenheit → Celsius")
    print("  0 - Sair")
    print("=" * 40)

    opcao = input("Opção: ").strip()

    if opcao == "0":
        print("Encerrando. Boas receitas! 👨‍🍳")
        break

    elif opcao == "1":
        temp = entrada_numerica("Digite a temperatura em Celsius: ")
        resultado = celsius_para_fahrenheit(temp)
        kelvin = celsius_para_kelvin(temp)
        print("=" * 40)
        print(f"  {temp}°C = {resultado:.1f}°F")
        print(f"  (também: {kelvin:.2f} K)")  # BÔNUS

    elif opcao == "2":
        temp = entrada_numerica("Digite a temperatura em Fahrenheit: ")
        resultado = fahrenheit_para_celsius(temp)
        kelvin = celsius_para_kelvin(resultado)
        print("=" * 40)
        print(f"  {temp}°F = {resultado:.1f}°C")
        print(f"  (também: {kelvin:.2f} K)")  # BÔNUS

    else:
        print("Opção inválida. Escolha 1, 2 ou 0.")

    print("=" * 40)
    input("\nPressione Enter para continuar...")
    print()