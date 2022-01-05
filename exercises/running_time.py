from math import ceil
voltas, placas = [int(i) for i in input().split()]
placas_totais = placas * voltas
porcentagens = []
for c in range(10, 100, 10):
    prov = c * placas_totais / 100
    if type(prov) == float:
        prov = ceil(prov)
    porcentagens.append(prov)
for item in porcentagens:
    print(item, end=' ')
