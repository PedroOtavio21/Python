# Escreva um programa que peça ao usuário um número e diga se ele é positivo, negativo 
# ou zero, usando condicionais if, elif e else.

number = int(input("Insira um valor qualquer: "))

if number > 0:
    print(f'O número inserido, ({number}), é positivo!')
elif number < 0:
    print(f'O número inserido, ({number}), é negativo!')
else:
    print(f'O número inserido, ({number}), é nulo!')