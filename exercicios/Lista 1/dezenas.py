# Entrada de Dados:
# Digite um número inteiro: 78615
numero_str = input("Digite um número inteiro: ")
numero_int = int(numero_str)

numero_decimal = numero_int % 100
numero_dezena = numero_decimal // 10

# Saída de Dados:
# O dígito das dezenas é 1
print("O dígito das dezenas é", numero_dezena)