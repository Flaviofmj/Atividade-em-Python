# Solicita a quantidade de horas trabalhadas na semana
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas na semana: "))

# Solicita o valor recebido por hora trabalhada
valor_hora = float(input("Digite o valor pago por hora: "))

# Calcula o salário semanal multiplicando as horas pelo valor da hora
salario_semanal = horas_trabalhadas * valor_hora

# Exibe o salário semanal calculado em reais
print("Seu salário semanal conforme as horas trabalhadas é de R$:", salario_semanal)