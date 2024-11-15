# Crie um programa que leia um número e exiba se ele é par ou ímpar usando o operador %.

num = int(input("Insira um valor inteiro qualquer: ")) # Inicializa e recebe um valor pelo terminal

# Exibe, através de uma verificação, se o valor é par ou ímpar
if num % 2 == 0:
    print(f'O valor inserido, ({num}) é par!')
else:
    print(f'O valor inserido, ({num}) é ímpar!')