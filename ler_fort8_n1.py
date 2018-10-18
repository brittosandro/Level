arq = open('fort.8', 'r')
lista_de_strings = [linha for linha in arq.readlines()]
arq.close()

n = int(input('Inf v.: '))
s = []
a0 = 0
for i in range(len(lista_de_strings)):
    for j in range(n):
        niveis_vibracionais = lista_de_strings[i][11: 12]
        if niveis_vibracionais == str(j):
            a0 += 1
    s.append(a0)

print('Lista de somas = {}'.format(s))
