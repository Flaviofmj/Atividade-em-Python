# Solicita o saldo atual da conta bancária
saldo_conta = float(input("Digite o saldo da conta: "))

# Declara o limite do cheque especial como 500 reais
limite_cheque_especial = 500

# Verifica se o saldo da conta é maior que o limite do cheque especial
print("O saldo da conta é maior que o limite do cheque especial:", saldo_conta > limite_cheque_especial)