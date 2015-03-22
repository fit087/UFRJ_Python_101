# Filename: aula1_1.py
# -*- coding: Latin -*-

"""
Created on Mon Mar 16 10:53:32 2015
    1ra aula pratica de Computacao 1 na UFRJ.
    Professora: Ana Maria
@author: Adolfo Correa
"""

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
        """Divisao de x/y"""
        x=float(x)
        y=float(y)
        return x/y

def quadrado(a):
    """Quadrado de a"""
    return a**2

def area():
        """Area de um retangulo"""
        print ('a=')
        a=input()
        print ('b=')
        b=input()
        return a*b


#Essa funcao vai calcular a area de um retangulo
def retangulo(a,b):
        """Area de um retangulo"""
        return a*b

#Essa funcao vai calcular a area de uma coroa circular
def coroa(r1,r2):
        """Area da coroa"""
        pi=3.14
        area=pi*(r1**2-r2**2)
        return area

#Divisao de 2 nros inteiros
def div2(x,y):
        """Cociente e resto"""
        return x/y,x%y

#Ordenada de uma funcao do segundo grau
def ordenada(a,b,c,x):
        """Ordenada de uma parabola"""
        return a*x**2+b*x+c

#Entra o valor da conta e devolve a gorjeta
def gorjeta(a):
        """Gorjeta do garcao"""
        return a*0.1

#Media de dois valores
def media(a,b):
        """Media de 2 numeros"""
        return (a+b)/2


#Media ponderada de dois valores
def mediapon(a,p1,b,p2):
        """Media ponderada de 2 numeros"""
        p1=float(p1)
        return (a*p1+b*p2)/(p1+p2)


#Distancia que a correnteza arrasta um barco que atravessa um rio.
def dist_arraste(correnteza,largura,vel_barco):
    """
        Distancia que a correnteza arrasta um barco que atravessa 
        um rio. Sao conhecidas: a velocidade da correnteza, a
        largura do rio e a velocidade do barco perpendicular
        a correnteza.
        
        float,float,float → float

    """
    time=float(largura)/vel_barco
    return correnteza*time
    
#Saldo ﬁnal de uma conta.
def saldoFinal(saldoInit, meses, juros):
    """ 
        Saldo ﬁnal de uma conta, dado o saldo inicial, 
        o numero de meses e a taxa de juros mensal.
        
        float,int,float → float
    """
    return saldoInit*(1+juros*meses/100)
 
# Erro entre o valor da soma de uma PG inﬁnita e outra finita
def PG(n,q,a1=1.0):
    """
    Erro entre o valor da soma de uma PG inﬁnita a partir de 1.0 
    e a soma dos n primeiros termos.  q eh a razao e 0 ≤ q < 1.
    
        int,float,float→ float,float,float
    
    """
    Sinf=1/(1-q)
    Sn=a1*(1-q**n)/(1-q)
    return Sinf-Sn,Sinf,Sn

# Tempo da Maratona    
def tempoProva(h0,m0,s0,hf,mf,sf):
    """
    Calcula o tempo total de prova de um corredor de maratona 
    em horas, minutos e segundos, dados: o tempo de partida
    (hh,mm,ss), e o tempo de chegada (hh,mm,ss).
    
    int,int,int→ int,int,int

    """
    t0=h0*3600+m0*60+s0
    tf=hf*3600+mf*60+sf
    tf-=t0
    hf=tf//3600
    tf-=hf*3600
    mf=tf//60
    tf-=mf*60
    sf=tf
    return hf,mf,sf

 #Conta compartilhada
def equalitaria(conta,pessoas):
    """
    Calcula o valor da gorjeta (10%) e o quanto cada pessoa 
    de um grupo deve pagar (divisa˜o equalita´ria).Sa˜o dados
    o valor total da conta do restaurante e o nu´mero de pessoas
    na mesa.
    
    float,int→ float

    """
    conta+=gorjeta(conta)
    conta/=pessoas
    return conta

#Area Cubo
def cubo(c):
    """
    Calcule a ´area da superf´ıcie de um cubo que tem c por aresta.
    
        float→ float
    """
    
    return c**3
# End of aula1_1.py
