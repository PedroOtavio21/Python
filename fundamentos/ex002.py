# Crie um programa que leia dois números do usuário e exiba a soma, subtração, multiplicação e divisão desses números.

num_1 = float(input("Insira um primeiro valor: "))
num_2 = float(input("Insira um segundo valor: "))

soma = num_1 + num_2
sub = num_1 - num_2
mult = num_1 * num_2
div = num_1 / num_2

print(f'Soma: {soma} \nSubtração: {sub} \nMultiplicação: {mult} \nDivisão: {div}')