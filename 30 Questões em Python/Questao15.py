# Solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# Solicita a primeira nota e converte para número decimal
nota1 = float(input("Digite a primeira nota: "))

# Solicita a segunda nota e converte para número decimal
nota2 = float(input("Digite a segunda nota: "))

# Solicita a terceira nota e converte para número decimal
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Exibe o nome do aluno
print("Nome do aluno:", nome)

# Exibe a média com duas casas decimais
print(f"A média obtida pelo aluno: {media:.2f}")