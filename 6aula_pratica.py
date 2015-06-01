# 31/05/2015
# Aula pratica 6
def inv_phrase(phrase):
    lista = str.split(phrase)
    lista.reverse()
    #lista = list.reverse(lista)
    phrase = str.join(" ", lista)
    return phrase
    
# Aula Pratica 9
#def select_sort(lista):
#    sort_list = lista[:]
#    #for index in range(len(lista)):
#    for index, elem in enumerate(lista):
#    #index = 0
#    #while lista:
#        #menor = lista[index]
#        menor = elem
#        #for elem in lista[index:]:
#        for elem in lista:
#            if elem < menor:
#                menor = elem
#        #list.remove(lista[index:], menor)
#        list.remove(lista, menor)
#        sort_list[index] = menor
#    return sort_list
    
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
    print (inv_phrase("eu gosto de doce"))
    lista = [9,8,4,5,1,9,8,6,4,8,9,2,3]
    print (lista)
    print (select_sort(lista))
    print (bubble_sort(lista))