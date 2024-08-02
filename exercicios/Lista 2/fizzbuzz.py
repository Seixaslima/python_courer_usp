numero = int(input("Digite o numero: "))

divisivel_por_3 = numero % 3 == 0
divisivel_por_5 = numero % 5 == 0

if(divisivel_por_3 & divisivel_por_5 ):
  print("FizzBuzz")
else:
  print(numero)