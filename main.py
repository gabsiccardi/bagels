# 1 - BAGELS
# BY: Gabriel Siccardi
# 13/10/2021
# ver. 1.0.0

import functions

print("ADIVINHE O NUMERO\n")
print("DICAS:\n")
print("- O numero possui TRÊS digitos:\n")
print("- Pico: Um digito está correto MAS na posição errada.\n")
print("- Fermi: Um digito está correto E na posição correta\n")
print("- Bagels: Nenhum digito está correto.\n")
print("Você tem 10 tentativas!\n")
repete = True
while repete:
    numero_secreto = functions.get_numero()
    cont_tentativas = 0
    while cont_tentativas < 10:
        cont_tentativas += 1
        tentativa = []
        tent = input("Tentativa #{}\n".format(cont_tentativas))
        tentativa += str(tent)
        dicas = functions.get_dicas(tentativa, numero_secreto)
        print('Dicas: ')
        print(dicas)
        if tentativa == numero_secreto:
            opcao = input("Gostaria de jogar novamente? (y/n)\n")
            if opcao == 'y':
                repete = True
                break
            else:
                repete = False
                break

        if cont_tentativas > 9:
            print("Você não tem mais tentativas, o numero era {}".format(numero_secreto))
            opcao = input("Gostaria de jogar novamente? (y/n)\n")
            if opcao == 'y':
                repete = True
                break
            else:
                repete = False
                break
