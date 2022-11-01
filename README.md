# LEVEL 16

Repositório armazena scripts para extração e processamento de dados 
associados ao programa LEVEL16.

- O programa LEVEL16 foi escrito pelo professor Robert J. Le Roy.
O título de seu artigo é: *A computer program for solving the
radial Schrodinger equation for bound and quasebounds levels.* 

- O programa resolve a equação de Schrodinger radial unidimencional, 
localiza automaticamente todos on níveis ligados ou quase ligados
para um conjunto de potenciais que podem ser simples ou duplos. 

- Calcula as constantes de rotação inercial, bem como as constantes 
de distorção centrífuga. Entre outras funcionalidades.

- Foram realizadas algumas modificações no código. Inserimos os
potenciais de Ridberg em grau 6 e Improved Lennard–Jones.

### Rydberg 6

$$
  V_{Ryd}(R) = -D_{e}\left[1 + \sum_{i=1}^{6}c_{i}(R-R_{e})^{i}\right]e^{-c_{1}(R-R_{e})}
$$

### Improved Lennard–Jones

$$
 n(R) = \beta + 4 \left(\frac{R}{R_{e}} \right)
$$

$$
  V_{ILJ}(R) = -D_{e}\left[\frac{6}{n(r) - 6} \left(\frac{R}{R_{e}} \right)^{n(R)} - \frac{n(R)}{n(r) - 6} \left(\frac{R}{R_{e}} \right)^{6}\right]
$$




