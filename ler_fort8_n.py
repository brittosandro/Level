arq = open('fort.8', 'r')
lista_de_strings = [linha for linha in arq.readlines()]
arq.close()

n = int(input('Inf. Número de Níveis Vibracionais: '))  # n denota a quantidade de níveis vibracionais do Sistema
nome = input('Inf. Nome do Arquivo de Output: ')        # nome arquivo de output

somas_niveis_vib = []               # Lista para armazenar os valores dos níveis vibracionais
somas_coef_einstein = []            # Lista para armazenar os valores dos coeficientes de Einstein

for j in range(0, n+1):
    total_vib = 0                   # Contador para os níveis vibracionais
    soma_coef_einstein = 0          # Contador para os coeficientes de Einstein

    for i in range(len(lista_de_strings)):
        niveis_vibracionais = lista_de_strings[i][11: 12]
        coef_einstein = lista_de_strings[i][41: 52]         # coef_einstein são os coeficientes de einstein

        if niveis_vibracionais == str(j):
            coef_einstein = coef_einstein.replace('D', 'e')
            coef_einstein = float(coef_einstein)
            total_vib += 1
            soma_coef_einstein += coef_einstein

    somas_niveis_vib.append(total_vib)
    somas_coef_einstein.append(soma_coef_einstein)

print(somas_niveis_vib)
print(somas_coef_einstein)


arq1 = open(nome, 'w')

arq1.write('###################################################################################\n')
arq1.write('#                                                                                 #\n')
arq1.write('#                           Tabela de Resultados                                  #\n')
arq1.write('#                           ____________________                                  #\n')
arq1.write('#                                                                                 #\n')
arq1.write('###################################################################################\n')
arq1.write('\n \n ')

arq1.write(' Níveis Vibracionais |  Quantidade de cada Nível | Somas coeficientes Einstein (nm)\n')
arq1.write('-----------------------------------------------------------------------------------\n')

for niveis, q_nivel in zip(range(n), somas_niveis_vib):                         # A variável q_nivel denota a soma dos níveis
    arq1.write('{:10} {:25d} {:33.10f}\n'.format(niveis, q_nivel, (somas_coef_einstein[niveis]*(10**9))))
    arq1.write('-----------------------------------------------------------------------------------\n')

arq1.close()

print('\n************************************************************************')
print('*                                                                      *')
print('*   Já calculamos -> Resultados em  | {} |        *'.format(nome))
print('*   -------------    ------------------------------------------------- *')
print('*                                                                      *')
print('************************************************************************\n\n')

#print('Lista de Somas Niv. Vibracionais = {}'.format(somas_niveis_vib))
#print('Lista de Soma Coef. Einstein = {}'.format(somas_coef_einstein))

