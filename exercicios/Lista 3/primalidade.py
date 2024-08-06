numero = int(input("Digite um número inteiro: "))

is_primo = True
raiz = int (numero **0.5)

if numero > 1:
  for teste in range(2,raiz +1):
    if numero % teste == 0:
      is_primo = False
      break

if is_primo:
  print("primo")
else:
  print("não primo")