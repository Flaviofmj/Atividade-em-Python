# Solicita o valor de cada produto
valor_produto = float(input("Digite o valor do produto: "))

# Solicita a quantidade de produtos comprados
quantidade_produto = float(input("Digite a quantidade comprada: "))

# Calcula o valor total da compra
valor_total = valor_produto * quantidade_produto

# Calcula 10% de desconto sobre o valor total
desconto = valor_total * 0.10

# Subtrai o desconto do valor total
valor_final = valor_total - desconto

# Exibe o valor total sem desconto, com duas casas decimais
print(f"Valor total da compra sem desconto: R$ {valor_total:.2f}")

# Exibe o valor final com 10% de desconto, com duas casas decimais
print(f"Valor a pagar com desconto de 10%: R$ {valor_final:.2f}")