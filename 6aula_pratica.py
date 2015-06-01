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
    nw_list1 = [ var[i] for var in lista[:] for i in (0,1)]
    nw_list2 = [ var[2][i] for var in lista[:] for i in (0,1)]
    countries = [ var for var in sorted(set(nw_list1))]
    nw_list2 = zip(nw_list1, nw_list2)
    final_list = zip(countries, [0 for i in countries])
    #final_list = [ elm += var1[1] for var1 in nw_list2 for var2 in countries if var1[0] == var2[0]]
    #final_list.tolist()
    for var1 in nw_list2:
        for i, var2 in enumerate(countries):
            print("var1[0]",var1[0])
            print("var2",var2)
            if var1[0] in var2:
                print (final_list[i][1])
                final_list[i][1] += var1[1]
                print("var1[1]",var1[1])
    for input in nw_list2:
        print ("input= ", input)
        
    return final_list
        
    
        
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
    
    # Aula pratica 9
    # Exc 1
    lista = [9,8,4,5,1,9,8,6,4,8,9,2,3]
    print (lista)
    
    print (select_sort(lista))
    # Exc 2
    print (bubble_sort(lista))
    
    
