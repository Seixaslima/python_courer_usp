numero = input("Digite um número inteiro: ")
adjacente = False

for posicao in range(len(numero)-1):
  if numero[posicao] == numero[posicao+1]:
    adjacente = True
    break

if adjacente:
  print("sim")
else:
  print("não")