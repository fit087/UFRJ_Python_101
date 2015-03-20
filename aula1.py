# -*- coding: cp1252 -*-
def soma(x,y):
    """Soma dos numeros"""
    return x+y

def raiz(a):
    """Raiz quadrada de a"""
    return a**(1.0/2.0)

def subtra(x,y):
    """Raiz quadrada de a"""
    return x-y

def multip(x,y):
        """Produto de dois numero"""
        return x*y

def div(x,y):
        """Divisão de x/y"""
        x=float(x)
        y=float(y)
        return x/y

def quadrado(a):
    """Quadrado de a"""
    return a**2

def area():
        """Area de um retangulo"""
        print 'a='
        a=input()
        print 'b='
        b=input()
        return a*b


#Essa função vai calcular a área de um retângulo
def retangulo(a,b):
        """Area de um retangulo"""
        return a*b

#Essa função vai calcular a área de uma coroa circular
def coroa(r1,r2):
        """Area da coroa"""
        pi=3.14
        area=pi*(r1**2-r2**2)
        return area

#Divisão de 2 nros inteiros
def div2(x,y):
        """Cociente e resto"""
        return x/y,x%y

#Ordenada de uma função do segundo grau
def ordenada(a,b,c,x):
        """Ordenada de uma parabola"""
        return a*x**2+b*x+c

#Entra o valor da conta e devolve a gorjeta
def gorjeta(a):
        """Gorjeta do garcao"""
        return a*0.1

#Média de dois valores
def media(a,b):
        """Media de 2 numeros"""
        return (a+b)/2


#Média ponderada de dois valores
def mediapon(a,p1,b,p2):
        """Media ponderada de 2 numeros"""
        p1=float(p1)
        return (a*p1+b*p2)/(p1+p2)
