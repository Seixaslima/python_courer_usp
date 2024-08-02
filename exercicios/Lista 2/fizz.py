numero = int(input("Digite o numero: "))

divisivel_por_3 = numero % 3 == 0

if(divisivel_por_3):
  print("Fizz")
else:
  print(numero)