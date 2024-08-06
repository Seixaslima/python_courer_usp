import math

def ehPrimo(numero):
  limite = int(math.sqrt(numero)) + 1
  for i in range(2,limite):
    if numero % i == 0:
      return False
  return True

def n_primos(numero):
  numero_primos = 0
  for i in range(2,numero+1):
    if ehPrimo(i):
      numero_primos += 1
  return numero_primos

if __name__ == "__main__":
  print(n_primos(3))
  print(n_primos(5))