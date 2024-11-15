# Crie uma função lambda que calcule o quadrado de um número e aplique essa função a uma lista de números usando map().

quadrado = lambda x: x * x

numeros = [2,5,7,6,10]

quadrados = list(map(quadrado, numeros))

print(f'Lista de Números original: {numeros}')
print(f'Lista de Números pares: {quadrados}')