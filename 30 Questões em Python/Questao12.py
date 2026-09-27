# Solicita o primeiro número e converte o valor digitado para inteiro
numero1 = int(input("Digite um número: "))

# Solicita o segundo número e converte o valor digitado para inteiro
numero2 = int(input("Digite outro número: "))

# Calcula o resto da divisão do primeiro número pelo segundo
resto = numero1 % numero2

# Verifica se o resto da divisão é igual a zero
# Se for zero, significa que o primeiro número é divisível pelo segundo
divisivel = numero1 % numero2 == 0

# Exibe o resto da divisão
print("O resto da divisão é:", resto)

# Exibe se o primeiro número é divisível pelo segundo
print("O primeiro número é divisível pelo segundo:", divisivel)