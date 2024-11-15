# Crie um programa que leia dois números do usuário e exiba a soma, subtração, multiplicação e divisão desses números.

# Inicializa e rebe 2 valores quaisquer pelo terminal
num_1 = float(input("Insira um primeiro valor: "))
num_2 = float(input("Insira um segundo valor: "))

# Realiza as 4 operações básicas e salva em variáveis
soma = num_1 + num_2
sub = num_1 - num_2
mult = num_1 * num_2
div = num_1 / num_2

# Exibe resultados em terminal
print(f'Soma: {soma} \nSubtração: {sub} \nMultiplicação: {mult} \nDivisão: {div}')