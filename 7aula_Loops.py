# -*- coding: utf8 -*-
# 18/05/2015
# Aula 7
"""
Created on Mon May 18 10:53:32 2015
    7a aula pratica de Computacao 1 na UFRJ.
    Professor: Anamaria Martins Moreira (amartinsmoreira@gmail.com)
    Topic: Estruturas de Repetição
@author: Adolfo Correa (fit087@gmail.com)
"""

"""
# Supondo que a populacao de um pais A seja da ordem de 80000 habitantes com uma taxa # anual de crescimento de 3% e que a populacao de B seja 200000 habitantes com uma taxa # de crescimento de 1.5%. Faca uma função que calcule e retorne o numero de anos # necessarios para que a populacao do pais. A ultrapasse ou iguale a populacao do pais # B, mantidas as taxas de crescimento.
"""
# A = 80000
# B = 200000

#import math as m
import random as r
import math as m

def pop_grown(pop, tax):
    return pop*(1+tax)
    
# Exc 1 e 2    
def popA_vs_popB(A, tax_A, B, tax_B):
    if (A < B and tax_A < tax_B) or (A > B and tax_A > tax_B):
        return "As populacoes nao serao iguais nunca"
    count_year = 0
    pop_min = min(A, B)
    pop_max = max(A, B)
    tax_min = max(tax_A, tax_B)
    tax_max = min(tax_A, tax_B)  
    while pop_min < pop_max: # python 3
    #while A != B: # python 3
    #while A <> B:  # python 2 
        #count_year += 1
        #A *= 1+tax_A
        #B *= 1+tax_B
        count_year += 1
        pop_min *= 1 + tax_min
        pop_max *= 1 + tax_max
    return count_year
    
# Exc 3
def dado_count():
    counter = 1
    first_time = r.randint(0, 6)
    second_time = r.randint(0, 6)
    while first_time != second_time:
        counter += 1
        first_time = r.randint(0, 6)
        second_time = r.randint(0, 6)
    return counter

# Exc 4
# str.find(umaString, substring, inicio, fim)
def encontrar(cadeia, letter, incid_max):
    pos = str.find(cadeia, letter)
    pos_ant = pos
    event = 1 if not pos == -1 else 0
    #incid = 1 if not pos == -1 else 0
    incid = event
    #if pos + 1:
    #while pos + 1:
    while event and incid < incid_max:
        pos_ant = pos
        pos = str.find(cadeia, letter, pos + 1, len(cadeia) - 1)
        event = 1 if not pos == -1 else 0
        #incid += 1 if not pos == -1 else 0
        incid += event
    return incid,pos
        
# Exc 5. Fibonacci
#def fibonacci(num):
#    term_1 = 0
#    term_2 = 1
#    sum = 0
#    if num == 1: 
#        sum = term_1
#    elif num == 1:
#        sum = term_2
#    count = 2
#    sum = term_1 + term_2
#    while count < num:
#        nw_term = term_1 + term_2
#        
#        sum += nw_term
#        count += 1
#    return sum
    
def fibonacci_term(num):
    "Return a fibonacci term. Using a iterative method"
    term_1 = 0
    term_2 = 1
    if num == 1: 
        nw_term = term_1
    elif num == 2:
        nw_term = term_2
    count = 2
    while count < num:
        nw_term = term_1 + term_2
        term_1 = term_2
        term_2 = nw_term
        count += 1
    return nw_term
    
def fibonacci_serie(term):
    "Return a sum of term fibonacci numbers. Using a function fibonacci_terms"
    serie_fibonacci = [0]*term
    for count in range(0, term):
        serie_fibonacci[count] = fibonacci_term(count + 1)
        #serie_fibonacci[count] = fibonacci_term(count)
    return serie_fibonacci
    
def list_sum(list):
    sum = 0
    for term in list:
        sum += term
    return sum
    
def fibonacci_sum(term):
    return list_sum(fibonacci_serie(term))

# Exc 6. Fatorial
def fact(num):
    fact = 1
    for n in range(1, num + 1, 1):
        fact *= n
    return fact
    
