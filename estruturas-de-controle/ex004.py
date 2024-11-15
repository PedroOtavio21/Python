# Crie um programa que simule uma senha de 4 dígitos. O usuário tem 3 tentativas para acertar. 
# Use um loop while e o break para controlar as tentativas.

senha = input("Crie sua senha: ") # Inicializa e recebe uma senha com valor qualquer (número ou string)

tentativas = 3 # Inicializa as 3 tentativas limites de acesso

# Realiza um loop while, com condições de parada de erro, esgotamento de tentativas e acerto de senha.
while tentativas > 0:
    teste = (input('Insira sua senha de acesso: '))
    if teste != senha:
        tentativas -= 1
        if tentativas > 0:
            print(f'Acesso negado. {tentativas} tentativas restantes.')
        else:
            print(f'Tentativas esgotadas. Bloqueando acesso ...')
    else:
        print('Acesso liberado.')
        break