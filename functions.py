import random


def get_numero():
    numero_secreto = []
    num = random.randint(100, 999)
    numero_secreto += str(num)
    return numero_secreto


def get_dicas(tentativa, numero_secreto):
    if tentativa == numero_secreto:
        return "Você acertou!!!\n"

    dicas = []

    for i in range(3):
        if tentativa[i] == numero_secreto[i]:
            dicas.append(' Fermi ')
        elif tentativa[i] in numero_secreto:
            dicas.append(' Pico ')
    if len(dicas) == 0:
        return 'Bagels'
    else:
        dicas.sort()
        return ''.join(dicas)
