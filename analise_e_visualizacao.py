# -*- coding: utf-8 -*-
"""analise_e_visualizacao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CcRsMeniAUgPNTbpiKRUnEiUxZUihgwB

Vamos pensar no seguinte exemplo. Temos um conjunto de dados que indica as compras efetuadas pelos lientes e um dos campos desses dados é a quantidade de itens comprados. Vamos gerar uma matriz que contém quantidades aleatórias para 100 compras.
"""

import numpy as np
media=20
desvio_padrao=4
quant=1000
#o comando random.normal gera números aleatórios seguindo uma distribuição normal
qitens=np.round(np.random.normal(media,desvio_padrao,quant))

"""Agora precisamos analisar esses dados. Evidententemente, apenas ler os números não faz com que seja possível obter informação útil o interessante. Portanto, vamos criar uma gráfico mostrando esses dados."""

import matplotlib.pyplot as plt
plt.plot(qitens)

"""O gráfico acima é conceitualmente inadequado. Gráficos de linha só fazem senstido quando os eixos são ordenadas, ou seja, seguem uma certa ordem, como espaço ou tempo, e o eixo y está em funação do eixo x. Vamos primeiro mudar o gráfico para um gráfico de barras."""

registros=np.arange(1,qitens.shape[0]+1)
plt.bar(registros,qitens)
plt.xlabel("registro de compra")
plt.ylabel("quantidade comprada")

"""O gráfico, apenas de agora estar correto, continua não dando informações úteis. Vamos então fazer um tip diferente de gráfico, um histograma. Um histograma mostra a frequência com que valores aparecem em uma lista."""

classes=10
plt.hist(qitens,bins=classes)
plt.xlabel("quantidade comprada")
plt.ylabel("Frequência")

"""Esse gráfico já é muito mais útil, pois informa que o valor com maior probabilidade de acontecer é o valor 20 ou seja, a maioria das pessoas compra por volta de 20 itens, e quanto mais nos afastamos desse velor, menor a probabilidade.

Vamos agora ver outro exemplo. Digamos que um sistema de agricultura de alta precisão dividiu uma lavoura em vários lotes menores de 1 ha cada, registrando quanto sacos foram colhidos em cada ha. A lavoura possui 100 ha em um formato quadrado de 10x10 ha. Os dados de pordução de cada ha formam uma matriz de 10x10.
"""

#o comando rand gera números aleatórios de 0 até 1 em uma matriz definida (10,10)
lavoura=np.random.rand(10,10)*50+40
print(lavoura)

"""Observar diretamente os dados da matriz torna difícil realizar uma análise. Vamos então fazer um gráfico que ilustre melhor a informação. Nesse caso, vamos utilizar um mapa de calor. Um mapa de calor é um gráfico que mostra a intensidade de uma valor em coordenadas x,y."""

plt.imshow(lavoura)
plt.colorbar()