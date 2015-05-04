# -*- coding: cp1252 -*-
# 04/05/2015
# Aula 6 Listas

"""
Created on Mon May 04 10:53:32 2015
    6a aula "pratica" (revisão para P1) de Computacao 1 na UFRJ.
    Professor: Anamaria Martins Moreira (amartinsmoreira@gmail.com)
    Topic: Revisão para P1, P1 - 15/08/2014 Teoria e Pratica
@author: Adolfo Correa (fit087@gmail.com)
"""

# Prova P2 2014
"""
l1 = range(3,9)

# ponto 1
l2 = l1

# ponto 2
l3 = l2[:]

# ponto 3
l3[1] = [5]

# ponto 4
l3[0:2] = [20,[30]]

# ponto 4'      # Muito importante a lista [2,3,4] sera carregada na memoria
l1 = [2, 3, 4]  # e o indicador l1 apontara a aquela posição na memoria.
                # Assim a l2 continuara apontando a mesma posição na memoria,
                # que não foi remplazada. Então o valor de l2 continua igual.

# ponto 5
l1[1] = "abc"

# ponto 6
l2[3:5] = "ab"

# ponto 7
"""

# Prova P1 Teorica - 15/08/2014

# Questão 1
def approbation_criteria(P1, P2, P3, PR, peso1 = 8, peso2 = 2):
    media_final = (mediaT(P1, P2, P3, PR) * peso1 + PR * peso2)
    media_final /= peso1 + peso2
    return media_final

def mediaT(P1, P2, P3, peso1 = 4, peso2 = 6):
    media = (P1 * peso1 + max(P2, P3) * peso2) / (peso1 + peso2)
    return media

# Prova P1 Pratica - 15/08/2014

# Questão 1
def f1(n):
    return 2*n**2

# Questão 2
def f2_ordem(a, b, c):
    if a<b and b<c:
        return "crescente"
    elif a>b and b>c:
        return "decrescente"
    else:
        return "desordenados"

# Questão 3
def data2text(data):
    return str.replace(data, "/", " de ")

# Questão 4
def reta(pnt1, pnt2):
    if pnt1[1] == pnt2[1]:
        if pnt1[0] == pnt2[0]:
            return "Os pontos são iguais"
        else:
            return "Reta Vertical"
    elif pnt1[0] == pnt2[0]:
        return "Reta Horizontal"
    else:
        return "Reta Inclinada"


if __name__ == '__main__':
    """print (l1)
    print (l2)
    print (l3)"""

    print ("approbation_criteria(10,10,5,10) = ", approbation_criteria(10,5,10,1))
    print ("f1(5) = ", f1(5))
    print ("f2_ordem(5,7,8) = ", f2_ordem(5,7,8))
    print ("f2_ordem(8,7,4) = ", f2_ordem(8,7,4))
    print ("f2_ordem(8,7,4) = ", f2_ordem(8,7,7))
    print ("data2text(\"04/05/2015\") = ", data2text("04/05/2015"))
    print ("reta((5,3),(5,5)) = ", reta((5,3),(5,5)))
    print ("reta((1,5),(5,5)) = ", reta((1,5),(5,5)))
    print ("reta((5,3),(3,4)) = ", reta((1,5),(3,4)))
    print ("reta((5,3),(5,5)) = ", reta((1,5),(1,5)))
