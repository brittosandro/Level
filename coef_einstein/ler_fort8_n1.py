arq = open('fort.8', 'r')
lista_de_strings = [linha.split() for linha in arq.readlines()]
arq.close()

const_fatiamento = 11          # Essa constante expressa o ponto do arquivo que temos interesse
const_linha_vib1 = 2           # Essa constante expressa a posição do nível de interesse
const_linha_coef_eins = 7      # Essa constante expressa a posição do coeficiente de einstein


n = int(input('Inf. Número de Níveis Vibracionais: '))  # n denota a quantidade de níveis vibracionais do Sistema
nome = input('Inf. Nome do Arquivo de Output: ')        # nome arquivo de output

lista_niveis = []              # Lista para armazenar as somas dos níveis vibracionais
lista_coef_einstein = []       # Lista para armazenar as somas dos coeficientes de Einstein

for i in range(n):
    numero_niveis = 0
    coef_eins = 0              # Contador para coeficiente de einstein

    for j in range(11, len(lista_de_strings)):
        if lista_de_strings[j][const_linha_vib1] == str(i):
            numero_niveis += 1
            coef_eins += float(lista_de_strings[j][const_linha_coef_eins].replace('D', 'e'))

    lista_niveis.append(numero_niveis)
    lista_coef_einstein.append(coef_eins)

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

for niveis, q_nivel in zip(range(n), lista_niveis):
    arq1.write('{:10} {:25d} {:33.10f}\n'.format(niveis, q_nivel, lista_coef_einstein[niveis]*10**9))
    arq1.write('-----------------------------------------------------------------------------------\n')

arq1.close()

print('\n************************************************************************')
print('*                                                                      *')
print('*   Já calculamos -> Resultados ;)                                     *'.format(nome))
print('*   -------------    ------------------------------------------------- *')
print('*                                                                      *')
print('************************************************************************\n\n')
