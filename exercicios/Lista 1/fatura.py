# Entrada de Dados:
# Digite o nome do cliente: Fulano de Tal
# Digite o dia de vencimento: 9
# Digite o mês de vencimento: Janeiro
# Digite o valor da fatura: 350,00
cliente = input("Digite o nome do cliente: ")
dia = input("Digite o dia de vencimento: ")
mes = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")

# Saída de Dados:
# Olá, Fulano de Tal
print("Olá,", cliente)
# A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.
print(f"A sua fatura com vencimento em {dia} de {mes} no valor de R$ {valor} está fechada.")