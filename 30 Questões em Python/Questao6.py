# Declara três variáveis com valores inteiros
a = 10
b = 20
c = 30

# Exibe os valores antes da troca
print("Valores antes da troca:", a, b, c)

# Guarda o valor de a na variável auxiliar
auxiliar = a

# Atribui o valor de b para a
a = b

# Atribui o valor antigo de a para b
b = auxiliar

# Exibe os valores depois da troca
print("Valores depois da troca:", a, b, c)