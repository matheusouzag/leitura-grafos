'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

grafo - Funções para criação de um objeto grafo da biblioteca iGraph.
Mais informações: https://igraph.org/python/tutorial/latest/tutorial.html

05/09/2022
===================================================='''

import numpy as np

'''lerGrafp: Usado para ler uma instância'''
def lerGrafo(matriz):
    with open(matriz, 'rb') as f:
        data = np.genfromtxt(f)

    return data