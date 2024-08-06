lista = []

numero = int(input("Digite um número: "))

while numero != 0:
  lista.append(numero)
  numero = int(input("Digite um número: "))

listaInvertida = lista[::-1]
print()
for num in listaInvertida:
  print(num)