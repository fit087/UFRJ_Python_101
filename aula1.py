# -*- coding: cp1252 -*-
def soma(x,y):
	return x+y

def raiz(a):
	return a**(1.0/2.0)

def subtra(x,y):
	return x-y

def multip(x,y):
        return x*y

def div(x,y):
        """ayuda"""
        x=float(x)
        y=float(y)
        return x/y

def quadrado(a):
        return a**2

def area():
        print 'a='
        a=input()
        print 'b='
        b=input()
        return a*b


#Essa função vai calcular a área de um retângulo
def retangulo(a,b):
        return a*b

#Essa função vai calcular a área de uma coroa circular
def coroa(r1,r2):
        pi=3.14
        area=pi*(r1**2-r2**2)
        return area

#Divisão de 2 nros inteiros
def div2(x,y):
        return x/y,x%y

#Ordenada de uma função do segundo grau
def ordenada(a,b,c,x):
        return a*x**2+b*x+c

#Entra o valor da conta e devolve a gorjeta
def gorjeta(a):
        return a*0.1

#Média de dois valores
def media(a,b):
        return (a+b)/2


#Média ponderada de dois valores
def mediapon(a,p1,b,p2):
        p1=float(p1)
        return (a*p1+b*p2)/(p1+p2)
