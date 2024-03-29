# Constantes Espectroscópicas

Neste retositório utilizamos o programa LEVEL16 para resolver a equação
de Schrodinger nuclear e calcular um conjunto de autovalores de interece.
Com as energias calculadas ($\epsilon$) podemos calcular as constantes espectróscopicas
de um sistema diatômico ou psudodiatômico.

As energias rovibracionais são então utilizadas para calcularmos as 
seguintes constantes espectroscópicas $\omega_{e}\gamma_{e}$, $\omega_{e}x_{e}$,
$\omega_{e}$, $\alpha_{e}$ e $\gamma_{e}$ pelo sistema de equações:

$$
\omega_{e}\gamma_{e} = \frac{1}{6}\left[3(\epsilon_{1,0} - \epsilon_{0,0}) - 3(\epsilon_{2,0} - \epsilon_{0,0}) + 1(\epsilon_{3,0} - \epsilon_{0,0}) \right]
$$ 

$$
\omega_{e}x_{e} = \frac{1}{4}\left[13(\epsilon_{1,0} - \epsilon_{0,0}) - 11(\epsilon_{2,0} - \epsilon_{0,0}) + 3(\epsilon_{3,0} - \epsilon_{0,0}) \right]
$$ 

$$
\omega_{e} = \frac{1}{24}\left[141(\epsilon_{1,0} - \epsilon_{0,0}) - 93(\epsilon_{2,0} - \epsilon_{0,0}) + 23(\epsilon_{3,0} - \epsilon_{0,0}) \right]
$$ 

$$
\alpha_{e} = \frac{1}{8}\left[-12(\epsilon_{1,1} - \epsilon_{0,1}) - 4(\epsilon_{2,1} - \epsilon_{0,1}) + 4\omega_{e} - 23\omega_{e}\gamma_{e} \right]
$$ 

$$
\gamma_{e} = \frac{1}{4}\left[-2(\epsilon_{1,1} - \epsilon_{0,1}) + (\epsilon_{2,1} - \epsilon_{0,1}) + 2\omega_{e}x_{e} - 9\omega_{e}\gamma_{e} \right]
$$ 

#### O script

O script proc_Level16.py executa o código do LEVEL16 gerando o executável e calcula
as energias rovibracionais $\epsilon_{\nu, J}$ para os estados J0 e J1. Utilizando
esses dados para o cálculos das constantes espectroscópicas listadas acima.

Para que o script execute essas tarefas é necessário ter os inputs do LEVEL16 no 
diretório corrente. Os nomes dos inputs devem ser da forma: *J0.txt e *J1.txt,
por exemplo inputJ0.txt e inputJ1.txt. O programa fortran *.f deve ter as constantes c1, c2, c3, c4, c5, c6, 
alteradas se o potencial Ridberg 6 for utilizado, se caso o potencial for o 
IMPROVED LENNARD-JONES deve ser adicionado o valor de $\beta$.  






