# Crie uma lista com os números de 1 a 10 e imprima apenas os números pares.

numeros = [] # Inicializa a lista

# Adiciona valores na lista por meio de um loop for
for number in range(10):
    if(number % 2 == 0):
        numeros.append(number) # Adiciona o item na última posição da lista

# Exibe valores da lista
print(numeros)