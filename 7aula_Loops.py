# -*- coding: utf8 -*-
# 18/05/2015
"""
# Supondo que a populacao de um pais A seja da ordem de 80000 habitantes com uma taxa # anual de crescimento de 3% e que a populacao de B seja 200000 habitantes com uma taxa # de crescimento de 1.5%. Faca uma função que calcule e retorne o numero de anos # necessarios para que a populacao do pais. A ultrapasse ou iguale a populacao do pais # B, mantidas as taxas de crescimento.
"""
# A = 80000
# B = 200000

#import math as m
import random as r

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
#def encontrar(cadeia, letter, pos):


    
    
    
def main():
    # Exc 1 
    print("popA_vs_popB(80000, .03, 200000, .015) ", popA_vs_popB(80000, .03, 200000, .015))
    
    # Exc 2
    print("\npopA_vs_popB(80000, .03, 200000, .015) ", popA_vs_popB(80000, .03, 20000, .015))
    
    # Exc 3
    print("\ndado_count() ", dado_count())
    print("dado_count() ", dado_count())
    
    
    
if __name__ == '__main__':
    main()