
# A funcao anos eh uma funcao constante que calcula e retorna em quantos anos
# a populacao
# de um pais com populacao inicial de 80mil habitantes e taxa de crescimento
# anual de 3% alcanca ou ultrapassa a de um pais com populacao inicial de 200mil
# e taxa de crescimento anual de 1,5%. O retorno eh um numero inteiro.
# -> int

def anos ():
    pA = 80000
    pB = 200000
    tA = 1.03
    tB = 1.015
    n = 0
    while pA < pB:
        pA = int(pA * tA)
        pB = int(pB * tB)
        n = n + 1
    return n

# OBS: como eh uma funcao constante, nao temos como variar os dados para testar
# situacoes variadas
        

# A funcao anos eh uma funcao que calcula e retorna em quantos anos
# a populacao  de um pais A alcanca ou ultrapassa a de um pais B
# dados a populacao inicial de A e de B e a taxa de crescimento de A e de B,
# nessa ordem.
# A funcao assume que a taxa de crescimento de A eh maior do que a de B ou que
# a populacao inicial de A ja eh maior do que a de B.
# O retorno eh um numero inteiro.
# int, int, float, float -> int


def anos (pA,pB,tA, tB):
    n = 0
    while pA < pB:
        pA = int(pA * (1 + tA))
        pB = int(pB * (1 + tB))
        n = n + 1
    return n

# alguns testes
anos(80000,200000,0.03,0.015) # 63
anos(10,1,.3,.05) # 0
anos(10,100,1,0) # 4
anos(10,100,1,0.01) # 4

# situacao eliminada nos comentarios
# anos(10,100,.01,0.1) # laco infinito
# na realidade o Python para e devolve algo, se nao tiver o cast para int
# (71102, inf, inf), (n, pA, pB)


# A funcao anos2 eh uma funcao que calcula e retorna em quantos anos
# a populacao  de um pais A alcanca ou ultrapassa a de um pais B
# dados a populacao inicial de A e de B e a taxa de crescimento de A e de B,
# nessa ordem.
# Caso nao seja possivel para o pais A alcancar o pais B com os dados
# apresentados (taxa de crescimento de A eh menor do que a de B e
# a populacao inicial de A eh menor ou igual a de B), devolve "nunca". 
# O retorno eh um numero inteiro ou a string "nunca".
# int, int, float, float -> int ou str

def anos2 (pA,pB,tA, tB):
    n = 0
    if pA < pB and tA <= tB:
        return "nunca"
    while pA < pB:      # obs. o else aqui eh implicito por causa do return
        pA = int(pA * (1 + tA))
        pB = int(pB * (1 + tB))
        n = n + 1
    return n



from random import randint

# jogadas devolve o numero de vezes (um int) que em que foram sorteados
# dois numeros de 1 a 6 ate que saissem 2 numeros iguais.
# OBS 1. apesar de nao ter parametros de entrada, jogada nao eh uma funcao
# constante
# OBS 2 - em teoria, o resultado poderia tambem ser long, se demorasse MUITO
# para que dois numeros iguais saissem, mas essa probabilidade eh zero, na
# pratica
# -> int 

def jogadas():
    d1 = randint(1,6)
    d2 = randint(1,6)
    n = 1
    while d1 != d2:
        d1 = randint(1,6)
        d2 = randint(1,6)
        n = n + 1
    return n

#     
# posLetra recebe como entrada uma string, uma letra, e um inteiro que
# indica a ocorrencia desejada da letra (1 para primeira ocorrencia, 2 para
# segunda, etc) e retorna em que posicao da string aquela ocorrencia da letra
# esta. Caso existam menos ocorrencias da letra do que a ocorrencia pedida,
# devolve uma mensagem.
# str, str, int -> int ou str

def posLetra(frase,letra,ocorrencia):
    i = 0
    nocs = 0
    while i<len(frase) and nocs<ocorrencia:
        if frase[i] == letra:
            nocs = nocs +1
        i = i + 1
    if nocs < ocorrencia:
        return "so foram encontradas "+str(nocs)+" ocorrencias de "+str(letra)
    else:
        return i-1

# alguns testes
posLetra("mariana come banana",'a',3) # 6
posLetra("mariana come banana",'z',3) # 'so foram encontradas 0 ocorrencias de z'
posLetra("mariana come banana",'a',1) # 1
posLetra("mariana come banana",'a',6) # 18
posLetra("mariana come banana",'a',7) # 'so foram encontradas 6 ocorrencias de a'
posLetra("mariana come banana",'m',1) # 0    
posLetra("",'a',3) # 'so foram encontradas 0 ocorrencias de a'

# fib espera receber um inteiro nao negativo n e devolve um inteiro nao negativo,
# correspondente ao n+1-esimo numero da sequencia
# int -> int
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
    
# soma_fib espera receber um inteiro nao negativo e devolve um inteiro nao
# negativo, correspondente a soma dos n primeiros termos da sequencia de
# fibonacci
# int -> int
def soma_fib (n):
    soma = 0
    i = 0
    while i < n:
        soma = soma + fib(i)
        i = i+1
    return soma

# alguns testes
soma_fib(0) # 0
soma_fib(1) # 0
soma_fib(2) # 1
soma_fib(3) # 2
soma_fib(4) # 4

# fat espera receber um inteiro nao negativo e devolve o fatorial desse numero
# int -> int
def fat(n):
    if n == 0:
        return 1
    else:
        return n*fat(n-1)
fat(0) # 1
fat(1) # 1
fat(2) # 2
fat(3) # 6
fat(5) # 120
fat(10) # 3628800


# ou, com while
# fat2 espera receber um inteiro nao negativo e devolve o fatorial desse numero
# int -> int

def fat2(n):
    if n == 0:
        return 1
    res = n
    while n > 2:
        n = n - 1 
        res = res * n
    return res

fat2(0) # 1
fat2(1) # 1
fat2(2) # 2
fat2(3) # 6
fat2(5) # 120
fat2(10) # 3628800

# OBS. existe diferenca de comportamento entre fat e fat2 no caso da entrada
# ser negativa, mas isso nao tem importancia pois esta fora do dominio
# de definicao das duas



# primo espera receber um inteiro positivo e devolve True, caso
# esse numero seja primo e False, caso contrario.
# int -> boolean

def primo(n):
    d = int(n/2)    # o int so eh necessario em Python 3
    res = True
    while res and d > 1:
        if  n%d == 0:
            res = False
        d = d -1
    return res


primo(1) # True
primo(2) # True
primo(3) # True
primo(4) # False
primo(11) # True
primo(111) # False

# !!!!! Atencao !!! o zero na frente diz que o numero esta em octal, mas ainda
# assim eh int. Para humanos o zero na frente eh desprezivel, para Python, nao.
primo(0111) # True   


    



    

        
        
        
        

    
    
 
        
