# -*- coding: cp1252 -*-
# 31/05/2015
# Aula Pratica 9
# Exc 1
def select_sort(lista):
    "Select Sort Method"
    for index, elem in enumerate(lista):
        menor = elem
        for j_esimo, elem in enumerate(lista[index:]):
            if elem < menor:
                #lista[index] = menor
                lista[j_esimo+index] = menor
                menor = elem
        lista[index] = menor
    return lista
# Exc 2
    
def bubble_sort(lista):
    "Bubble Sort Method"
    flag = True
    while flag:
        flag = False
        for index in range(len(lista) - 1):
        #for index in range(len(lista)):
            if lista[index + 1] < lista[index]:
                aux = lista[index]
                lista[index] = lista[index + 1]
                lista[index + 1] = aux
                flag = True
    return lista

if __name__ == '__main__':  
    # Aula pratica 9
    # Exc 1
    lista = [9,8,4,5,1,9,8,6,4,8,9,2,3]
    print ("Lista desordenada")
    print (lista)
    
    print ("Lista ordenada select_sort")
    print (select_sort(lista))
    # Exc 2
    print ("Lista ordenada bubble_sort")
    print (bubble_sort(lista))
