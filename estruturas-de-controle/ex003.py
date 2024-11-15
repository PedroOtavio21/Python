# Escreva um programa que calcule a soma de todos os números pares de 1 a 100 utilizando um loop for.

sum = 0 # Inicializa uma variável 'sum' para exibir em resultado final

# Realiza uma iteração de 0 à 100, adicionando à variável sum, o somatório de todos os valors pares.
for number in range(100):
    if(number % 2 == 0):
        sum += number

# Exibe o resultado no terminal
print(f'Resultado da soma dos valores pares, presentes no intervalo de 1 à 100: {sum}')