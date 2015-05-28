# -*- coding: utf-8 -*-
# 26/05/2015
# Comp 1. Manipulacao de listas


#def alteraLista(lista):
#    progresso = [[]]*11
    #progresso = [[]*11]
    #progresso = []*11
    #progresso = []
#    progresso[0] = lista [:]
#    list.append(lista,10)
#    progresso[1]= lista [:]
#    list.append(lista,[3,'bola'])
#    progresso[2]= lista [:]
#    list.append(lista,'lua')
#    progresso[3]=  lista [:]
#    list.extend(lista,[1,2,3])
#    progresso[4]=  lista [:]
#    list.extend(lista,'lua')
#    progresso[5]=  lista [:]
#    del lista[2]
#    progresso[6]=  lista [:]
#    list.insert(lista,2,1)
#    progresso[7]=  lista [:]
#    list.remove(lista,2)
#    progresso[8]=  lista [:]
#    elemento = list.pop(lista,3)
#    progresso[9]=  lista [:]
#    list.insert(lista,1,elemento)
#    progresso[10]=  lista [:]
#    return lista, progresso
    
def alteraLista(lista):
    progresso = [[]]*11
    #progresso = [[]*11]
    #progresso = []*11
    #progresso = []
    progresso += lista [:]
    list.append(lista,10)
    progresso += lista [:]
    list.append(lista,[3,'bola'])
    progresso += lista [:]
    list.append(lista,'lua')
    progresso +=  lista [:]
    list.extend(lista,[1,2,3])
    progresso +=  lista [:]
    list.extend(lista,'lua')
    progresso +=  lista [:]
    del lista[2]
    progresso +=  lista [:]
    list.insert(lista,2,1)
    progresso +=  lista [:]
    list.remove(lista,2)
    progresso +=  lista [:]
    elemento = list.pop(lista,3)
    progresso +=  lista [:]
    list.insert(lista,1,elemento)
    progresso +=  lista [:]
    return lista, progresso
    
# Para o del  ́e preciso indicar o  ́ındice do elemento da lista que se deseja deletar:
# del lista[3]
# Enquanto que para o remove basta indicar o elemento a ser deletado:
# list.remove(lista, 1)
    
def main():
    lista = [4,5]
    print (lista)
    print (alteraLista(lista))
    
    
if __name__ == '__main__':
    main()
#    lista = [4,5]
#    print lista
#    print (alteraLista(lista))
 