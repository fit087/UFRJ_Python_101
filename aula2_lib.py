# -*- coding: latin1 -*-
#    Arquivo: library


"""
Created on Mon Mar 30 10:53:32 2015
    Aula 2 - Pratica: Funcao.
    Professora: Anamaria Martins Moreira (amartinsmoreira@gmail.com)
    website:http://www.dcc.ufrj.br/~pythonufrj/aulas/aula2_pratica.pdf
@author: Adolfo Correa
"""

def media(a,b):
    return (a+b)/2

def media4(a,b,c,d):
    return media(media(a,b),media(c,d))

def bombons(preco,dinheiro):
    num,troco=dinheiro//preco,dinheiro%preco
    return num,troco

import math

def hipotenusa(catA,catB):
    hipo=math.sqrt(catA**2+catB**2)
    return hipo

def dist2ptos(x1,y1,x2,y2):
    lado1=x2-x1
    lado2=y2-y1
    #return hipotenusa(lado1,lado2)
    return math.hypot(lado1,lado2)

def perimetro3ang(lado1,lado2):
    return hipotenusa(lado1,lado2)+lado1+lado2

def somaSinCos(ang):
    ang=math.radians(ang)
    soma=math.sin(ang)**2+math.cos(ang)**2
    return soma

#print somaSinCos(50)

def eq2grau(a,b,c):
    x1=(-b+math.sqrt(b**2-4*a*c))/2/a
    x2=(-b-math.sqrt(b**2-4*a*c))/2/a
    return x1,x2

def circunferencia(raio):
    return 2*math.pi*raio

def voltas(raio,dist):
    return float(dist)/circunferencia(raio)

def discriminante(a,b,c):
    return b**2-4*a*c

def eq2grau2(a,b,c):
    if discriminante(a,b,c)>=0:
        return eq2grau(a,b,c)
    else:
        #print "As raizes são imaginarias"
        return "As raizes são imaginarias"

def setorCircular(raio,ang=360):
    ang=math.radians(ang)
    return ang*raio**2

def progAritmetica(A1,An,razao):
    n=(An-A1)/razao+1
    soma=(A1+An)*n/2
    return n,soma