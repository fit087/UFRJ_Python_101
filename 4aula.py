# -*- coding: UTF-8 -*-
# 13/04/2015
# Aula 4
"""
Created on Mon Apr 13 10:53:32 2015
    4a aula pratica de Computacao 1 na UFRJ.
    Professor: Anamaria Martins Moreira (amartinsmoreira@gmail.com)
    Topic: Strings
@author: Adolfo Correa (fit087@gmail.com)
"""
# Exercicio 1

# Func˜ao que receba duas strings a e b, e retorne a concatena¸
# c˜ao delas no formato abba.

def concatenar(string1, string2):
    return str(string1) + str(string2) + str(string2) + str(string1)

# Exercicio 2

# numero da sorte

def number_luck(age, nome):
    aux = age * 4 + 8
    aux *= 60
    aux /= 240
    aux += 22
    aux -= age
    return "PARABENS " + nome + "! " + aux + " e seu numero da sorte."

# Exercicio 3

# Escreva uma fun¸c˜ao que receba duas strings de no m´ınimo 15 caracteres e
# retorne a concatena¸c˜ao da primeira, sem os cinco primeiros caracteres,
# com a segunda, sem os ´ultimos dez caracteres.

def ex3_concatena(str1, str2):
    return str1[5:] + str2[:-10]

# Exercicio 4

# Escreva uma fun¸c˜ao que receba uma string s, um caractere x e um n´umero
# inteiro i entre 0 e o comprimento da string, e retorne uma string igual a s,
# exceto que o elemento da posi¸c˜ao i deve ser substitu´ıdo pelo caractere x.

def text_char(str1, x, i):
    str1[i] = x
    return str1
   # return str1[0:i] + x + str1[i + 1:]

# Exercicio 5

# Escreva uma fun¸c˜ao que receba uma string e retorne essa string no meio
# dela mesma. Por exemplo, ao receber a string ”abcd”, a fun¸c˜ao deve retornar
# ”ababcdcd”. Outro exemplo: se receber ”abcde”, a fun¸c˜ao deve retornar
# ”ababcdecde”

def text_text(text):
   #text = text[:len(text) // 2] + text + text[-(len(text) // 2 + 1):]
   text = text[:len(text) // 2] + text + text[len(text) // 2:]
   return text

# Exercicio 6

# Escreva uma fun¸c˜ao que receba uma string e insira o caractere ”#”
# no in´ıcio, no meio e no final dela. Por exemplo, se a entrada for ”abcd”,
# a sa´ıda deve ser ”#ab#cd#”. Outro exemplo: se receber ”abcde”,
# a fun¸c˜ao deve retornar ”#ab#cde#”.

def ex6_hashtag(str1):
    #pre = str1[:len(str1)//2]
    #pos = str1[len(str1)//2:]
    #str1 = "#" + pre + "#" + pos + "#"
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    return str1

# Exercicio 7

# Escreva uma fun¸c˜ao que receba uma string e a rotacione 3 posi¸c˜oes para
# a esquerda. Por exemplo, se a entrada for ”abcdef ”, a fun¸c˜ao deve
# retornar ”defabc”. Assuma que a string passada tem no m´ınimo 3 caracteres.

def ex7_rotation(str1):
    i = len(str1)//2
    aux = str1[:i]
    str1[:i] = str1[i:]
    str1[i:] = aux
    return str2

# Exercicio 8

# Escreva uma fun¸c˜ao que receba uma string e um n´umero inteiro x e rotacione
# a string x posi¸c˜oes para a esquerda. Assuma que a string tem pelo menos x
# caracteres.

# Exercicio 9

# Escreva uma fun¸c˜ao similar `a anterior, s´o que agora considere que a
# string passada pode ter qualquer tamanho, inclusive menor que x.

# Exercicio 10

# Escreva uma fun¸c˜ao que receba duas datas no formato ”DD/MM/AAAA”,
# sendo a segunda maior que a primeira, e calcule o total de dias passados
# entre uma data e outra. A frase retornada deve ser ”O total de dias ´e x ”,
# onde x ´e o total achado. Considere que todo mˆes tem 30 dias. E que o ano
# tem 365 dias.
# Exemplo: Se as datas s˜ao ”02/03/1982” e ”01/02/1983”, o total de dias ´e 334.


       
if __name__ == '__main__':
    print ("\n\n\n********************************")
    print ("\t4a Aula. Strings")
    print ("********************************\n")
    
    print ("Ex1", concatenar(" Ola. ", ",a todos"))
    print ("Ex5", text_text("abcd"))
    print ("Ex5", text_text("abcde"))
    print ("Ex6", ex6_hashtag("abcd"))
    print ("Ex6", ex6_hashtag("abcde"))
    print ("Ex7", ex7_rotation("abcd"))
    print ("Ex7", ex7_rotation("abcde"))
    

