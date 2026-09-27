# Solicita ao usuário o valor do salário atual
salario = float(input("Digite o valor do seu salário: "))

# Calcula o valor do aumento de 15% sobre o salário
aumento = salario * 0.15

# Soma o salário atual com o valor do aumento
reajustado = salario + aumento

# Exibe o novo salário com duas casas decimais
print(f"Seu novo salário com aumento de 15% é de: R$ {reajustado:.2f}")