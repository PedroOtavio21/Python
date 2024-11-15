# Crie um dicionário que armazene o nome, idade e cidade de uma pessoa e exiba essas informações de forma organizada.

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
cidade = input("Insira o nome da cidade em que você reside: ")

pessoa = {
    'nome': nome,
    'idade': idade,
    'cidade': cidade
}

print(pessoa)