# Exc 7. Prime numbers
def is_prime(num):
    prime = True
    for counter in range(2, int(m.sqrt(num) + 1)):
        if num % counter == 0: 
            prime = False
            print("Entrou e Saiu?")
            break
    return "O numero é primo?", prime

    

    
    
    
def main():
    print ("\n\n\n********************************")
    print ("\t7a Aula. Loops")
    print ("********************************\n")


    # Exc 1 
    print ("\n\n\n***************************")
    print ("\t1o Exercicio")
    print ("***************************\n")

    print("popA_vs_popB(80000, .03, 200000, .015) ", popA_vs_popB(80000, .03, 200000, .015))
    
    # Exc 2
    print ("\n\n\n***************************")
    print ("\t2o Exercicio")
    print ("***************************\n")

    print("\npopA_vs_popB(80000, .03, 200000, .015) ", popA_vs_popB(80000, .03, 20000, .015))
    
    # Exc 3
    print ("\n\n\n***************************")
    print ("\t3o Exercicio")
    print ("***************************\n")

    print("\ndado_count() ", dado_count())
    print("dado_count() ", dado_count())
        
    # Exc 4
    print ("\n\n\n***************************")
    print ("\t4o Exercicio")
    print ("***************************\n")

    print("\nencontrar(Hola, que tal?, q, 1) ", encontrar("Hola, que tal?", "q", 1))
    print("\nencontrar(Hola, que tal?, d, 1) ", encontrar("Hola, que tal?", "d", 1))
    print("\nencontrar(Hola, que tal?, a, 2) ", encontrar("Hola, que tal?", "a", 2))
    print("\nencontrar(Hola, que tal?, a, 2) ", encontrar("Hola, que tal?","?", 1))
    print("\nencontrar(mariana come banana, a, 3) ", encontrar("mariana come banana","a", 3))
      
    # Exc 5
    print ("\n\n\n***************************")
    print ("\t5o Exercicio")
    print ("***************************\n")

#    print("\nfibonacci(1) ", fibonacci(1))
#    print("\nfibonacci(2) ", fibonacci(2))
#    print("\nfibonacci(3) ", fibonacci(3))
#    print("\nfibonacci(4) ", fibonacci(4))
#    print("\nfibonacci(5) ", fibonacci(5))
#    print("\nfibonacci(6) ", fibonacci(6))
    
    print("\nfibonacci_terms(1) ", fibonacci_term(1))
    print("\nfibonacci_terms(2) ", fibonacci_term(2))
    print("\nfibonacci_terms(3) ", fibonacci_term(3))
    print("\nfibonacci_terms(4) ", fibonacci_term(4))
    print("\nfibonacci_terms(5) ", fibonacci_term(5))
    print("\nfibonacci_terms(6) ", fibonacci_term(6))
    print("\nfibonacci_terms(19) ", fibonacci_term(19))
    print("\nfibonacci_terms(20) ", fibonacci_term(20))
    print("\nfibonacci_serie(5) ", fibonacci_serie(5))
    print("\nfibonacci_sum(5) ", fibonacci_sum(5))
    print("\nfibonacci_serie(7) ", fibonacci_serie(7))
    print("\nfibonacci_sum(7) ", fibonacci_sum(7))
    print("\nfibonacci_serie(7) ", fibonacci_serie(10))
    print("\nfibonacci_sum(7) ", fibonacci_sum(10))
      
    # Exc 6
    print ("\n\n\n***************************")
    print ("\t6o Exercicio")
    print ("***************************\n")

    print("\nfact(1) ", fact(1))
    print("\nfact(2) ", fact(2))
    print("\nfact(3) ", fact(3))
    print("\nfact(4) ", fact(4))
    print("\nfact(5) ", fact(5))
    print("\nfact(6) ", fact(6))
      
    # Exc 7
    print ("\n\n\n***************************")
    print ("\t7o Exercicio")
    print ("***************************\n")

    print("\nis_prime(24) ", is_prime(24))
    print("\nis_prime(23) ", is_prime(23))


    

    
    
if __name__ == '__main__':
    main()