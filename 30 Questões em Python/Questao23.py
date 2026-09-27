# Solicita a nota do aluno e converte para número decimal
nota_aluno = float(input("Digite a nota do aluno: "))

# Declara a média mínima necessária para aprovação
media_minima = 6.0

# Verifica se a nota do aluno é maior ou igual à média mínima
print("A nota do aluno está de acordo com a média mínima exigida:", nota_aluno >= media_minima)