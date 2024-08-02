numero = int(input("Digite o valor de n: "))

resultado = 1

while numero > 0:
  resultado *= numero
  numero -= 1

print(resultado)