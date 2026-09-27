# Solicita ao usuário a quantidade total de segundos
segundos = float(input("Digite a quantidade de segundos: "))

# Converte os segundos em horas completas
horas = segundos // 3600

# Calcula os minutos restantes após retirar as horas completas
minutos = (segundos % 3600) // 60

# Calcula os segundos que sobraram após retirar os minutos completos
segundo = segundos % 60

# Exibe o resultado da conversão em horas, minutos e segundos
print(horas, "Horas,", minutos, "minutos e", segundo, "segundos")