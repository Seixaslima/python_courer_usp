largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while altura > 0:
  largura_loop = largura
  while largura_loop > 0:
    print("#",end="")
    largura_loop -= 1
  print("")
  altura -= 1