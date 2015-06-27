# -*- coding: cp1252 -*-
# 31/05/2015
# Aula pratica 6
# Exc 1
def inv_phrase(phrase):
    """func�ao que dada uma frase retorne uma outra frase que contenha
        as mesmas palavras da frase de entrada na ordem inversa."""
    lista = str.split(phrase)
    lista.reverse()
    #lista = list.reverse(lista)
    phrase = str.join(" ", lista)
    return phrase
    
# Exc 2
def alphabetic_sort(phrase):
    """Fun�c�ao que dada uma frase, reordene as palavras em ordem alfab�etica.
    Retorne a frase alterada.
"""
    phrase_returned = str.split(phrase)
    list.sort(phrase_returned)
    str.join(" ", phrase_returned)
    return phrase_returned
    
# Exc 3
def vowel_change(phrase):
    """Fun�c�ao que dada uma frase, troque todas as vogais das palavras
    consideradas por i."""
    #for letter in phrase:
    nw_phrase = phrase[:]
    #for vowel in ("a", "e", "o", "u"):
    for vowel in ["a", "e", "o", "u"]:
        nw_phrase = str.replace(nw_phrase, vowel, "i")
    return nw_phrase
# Exc 4
def ins_word(phrase, word, position):
    """
    Fun�c�ao que receba uma frase, uma palavra e uma posi�c�ao. Caso a palavra
    j�a exista na frase, transforme-a para mai�uscula e mostre a frase
    novamente. Caso a palavra n�ao exista, insira a palavra na frase na posi�c�ao
    dada. Assuma que a primeira palavra est�a na posi�c�ao 0.
    retorne a nova frase.
    """
    o_phrase = phrase[:]
    list_phrase = str.split(phrase)
    if word in list_phrase:
        #up_word = str.upper(word)
        position = list.index(list_phrase, word)
        word = str.upper(word)
        #print word
        list_phrase[position] = word
    else:
        #list_phrase.insert(position, word)         # Both are ok
        list.insert(list_phrase, position, word)    # Both are ok
    #list_phrase[position] = up_word
    #list_phrase[position] = word
    #list_phrase[position] = word # Addicionar Insert
    o_phrase = str.join(" ", list_phrase)
    return o_phrase

# Exc 5
def sum_discriminate(lista):
    nw_list1 = [ var[i] for var in lista[:] for i in (0,1)]     # Countries in every
                                                                # ...game
    nw_list2 = [ var[2][i] for var in lista[:] for i in (0,1)]  # Falls in every game
    countries = [ var for var in sorted(set(nw_list1))]         # All countries
#    print (countries)
    nw_list2 = zip(nw_list1, nw_list2)                          # List of tuples
                                                                # ...(country, falls)
    final_list1 = list(zip(countries, [0 for i in countries]))
    #final_list = zip(countries, [0]*len(countries))
    #print("final_list ",final_list)
    #print("final_list ",list(final_list))
    #final_list1 = list(final_list)[:]
    final_list = [list(tuple) for tuple in final_list1]
    #final_list1 = [tuple for tuple in list(final_list)]
    #for tuple in list(final_list):
        #print("entrou")
        #print(tuple)
    #final_list = list(final_list)
    ##print("final_list ",final_list)
    ##print("final_list1 ",final_list1)
    #print("final_list1 ",final_list1)
    #final_list = [ elm += var1[1] for var1 in nw_list2 for var2 in countries if var1[0] == var2[0]]
    #final_list.tolist()
    for var1 in nw_list2:
        for i, var2 in enumerate(countries):
#            print("var1[0]",var1[0])
#            print("var2",var2)
            if var1[0] in var2:
#                print (final_list[i][1])
#                print (final_list[i])
                final_list[i][1] += var1[1]
#                print("var1[1]",var1[1])
    for input in nw_list2:                      # Entra no for em py -2 mas nao em -3
        print ("input= ", input)
        
    return final_list
        
# Exc 6

def insert_sort(sorted_list, n):
    sorted_list.append(n)
    sorted_list.sort()

#    return list.sort(sorted_list)
    return sorted_list

# Exc 7

def insert_sort_des(sorted_list, n):
    sorted_list.append(n)
    sorted_list.sort(reverse = True)

#    return list.sort(sorted_list)
    return sorted_list
    
def insert_sort(sorted_list, n, decreacing = False):
    sorted_list.append(n)
    sorted_list.sort(reverse = decreacing)

#    return list.sort(sorted_list)
    return sorted_list
    
    
def bigger_than(decreacing_list, num):
    full_list = insert_sort_des(decreacing_list, num)
#    sub_list = [ elem if not elem == num break for elem in full_list]
#    sub_list = [ val = elem if not elem == num break for elem in full_list]
    sub_list = [ elem for elem in full_list if elem > num ]
    return sub_list

# Exc 8

def biggest_num(list):
    list.sort(reverse = True)
    return list[0]

# Exc 9
def upper_mean(qualif):
    sum = 0
    for note in qualif:
        sum += note
        
    mean = sum / len(qualif)
    upper_mean = bigger_than(qualif, mean)
    
    return mean, upper_mean

    
# Aula Pratica 9
# Exc 1
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
    
    # Aula pratica 6
    # Exc 1
    print (inv_phrase("eu gosto de chocolate"))
    # Exc 2
    print(alphabetic_sort("eu gosto de doce"))
    # Exc 3
    print (vowel_change("Levei meu cachorro para passear"))
    # Exc 4
    print (ins_word("Meu nome e ana", "ana", 1))
    print (ins_word("Meu nome e ana", "primeiro", 1))
    
    # Exc 5
    print (sum_discriminate([['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha',[5, 7]], ['Italia', 'Espanha', [7,8]]]))
    
    # Exc 6
    print (insert_sort([1,4,6,8,9], 7))
    
    # Exc 7
    print (insert_sort_des([1,4,6,8,9], 7))
    
    print (bigger_than([1,4,6,8,9], 7))
    
    # Exc 8
    
    print (biggest_num([1,4,6,8,9]))
    
    # Exc 9
    
    print (upper_mean([1,4,6,8,9]))

    
    """
    # Aula pratica 9
    # Exc 1
    lista = [9,8,4,5,1,9,8,6,4,8,9,2,3]
    print (lista)
    
    print (select_sort(lista))
    # Exc 2
    print (bubble_sort(lista))
    """
    
