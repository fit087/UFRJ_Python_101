# Recibido de Anamaria Martins Moreira (amartinsmoreira@gmail.com)

# ex 1
# recebe dois strings a e b e devolve abba
# str, str -> str
# obs. essa funcao tb devolveria um resultado caso a e b fossem numeros...
def concatena(a,b):
    return a + b + b + a


# ex 2
# recebe o nome de uma pessoa (str) e sua idade (int) e devolve uma
# mensagem (str) contendo o nome e o numero da sorte.
# str, int -> str
def numeroSorte(nome,idade):
    x = idade*4
    x = x + 8
    x = x*60
    x = x/240
    x = x + 22
    x = x - idade
    return "Parabens " + nome + "! seu numero da sorte eh " + str(x) + "!"

# ex 3
# recebe duas strings e devolve a concatenacao da primeira sem seus primeiros 5
# caracteres  com a segunda sem seus ultimos 10 caracteres.
# ASSUME que ambas as strings possuem no minimo 15 caracteres
# observacao: isso eh o que diz a especificacao (o enunciado) - mas a funcao
# abaixo funciona em um conjunto maior de situacoes - QUAL?? E o que acontece
# em cada situacao??
# str, str -> str
def concatena2(string1,string2):
    return string1[5:] + string2[:-10]

# ex 4
# recebe uma string s, um caractere x e um indice i valido dessa string
# (i:0..tamanho de s - 1) e devolve uma string igual a s, excetuado o caracter
# do indice i, que deve ser substituido por x.
# pergunta 1: o que acontece se i = tamanho de s?
# pergunta 2: o que acontece se x tem mais de um caractere?
# str, str, int -> str
def subst(s,x,i):
    s = s[:i] + x + s[i+1:]
    return s

# ex 5
# recebe uma string e devolve essa string no meio dela mesma.
# str -> str
def insereMeio(s):
    meio = len(s)/2
    nova_s = s[:meio] + s + s[meio:]
    return nova_s

# ex 6
# recebe uma string e devolve essa string com uma tralha no inicio, meio e fim
# da string
# str -> str
def insereTralha(string):
    meio = len(string)/2
    nova_string = "#" + string[:meio] + "#" + string[meio:] + "#"
    return nova_string


# ex 7
# recebe uma string e devolve essa string rotacionada de 3 posicoes para a esquerda
# ASSUME que a string tem tamanho minimo = 3
# O que acontece se o tamanho for menor do que 3?
# str -> str
def rotaciona3Esq(palavra):
    nova_palavra = palavra[3:] + palavra[:3]
    return nova_palavra

# ex 8
# recebe uma string e um inteiro x e devolve essa string rotacionada de x
# posicoes para a esquerda
# ASSUME que a string tem tamanho minimo = x
# O que acontece se o tamanho for menor do que x?
# str, int -> str
def rotacionaXEsq(palavra,x):
    nova_palavra = palavra[x:] + palavra[:x]
    return nova_palavra

# ex 9
# recebe uma string e um inteiro x e devolve essa string rotacionada de x
# posicoes para a esquerda, mesmo que x seja maior do que o tamanho da string
# str, int -> str
def rotacionaXEsqGen(palavra,x):
    nova_palavra = palavra[x%len(palavra):] + palavra[:x%len(palavra)]
    return nova_palavra

# ex 10
# recebe duas datas no formato 'DD/MM/AAAA' (str) e calcula o numero de dias
# entre uma data e outra. Devolve a mensagem (str) "O total de dias eh <x>",
# onde <x> eh o valor calculado.
# ASSUME que a segunda data nao eh anterior a primeira, que todo mes tem 30
# dias e que um ano tem 365 dias 
# str, str -> str
def datas(data1,data2):
    dias1 = int(data1[:2]) + int(data1[3:5])*30 + (int(data1[6:])-1)*365
    dias2 = int(data2[:2]) + int(data2[3:5])*30 + (int(data2[6:])-1)*365
    total = dias2 - dias1
    return "O total de dias eh " + str(total)

