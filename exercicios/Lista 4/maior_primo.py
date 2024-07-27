import math

def ehPrimo(num):
    if num < 2:
        return False
    raiz = int(math.sqrt(num))
    for i in range(2, raiz + 1):
        if num % i == 0:
            return False
    return True

def maior_primo(num):
  for i in range(num, 2, -1):
    if ehPrimo(i):
      return i