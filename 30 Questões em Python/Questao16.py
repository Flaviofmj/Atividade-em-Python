# Solicita a temperatura em graus Celsius
# float() permite receber valores com casas decimais
temperatura = float(input("Digite a temperatura em graus Celsius: "))

# Converte a temperatura de Celsius para Fahrenheit
# Fórmula: Fahrenheit = (Celsius × 9 / 5) + 32
fahrenheit = (temperatura * 9 / 5) + 32

# Exibe o resultado da conversão
print("Resultado da temperatura convertida para Fahrenheit:", fahrenheit)