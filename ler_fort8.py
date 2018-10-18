arq = open('fort.8', 'r')
lista_de_strings = [linha for linha in arq.readlines()]
arq.close()

v0, soma_coef_einstein0 = 0, 0
v1, soma_coef_einstein1 = 0, 0

v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0
v8 = 0
v9 = 0

somas_coef_einstein = []

for i in range(len(lista_de_strings)):
    vib1 = lista_de_strings[i][11: 12]                 # vib1 é definido como nível vibracional inicial
    coef_einstein = lista_de_strings[i][41: 52]        # coef_einstein são os coeficientes de einstein

    #print(vib1)
    #print(coef_einstein)
    soma_coef_einstein = 0
    if vib1 == '0':
        v0 += 1
        coef_einstein = coef_einstein.replace('D', 'e')
        soma_coef_einstein += float(coef_einstein)
        #somas_coef_einstein.append(soma_coef_einstein0)
    elif vib1 == '1':
        v1 += 1
        coef_einstein = coef_einstein.replace('D', 'e')
        soma_coef_einstein += float(coef_einstein)
        #somas_coef_einstein.append(soma_coef_einstein1)

    somas_coef_einstein.append(soma_coef_einstein)

'''
    elif vib1 == '2':
        v2 += 1
        soma_coef_einstein += int(coef_einstein)
        somas_coef_einstein.append(soma_coef_einstein)
    elif vib1 == '3':
        v3 += 1
        soma_coef_einstein += int(coef_einstein)
        somas_coef_einstein.append(soma_coef_einstein)
    elif vib1 == '4':
        v4 += 1
        soma_coef_einstein += int(coef_einstein)
        somas_coef_einstein.append(soma_coef_einstein)
    elif vib1 == '5':
        v5 += 1
        soma_coef_einstein += int(coef_einstein)
        somas_coef_einstein.append(soma_coef_einstein)
    elif vib1 == '6':
        v6 += 1
        soma_coef_einstein += int(coef_einstein)
        somas_coef_einstein.append(soma_coef_einstein)
    elif vib1 == '7':
        v7 += 1
        soma_coef_einstein += int(coef_einstein)
        somas_coef_einstein.append(soma_coef_einstein)
    elif vib1 == '8':
        v8 += 1
        soma_coef_einstein += int(coef_einstein)
        somas_coef_einstein.append(soma_coef_einstein)
    elif vib1 == '9':
        v9 += 1
        soma_coef_einstein += int(coef_einstein)
        somas_coef_einstein.append(soma_coef_einstein)



    if linha[0] == ' R(  0)':
        print(linha[0])
    else:
        print(linha[2])
'''

print('v0 = {}'.format(v0))
print('v1 = {}'.format(v1))
print('v2 = {}'.format(v2))
print('v3 = {}'.format(v3))
print('v4 = {}'.format(v4))
print('v5 = {}'.format(v5))
print('v6 = {}'.format(v6))
print('v7 = {}'.format(v7))
print('v8 = {}'.format(v8))
print('v9 = {}'.format(v9))

print(somas_coef_einstein)
print(soma_coef_einstein0)
print(soma_coef_einstein1)
