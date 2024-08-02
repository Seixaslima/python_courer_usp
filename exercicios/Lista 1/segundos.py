# quantidade de segundos em cada tempo
MIN_SEG = 60
HORA_SEG = 60*MIN_SEG
DIA_SEG = 24*HORA_SEG

# Entrada de Dados:
# Por favor, entre com o número de segundos que deseja converter: 178615
segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos_int = int(segundos_str)

#Calculando o numero de dias
dias = segundos_int // DIA_SEG
segundos_restantes = segundos_int % DIA_SEG

#calculando o numeor de horas
horas = segundos_restantes // HORA_SEG
segundos_restantes = segundos_restantes % HORA_SEG

#calculando o numero de minutos e segundos
minutos = segundos_restantes // MIN_SEG
segundos = segundos_restantes % MIN_SEG

# Saída de Dados:
# 2 dias, 1 horas, 36 minutos e 55 segundos.
print(dias,"dias,",horas, "horas,", minutos, "minutos e", segundos, "segundos." )