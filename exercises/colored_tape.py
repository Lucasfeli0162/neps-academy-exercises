tamanho_da_fita = int(input())
fita = [int(i) for i in input().split()]
fita_colorida = []


def percorrer_lista(fita):
    pass


for pos, item in enumerate(fita):
    if item == -1:
        percorrer_lista(fita)
