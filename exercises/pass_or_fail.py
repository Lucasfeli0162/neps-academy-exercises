A, B = [float(i) for i in input().split()]
average = (A+B) / 2
if average >= 7:
    print('Aprovado')
elif average < 4:
    print('Reprovado')
else:
    print('Recuperacao')