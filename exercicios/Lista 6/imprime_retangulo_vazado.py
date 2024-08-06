largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

largura_loop = largura
while largura_loop > 0:
  print("#",end="")
  largura_loop -= 1
altura -= 1
print()

while altura > 1:
  largura_loop = largura -1
  print("#",end="")
  while largura_loop > 1:
    print(" ",end="")
    largura_loop -= 1
  print("#")
  altura -= 1

largura_loop = largura
while largura_loop > 0:
  print("#",end="")
  largura_loop -= 1