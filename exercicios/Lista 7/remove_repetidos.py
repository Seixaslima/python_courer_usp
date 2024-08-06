def remove_repetidos(lista):
  listaSemRepetida = []
  for elemento in lista:
    if not (elemento in listaSemRepetida):
      listaSemRepetida.append(elemento)
  listaSemRepetida.sort()
  return listaSemRepetida


if __name__ == "__main__":
  lista = [2, 4, 2, 2, 3, 3, 1]
  print(remove_repetidos(lista))
  print(remove_repetidos([1, 2, 3, 3, 3, 4]))