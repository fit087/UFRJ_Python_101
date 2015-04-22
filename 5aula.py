# 22/04/2015
# 5 aula pratica

# Exercise 1
def conta_palavras(frase):
    """
    Faca uma funcao que dada uma frase, retorne o numero de palavras da frase. 
    Considere que a frase pode ter espacos no inicio e no final.
    """
    #frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)

# Exercise 2
def retirar(frase, palavra, pos1, pos2):
    """
    Faca uma funcao que dada uma frase, uma palavra, e duas posicoes,
    retorna a frase excluindo-se as ocorrencias desta palavra entre estas duas 
    posicoes, inclusive
    """
    index = str.find(frase, palavra, pos1, pos2)
    size = len(palavra)
    
    if (not index == -1) and (pos1 + index + size < pos2):
        pos2 -= index + size - 1
        #pos2 = pos2 - index - size + 1
        return frase[:index] + retirar(frase[index + size:], palavra, 0, pos2)
    else:
        return frase[:index] + frase[index + size:]

# Exercise 3
def substituir_espaco(frase):
    """
    Faca uma funcao que dada uma frase, substitua todos os espacos em branco por ”#”,
    so que sem usar a funcao replace.
    """
    frase = str.split(frase, " ")
    frase = str.join("#", frase)
    return frase

# Exercise 4
def apos_chr(frase, caracter):
    """
    Escreva uma funcao que tenha dois parametros, uma string e um caractere,
    e retorne apenas o trecho da string situado entre a primeira ocorrencia do
    caractere ate o final da string. Por exemplo, se a entrada for ”abcabc” e
    ”a”, a sa´ıda deve ser ”bcabc”.
    """
    index = str.find(frase, caracter, 0, len(frase))
    return frase[index + len(caracter):]

# Exercise 5
def separar_tipos(tupla, elem = 0):
    """
    Faca uma funcao que receba uma tupla de tres elementos como parametro,
    e retorne duas tuplas, sendo que a primeira deve conter apenas os elementos
    da tupla de entrada que forem do tipo string, e a segunda os elementos da 
    tupla de entrada que sejam dos tipos inteiro, float ou complex.
    """
    if type(tupla[elem])==str:pass
        

# Exercise 6
def intercalando_listas(lista1, lista2):
    return zip(lista1, lista2)

if __name__ == '__main__':
    print ("Exc1 conta_palavras ", conta_palavras("  hola Susana te estamos llamando queremos jugar  "))
    print ("Exc2 retirar ", retirar("Hola Susana te estamos llamando queremos llamando", " llamando", 10, 48))
    print ("Exc3 substituir ", substituir_espaco("Hola Susana te estamos llamando queremos llamando"))
    print ("Exc4 apos_chr ", apos_chr("Hola Susana te estamos llamando queremos llamando", "na"))
    print ("Exc6 intercalando_listas ", intercalando_listas([1,3,5], [2,4,6]))