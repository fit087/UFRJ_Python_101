# -*- coding: cp1252 -*-
# 15/06/2015
# Aula Pratica 10
# Comp 1

# Escreva uma fun¸c˜ao que recebe uma lista e retorna uma nova lista sem
# elementos duplicados. Lembre que os elementos duplicados n˜ao precisam
# aparecer em posi¸c˜oes consecutivas. Dica: use um dicion´ario

# Exercise 1

# Using list
def list_wo_duplicates(lista):
    nw_list = []
    for i, elemento in enumerate(lista):
        if not elemento in lista[:i]:
            nw_list.append(elemento)
    return nw_list

# Dicas de colegas
# while list.count(lista1, elem)>1

# Using dictionary
def dict_wo_duplicates(lista):
    nw_dictionary ={}
    for elemento in lista:
        if not (dict.get(nw_dictionary,elemento)):
            nw_dictionary[elemento] = 1
        else:
            nw_dictionary[elemento] += 1
    return nw_dictionary

##l=len(lista)
##dicionario = {}
##for i in range(l):
##    dicionario[lista[i]] = lista[i]
##y = dict.values(dicionario)
##return y

# Exercise 2
def romanian_numbers(num):
    UNIDADES = { 0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI',
                 7: 'VII', 8: 'VIII', 9: 'IX' }
    DEZENAS = { 0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX',
                7: 'LXX', 8: 'LXXX', 9: 'XC' }
    CENTENAS = { 0: '', 2: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC',
                 7: 'DCC', 8:'DCCC', 9:'CM' } 
    num_list = []
    num_list.extend(str(num))
    ##if len(num_list) == 2:
    ##rom_num_list = DEZENAS[int(num_list)]
    lista = []
    i = -1
    for base in (UNIDADES, DEZENAS, CENTENAS):
        lista.append(base[int(num_list[i])])
        if abs(i) == len(num_list): break
        i -= 1
##        if abs(i) == len(num_list): break
    return ''.join(lista[::-1])

# dica
##if un in Unidades:
##    u = unidades[un]
##if dez in Dezenas:
##    d = DEZENAS[dez]
##if cen in CENTENA:
##    c = CENTENA[cen]


if __name__ == '__main__':
    # Exercise 1
    print([1,3,4,6,1,4,6,10])
    print(list_wo_duplicates([1,3,4,6,1,4,6,10]))
    print(dict_wo_duplicates([1,3,4,6,1,4,6,10]))

    # Exercise 2
    print(romanian_numbers(13))
    print(romanian_numbers(19))
    print(romanian_numbers(999))
