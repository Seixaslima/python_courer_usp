import math

a_str = input("a ")
b_str = input("b ")
c_str = input("c ")

a = float(a_str)
b = float(b_str)
c = float(c_str)

delta = b**2 - (4*a*c)

if delta < 0:
  print("esta equação não possui raízes reais")
elif delta == 0:
  x1 = (-b)/(2*a)
  print("a raiz dupla desta equação é", x1)
else: 
  x1 = ((-b) + math.sqrt(delta)) / ((2*a))
  x2 = ((-b) - math.sqrt(delta)) / ((2*a))
  if (x1 > x2):
    print("as raízes da equação são", x2 , "e" , x1)
  else:
    print("as raízes da equação são", x1 , "e" , x2)
  