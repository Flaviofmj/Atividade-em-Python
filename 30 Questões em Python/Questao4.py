# Solicita ao usuário que digite um valor em reais
# float() permite receber valores com casas decimais
valor_real = float(input("Digite um valor em reais: "))

# Declara uma variável com a taxa de conversão do dólar
taxa_conversao = 5.50

# Converte o valor de reais para dólares
# Divide o valor em reais pela taxa de conversão
dolar = valor_real / taxa_conversao

# Exibe o resultado com apenas duas casas decimais
# O f-string permite formatar o valor usando :.2f
print(f"Seu valor em dólar é de: US$ {dolar:.2f}")