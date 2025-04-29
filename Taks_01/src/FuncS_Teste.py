#==================================================================================
#
#         Nome: TestingFunctions.py    Usado para testar as funções de ativação
#
#     Autor: João Gustavo Silva Guimarães   
#
#     Notas:
#       Grau de pertinencia: Valor que representa amostragem no conjunto fuzzy
#         Ex: Um 1.7 metros de altura de um salto em cama elástica, representa um grau de pertinência de 0.5 para o grau de ativação "salto alto"
#       
#       Grau de ativação: Impacto de um grau de pertinência em uma lógica fuzzy
#           Ex: o Grau de ativação para "alto" é qualquer valor maior que 1 e 1.8 
#
#==================================================================================


from Functions import Triangular, Trapezoidal, Gaussiana, Sigmoidal, Sino_Generalizada, FuncS, FuncZ, Cauchy, Gaussiana_Dupla, UserFunction1, UserFunction2
from numpy import linspace, array, round
import matplotlib.pyplot as plt

# Amostras 1: altura de saltos em cama elástica
altura_de_saltos_em_cama_elastica = round(linspace(0, 5, 16), 2)

# Amostras 2: altura de saltos para enterrada no basquete
altura_de_saltos_para_enterrada_no_basquete = round(linspace(0, 4, 16), 2)



comum = [altura_de_saltos_em_cama_elastica[0:4], 'salto comum']
alto = [altura_de_saltos_em_cama_elastica[3:7], 'salto alto']
muito_alto = [altura_de_saltos_em_cama_elastica[6:10], 'salto muito alto']
perigoso = [altura_de_saltos_em_cama_elastica[9:13], 'salto perigoso']
#
dados_cama_elastica = [comum, alto, muito_alto, perigoso]


comum = [altura_de_saltos_para_enterrada_no_basquete[0:4], 'longe da cesta']
alto = [altura_de_saltos_para_enterrada_no_basquete[3:7], 'próximo da cesta']
muito_alto = [altura_de_saltos_para_enterrada_no_basquete[6:10], 'boa altura para enterrar']
perigoso = [altura_de_saltos_para_enterrada_no_basquete[9:13], 'alto de mais para enterrar']

# Definindo os valores de ativação para cada função
dados_basquete = [comum, alto, muito_alto, perigoso]


colors = {
    '1': 'blue',
    '2': 'green',
    '3': 'yellow',
    '4': 'red'
}

fig, ax_cama_elastica = plt.subplots()
fig, ax_basquete = plt.subplots()

# Definindo os valores de ativação para cada função
for index, dado in enumerate(dados_cama_elastica):
    a, b = round(dado[0],1)[0],round(dado[0],1)[1]
    color_i = colors[str(index+1)]
    pertinencia = [FuncS(round(x, 1), a, b) for x in altura_de_saltos_em_cama_elastica]

    ax_cama_elastica.plot(altura_de_saltos_em_cama_elastica, pertinencia, label=f'Pertinência {a}, {b} : {dado[1]}', color=color_i, linewidth = 2)


# Definindo os valores de ativação para cada função
for index, dado in enumerate(dados_basquete):
    a, b = round(dado[0],1)[0],round(dado[0],1)[1]
    color_i = colors[str(index+1)]
    pertinencia = [FuncS(round(x, 1), a, b) for x in altura_de_saltos_para_enterrada_no_basquete]

    ax_basquete.plot(altura_de_saltos_para_enterrada_no_basquete, pertinencia, label=f'Pertinência {a}, {b} : {dado[1]}', color=color_i, linewidth = 2)




ax_cama_elastica.set_xlabel('Metros acima do solo saltando em cama elástica')
ax_cama_elastica.set_ylabel('Grau de ativação')
ax_cama_elastica.set_title('Fuzzyficação Amostragem 1')
ax_cama_elastica.legend()

ax_basquete.set_xlabel('Altura alcançada por um jogador de basquete ao tentar realizar uma enterrada')
ax_basquete.set_ylabel('Grau de ativação')
ax_basquete.set_title('Fuzzyficação Amostragem 2')
ax_basquete.legend()


plt.show()

