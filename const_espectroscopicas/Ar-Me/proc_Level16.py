from glob import glob
import sys
import subprocess


arq_fortran = glob('*.f')[0]
inputs = glob('*.txt')
nome_executavel = 'LEVEL16'
#print(inputs)
modo_vib = slice(4, 5)
modo_rot = slice(9, 10)
energia = slice(12, 24)

dados_JO = []
dados_J1 = []

for input in inputs:
    if 'J0' in input:
        print('Dados de v para J0')
        proc1 = subprocess.run(f'gfortran -o {nome_executavel} {arq_fortran}',
                               shell=True,)
        proc2 = subprocess.run(f'{nome_executavel} < {input} > output_J0.dat',
                               shell=True,)

        with open('fort.7', 'r') as f:
            s = f.readlines()

        valores_calculados = s[3:]
        if len(valores_calculados) >= 4:
            for linha in s[3:]:
                i_vib = linha[modo_vib]
                j_rot = linha[modo_rot]
                en_rovib = linha[energia].strip()
                print(i_vib, j_rot, en_rovib)
                dados_JO.append((i_vib, j_rot, en_rovib))
            en00 = dados_JO[0][2]
            en10 = dados_JO[1][2]
            en20 = dados_JO[2][2]
            en30 = dados_JO[3][2]
        else:
            print('---------------------------------------------------------')
            print(' Não podemos calcular as Constantes Espectroscópicas. :( ')
            print(' Verifique a quantidade de níveis vibracionais.          ')
            print(' Lembre-se: são necessários um mínimo de 3 níveis.       ')
            print(' quando estamos calculando para J1 ou 4 níveis,          ')
            print(' para J0.                                                ')
            print('---------------------------------------------------------')
            sys.exit()

    else:
        print('Dados de v para J1')
        proc1 = subprocess.run(f'gfortran -o {nome_executavel} {arq_fortran}',
                               shell=True,)
        proc2 = subprocess.run(f'{nome_executavel} < {input} > output_J1.dat',
                               shell=True,)

        with open('fort.7', 'r') as f:
            s = f.readlines()

        valores_calculados = s[3:]
        if len(valores_calculados) >= 3:
            for linha in s[3:]:
                i_vib = linha[modo_vib]
                j_rot = linha[modo_rot]
                en_rovib = linha[energia].strip()
                print(i_vib, j_rot, en_rovib)
                dados_J1.append((i_vib, j_rot, en_rovib))
            en01 = dados_J1[0][2]
            en11 = dados_J1[1][2]
            en21 = dados_J1[2][2]
        else:
            print('---------------------------------------------------------')
            print(' Não podemos calcular as Constantes Espectroscópicas. :( ')
            print(' Verifique a quantidade de níveis vibracionais.          ')
            print(' Lembre-se: são necessários um mínimo de 3 níveis.       ')
            print(' quando estamos calculando para J1 ou 4 níveis,          ')
            print(' para J0.                                                ')
            print('---------------------------------------------------------')
            sys.exit()

def weye(en00, en10, en20, en30):
    a = 3 * (en10 - en00)
    b = 3 * (en20 - en00)
    c = en30 - en00
    return round(1/6 * (a - b + c), 6)

def wexe(en00, en10, en20, en30):
    a = 13 * (en10 - en00)
    b = 11 * (en20 - en00)
    c = 3 * (en30 - en00)
    return round(1/4 * (a - b + c), 6)

def we(en00, en10, en20, en30):
    a = 141 * (en10 - en00)
    b = 93 * (en20 - en00)
    c = 23 * (en30 - en00)
    return round(1/24 * (a - b + c), 6)

def ye(en01, en11, en21, wexe, weye):
    a = 2 * (en11 - en01)
    b = en21 - en01
    c = 2 * wexe
    d = 9 * weye
    return round(1/4 * (-a + b + c - d), 6)

def alfa_e(en01, en11, en21, we, weye):
    a = 12 * (en11 - en01)
    b = 4 * (en21 - en01)
    c = 4 * we
    d = 23 * weye
    return round(1/8 * (-a + b + c - d), 6)

weye = weye(float(en00), float(en10), float(en20), float(en30))
wexe = wexe(float(en00), float(en10), float(en20), float(en30))
we = we(float(en00), float(en10), float(en20), float(en30))
ye = ye(float(en01), float(en11), float(en21), wexe, weye)
alfa_e = alfa_e(float(en01), float(en11), float(en21), we, weye)

print('\n')
print('Constantes Espectroscópicas [cm-1]')
print('----------------------------------')
print(f'weye = {weye}')
print(f'wexe = {wexe}')
print(f'we = {we}')
print(f'ye = {ye}')
print(f'alfa_e = {alfa_e}')
