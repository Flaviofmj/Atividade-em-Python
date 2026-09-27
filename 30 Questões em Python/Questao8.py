# Solicita a quantidade de alunos da turma
# int() converte o valor digitado para número inteiro
numero_alunos = int(input("Digite a quantidade de aluno da turma: "))

# Solicita a média da turma
# float() permite receber números com casas decimais
media_turma = float(input("Digite a média da turma: "))

# Verifica se a média da turma é maior ou igual a 7
# Exibe True se a turma foi aprovada ou False caso contrário
print("Os alunos da turma foram aprovados:", media_turma >= 7)  