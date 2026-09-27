# Solicita ao usuário uma quantidade de tempo em segundos
# float() permite receber valores com casas decimais
tempo_segundos = float(input("Digite uma quantidade de tempo em segundos: "))

# Declara uma constante com a velocidade da luz em km/s
velocidade_luz = 300000

# Calcula a distância percorrida pela luz
# Fórmula: distância = velocidade x tempo
distancia = tempo_segundos * velocidade_luz

# Exibe a distância calculada com duas casas decimais
print(f"A distancia percorrida pela luz nesse tempo foi de: {distancia:.2f}")