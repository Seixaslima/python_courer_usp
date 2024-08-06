import math

def é_hipotenusa(hipotenusa):
  quadrado = hipotenusa * hipotenusa
  for cat1 in range(1,hipotenusa):
    cat1Quadrado = cat1*cat1
    for cat2 in range(cat1,hipotenusa):
      cat2Quadrado = cat2*cat2
      soma = cat1Quadrado + cat2Quadrado
      if quadrado == soma:
        return True
  return False


def soma_hipotenusas(numero):
  soma = 0
  for hipotenusa in range(numero + 1):
    if é_hipotenusa(hipotenusa):
      soma += hipotenusa
  return soma

if __name__ == "__main__":
  print(é_hipotenusa(4))
  print(soma_hipotenusas(25))