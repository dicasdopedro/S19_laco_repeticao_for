i = int(input('Começa com este número:'))
f = int(input('Termina com este número:'))
p = int(input('E vai pulando de quanto em quanto?:'))
for c in range(i, f+1, p):
    print(c)
print('FIM')