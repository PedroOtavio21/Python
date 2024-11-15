# Crie um programa que solicite ao usuário três notas e calcule a média aritmética delas. 
# Exiba se o aluno está "Aprovado" (média ≥ 7) ou "Reprovado".

print("Insira as três notas do aluno:")

# Inicializa e recebe as 3 notas 
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

# Realiza o cálculo e armazena a média das notas
media = (n1 + n2 + n3) / 3.0

# Exibe situação de usuário por meio da média
if media >= 7.0:
    print('Aprovado!')
else:
    print("Reprovado.")