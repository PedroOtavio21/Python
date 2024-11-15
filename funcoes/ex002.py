# Crie uma função que receba uma lista de números e retorne apenas os números pares utilizando a função filter().


def pares(lista):
    pares = filter(lambda x: x % 2 == 0, lista) 
    return list(pares) # Converte o resultado em uma lista

# Diferente de JavaScript, não ocorre o encadeamento de métodos!

numeros = [1,4,3,45,2,6,7,8]

nova_lista = pares(numeros)

print(nova_lista)