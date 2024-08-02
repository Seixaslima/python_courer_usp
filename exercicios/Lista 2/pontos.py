import math
p1x = float(input("Cordenada x do primeiro ponto: "))
p1y = float(input("Cordenada y do primeiro ponto: "))

p2x = float(input("Cordenada x do segundo ponto: "))
p2y = float(input("Cordenada y do segundo ponto: "))

parcela_x = (p1x - p2x) ** 2
parcela_y = (p1y - p2y) ** 2

distancia = math.sqrt(parcela_x + parcela_y)

if distancia >= 10:
  print("longe")
else:
  print("perto")

