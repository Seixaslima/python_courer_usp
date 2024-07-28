def computador_escolhe_jogada(n, m):
  multplicador = n // (m+1)
  numeroRestante = multplicador * (m + 1)
  retirar = n - numeroRestante
  if retirar == 0:
    return m
  return retirar

def usuario_escolhe_jogada(n,m):
  valor = int(input("Quantas peças você vai tirar? "))
  teste = valor < 0 or valor > m or valor > n
  while teste:
    print("Oops! Jogada inválida! Tente de novo.")
    valor = int(input("Quantas peças você vai tirar? "))
    teste = valor < 0 or valor > m or valor > n
  return valor


def partida():
  n = int(input("Quantas peças? "))
  m = int(input("Limite de peças por jogada? "))
  vezDoComputador = True
  if (n % (m+1) == 0):
    print( "Você começa!")
    vezDoComputador = False
  else:
    print("Computador começa!")

  while n > 0:
    if vezDoComputador: 
      remover = computador_escolhe_jogada(n,m)
      n -= remover

    else:
      remover = usuario_escolhe_jogada(n,m)
      n -= remover
    
    if (remover > 1):
      if vezDoComputador:
        print(f"O computador tirou {remover} peças.")
      else:
        print(f"Você tirou {remover} peças.")
    else:
      if vezDoComputador:
        print(f"O computador tirou {remover} peça.")
      else:
        print(f"Você tirou {remover} peça.")
    
    if n == 0:
      if vezDoComputador:
        print("O computador ganhou!")
      else:
        print("Você ganhou!")
      return vezDoComputador
    elif n == 1:
      print("Agora resta apenas uma peça no tabuleiro.")
    else:
      print(f"Agora restam {n} peças no tabuleiro.")
    vezDoComputador = not vezDoComputador


  


def imprime_menu():
  print("1 - para jogar uma partida isolada")
  print("2 - para jogar um campeonato 2")
  print("")
    
def campeonato():
  pontosComputador = 0
  for i in range(3):
    if (partida()):
      pontosComputador += 1
  
  pontosUsuario = 3 - pontosComputador
  print(f"Placar: Você {pontosUsuario} X {pontosComputador} Computador")


def jogo():
  print("Bem-vindo ao jogo do NIM! Escolha: \n")
  imprime_menu()
  escolha = input()

  while not (escolha == "1" or escolha == "2"):
    print("escolha uma opção valida \n")
    imprime_menu()
    escolha = input()
  
  if escolha == "1":
    partida()
  elif escolha == "2":
    campeonato()

jogo()



