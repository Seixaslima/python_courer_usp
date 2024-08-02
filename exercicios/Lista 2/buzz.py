numero = int(input("Digite o numero: "))

divisivel_por_5 = numero % 5 == 0

if(divisivel_por_5):
  print("Buzz")
else:
  print(numero)