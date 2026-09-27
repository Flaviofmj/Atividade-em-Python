# Solicita a quantidade de produtos disponíveis no estoque
produto_estoque = int(input("Digite a quantidade de produtos em estoque: "))

# Define a quantidade mínima de produtos permitida no estoque
estoque_minimo = 35

# Verifica se o estoque está menor ou igual ao limite mínimo
print("O estoque é menor ou igual à quantidade mínima:", produto_estoque <= estoque_minimo)