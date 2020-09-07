# ____Jogo 2048____

# Filipe Azevedo 82468
# Martim Zanatti 82517

# al040

from random import random


# ______________________________TAD Coordenada________________________________

def cria_coordenada(int1,int2):
    '''cria_coordenada: inteiros --> tuplo(int,int)
        A funcao cria_coordenada recebe como argumento um inteiro l e um inteiro c (entre 1 e 4) 
        e devolve um elemento do tipo coordenada correspondente a posicao (l, c)'''    
    if 0 < int1 < 5 and 0 < int2 < 5:
        return (int1,int2)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')
    
def coordenada_linha(coordenada):
    '''coordenada_linha: tuplo(int,int) --> int 
       A funcao coordenada_linha recebe como argumento um elemento do tipo coordenada e devolve a linha respetiva.'''    
    return coordenada[0]

def coordenada_coluna(coordenada):
    ''' coordenada_coluna: tuplo(int,int) --> int
        A funcao coordenada_coluna recebe como argumento um elemento do tipo coordenada e devolve a coluna respetiva.'''    
    return coordenada[1]

def e_coordenada(arg):
    '''e_coordenada: universal --> True/False
        A funcao e_coordenada recebe um unico argumento e devolve True caso esse argumento seja do tipo coordenada, e False em caso contrario'''    
    if isinstance(arg, tuple) and len(arg) == 2:
        if 0 < arg[0] < 5 and 0 < arg[1] < 5:
            return True
        else:
            return False
    else:
        return False
    
def coordenadas_iguais(c1,c2):
    ''' coordenadas_iguais: tuplo(int,int) tuplo(int,int) --> True/False
        A funcao coordenadas_iguais recebe como argumentos dois elementos do tipo coordenada e devolve True caso esses argumentos correspondam a mesma posicao (l, c) do tabuleiro, e False em caso contrario.'''    
    if e_coordenada(c1) and e_coordenada(c2):
        return c1 == c2
    else:
        return False
    
#  _____________________________TAD Tabuleiro_________________________________
    
def cria_tabuleiro():
    '''cria_tabuleiro: {} --> tabuleiro
        A funcao cria_tabuleiro devolve um elemento do tipo tabuleiro com as posicoes todas vazias de acordo com a representacao interna escolhida.'''    
    t = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],0]
    return t

def tabuleiro_posicao(t,pos):
    '''tabuleiro_posicao: tabuleiro tuplo(int,int) --> int
        A funcao tabuleiro_posicao recebe como argumentos um elemento t do tipo tabuleiro e um elemento c do tipo coordenada e devolve um elemento do tipo inteiro, que corresponde ao valor na posicao do tabuleiro correspondente a coordenada c, gerando um ValueError no caso do segundo argumento (coordenada) nao ser valido'''    
    if e_coordenada(pos) == False:
        raise ValueError('tabuleiro_posicao: argumentos invalidos')
    else:
        for l in range(1,5):
            for c in range(1,5):
                if coordenadas_iguais(cria_coordenada(l,c), pos):
                    return t[coordenada_linha(pos)-1][coordenada_coluna(pos)-1]
                
def tabuleiro_pontuacao(t):
    '''tabuleiro_pontuacao: tabuleiro --> int
        A funcao tabuleiro_pontuacao recebe como argumento um elemento t do tipo tabuleiro e devolve a pontuacao atual do tabuleiro dado.'''    
    return t[4]

def tabuleiro_posicoes_vazias(t):
    '''tabuleiro_posicoes_vazias: tabuleiro --> lista
        A funcao tabuleiro_posicoes_vazias recebe como argumento um elemento t do tipo tabuleiro devolve uma lista contendo as coordenadas de todas as posicoes vazias do mesmo tabuleiro.'''    
    lista = []
    for l in range(1,5):
        for c in range(1,5):
            pos = cria_coordenada(l,c)
            if e_coordenada(pos) and tabuleiro_posicao(t,pos) == 0:
                lista = lista + [pos]
    return lista

def tabuleiro_preenche_posicao(t,pos,v):
    ''' tabuleiro_preenche_posicao: tabuleiro tuplo(int,int) int -->  tabuleiro
        Este modificador recebe como argumentos um elemento t do tipo tabuleiro, um elemento c do tipo coordenada e um inteiro v, e modifica o tabuleiro t, colocando o valor v na posição correspondente à coordenada c. A função deve devolver o tabuleiro modificado.'''    
    if e_coordenada(pos) and isinstance(v,int):
        for l in range(1,5):
            for c in range(1,5):
                coord = cria_coordenada(l,c)
                if coordenadas_iguais(coord,pos):
                    t[coordenada_linha(pos)- 1][coordenada_coluna(pos)-1] = v  
        return t
    else:
        raise ValueError('tabuleiro_preenche_posicao: argumentos invalidos')
    

def tabuleiro_actualiza_pontuacao(t,v):
    '''tabuleiro_actualiza_pontuacao: tabuleiro int --> tabuleiro
        A funcao tabuleiro_atualiza_pontuacao recebe como argumentos um elemento t do tipo tabuleiro e um inteiro v, nao negativo e multiplo de 4 (no caso de nao o ser, gera um ValueError). Modifica o tabuleiro t, acrescentando ao valor da respectiva pontuacao v pontos, devolvendo o tabuleiro modificado.'''    
    if v % 4 != 0 or v < 0:
        raise ValueError('tabuleiro_actualiza_pontuacao: argumentos invalidos')
    else:
        t[4] = t[4] + v
    return t


def tabuleiro_reduz(t,d):
    ''' tabuleiro_reduz: tabuleiro, string --> tabuleiro
        A funcao tabuleiro_reduz recebe como argumento um elemento t do tipo tabuleiro e uma cadeia de caracteres d correspondente a uma das 4 acoes possiveis. Em particular d devera ser uma das cadeias de caracteres 'N', 'S', 'W', 'E'. A funcao modifica o tabuleiro t, reduzindo-o na direcao d de acordo com as regras do jogo 2048, devolvendo o tabuleiro t modificado, incluindo a atualizacao da pontuacao. Deve ainda verificar se d e uma jogada gerando um ValueError em caso contrario'''    
    if d == 'N':
        for c in (0,1,2,3):
            i = 1
            for l in (0,1,2,3):
                if tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) != 0:
                    tabuleiro_preenche_posicao(t,cria_coordenada(i,c+1),tabuleiro_posicao(t,cria_coordenada(l+1,c+1)))
                    if coordenadas_iguais(cria_coordenada(l+1,c+1),cria_coordenada(i,c+1)) == False:
                        tabuleiro_preenche_posicao(t,cria_coordenada(l+1,c+1),0)
                    i = i + 1
            i = 1
            for l in (0,1,2):
                x = l + 2
                if tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) == tabuleiro_posicao(t,cria_coordenada(l+2,c+1)) and tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) != 0:
                    tabuleiro_preenche_posicao(t,cria_coordenada(l+1,c+1),tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) + tabuleiro_posicao(t,cria_coordenada(l+2,c+1)))
                    tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t,cria_coordenada(l+1,c+1)))
                    while x < 5:
                        if x + 1 < 5:
                            tabuleiro_preenche_posicao(t,cria_coordenada(x,c+1),tabuleiro_posicao(t,cria_coordenada(x+1,c+1)))
                        else:
                            tabuleiro_preenche_posicao(t,cria_coordenada(4,c+1),0)
                        x = x + 1
        return t    
    elif d == 'S':
        for c in (0,1,2,3):
            i = 4
            for l in (3,2,1,0):     
                if tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) != 0:
                    tabuleiro_preenche_posicao(t,cria_coordenada(i,c+1),tabuleiro_posicao(t,cria_coordenada(l+1,c+1)))
                    if coordenadas_iguais(cria_coordenada(l+1,c+1),cria_coordenada(i,c+1)) == False:
                        tabuleiro_preenche_posicao(t,cria_coordenada(l+1,c+1),0)
                    i = i - 1
            i = 4
            for l in (3,2,1):
                x = l
                if tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) == tabuleiro_posicao(t,cria_coordenada(l,c+1)) and tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) != 0:
                    tabuleiro_preenche_posicao(t,cria_coordenada(l+1,c+1),tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) + tabuleiro_posicao(t,cria_coordenada(l,c+1)))
                    tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t,cria_coordenada(l+1,c+1)))
                    while x > 0:
                        if x - 1 > 0:
                            tabuleiro_preenche_posicao(t,cria_coordenada(x,c+1),tabuleiro_posicao(t,cria_coordenada(x-1,c+1)))
                        else:
                            tabuleiro_preenche_posicao(t,cria_coordenada(1,c+1),0)
                        x = x - 1
        return t                   
    elif d == 'W':
        for l in (0,1,2,3):
            i = 1
            for c in (0,1,2,3):     
                if tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) != 0:
                    tabuleiro_preenche_posicao(t,cria_coordenada(l+1,i),tabuleiro_posicao(t,cria_coordenada(l+1,c+1)))
                    if coordenadas_iguais(cria_coordenada(l+1,c+1),cria_coordenada(l+1,i)) == False:
                        tabuleiro_preenche_posicao(t,cria_coordenada(l+1,c+1),0)
                    i = i + 1
            i = 1
            for c in (0,1,2):
                x = c + 2
                if tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) == tabuleiro_posicao(t,cria_coordenada(l+1,c+2)) and tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) != 0:
                    tabuleiro_preenche_posicao(t,cria_coordenada(l+1,c+1),tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) + tabuleiro_posicao(t,cria_coordenada(l+1,c+2)))
                    tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t,cria_coordenada(l+1,c+1)))
                    while x < 5:
                        if x + 1 < 5:
                            tabuleiro_preenche_posicao(t,cria_coordenada(l+1,x),tabuleiro_posicao(t,cria_coordenada(l+1,x+1)))
                        else:
                            tabuleiro_preenche_posicao(t,cria_coordenada(l+1,4),0)
                        x = x + 1
        return t   
    elif d == 'E':
        for l in (0,1,2,3):
            i = 4
            for c in (3,2,1,0):     
                if tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) != 0:
                    tabuleiro_preenche_posicao(t,cria_coordenada(l+1,i),tabuleiro_posicao(t,cria_coordenada(l+1,c+1)))
                    if coordenadas_iguais(cria_coordenada(l+1,c+1),cria_coordenada(l+1,i)) == False:
                        tabuleiro_preenche_posicao(t,cria_coordenada(l+1,c+1),0)
                    i = i - 1
            i = 4
            for c in (3,2,1):
                x = c
                if tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) == tabuleiro_posicao(t,cria_coordenada(l+1,c)) and tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) != 0:
                    tabuleiro_preenche_posicao(t,cria_coordenada(l+1,c+1),tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) + tabuleiro_posicao(t,cria_coordenada(l+1,c)))
                    tabuleiro_actualiza_pontuacao(t,tabuleiro_posicao(t,cria_coordenada(l+1,c+1)))
                    while x > 0:
                        if x - 1 > 0:
                            tabuleiro_preenche_posicao(t,cria_coordenada(l+1,x),tabuleiro_posicao(t,cria_coordenada(l+1,x-1)))
                        else:
                            tabuleiro_preenche_posicao(t,cria_coordenada(l+1,1),0)
                        x = x - 1
        return t                    
    else:
        raise ValueError('tabuleiro_reduz: argumentos invalidos')
                      
                      
    
    
                      

def e_tabuleiro(x):
    ''' e_tabuleiro: universal --> True/False
        A funcao e_tabuleiro recebe um unico argumento, devolvendo True se o seu argumento for do tipo tabuleiro, e False em caso contrario.'''    
    if isinstance(x,list) and len(x) == 5 and isinstance(x[4],int) and x[4] >= 0:
        for i in range(4):
            if not isinstance(x[i], list) or not len(x[i]) == 4:
                return False
            for l in range(4):
                if  not isinstance(x[i][l], int) or x[i][l] < 0:
                    return False
                     
        return True         
    else:
        return False               
                    
            
       
   

def tabuleiro_terminado(t):
    ''' tabuleiro_terminado: tabuleiro --> True/False
    A funcao tabuleiro_terminado recebe como argumento um elemento t do tipo tabuleiro e devolve True caso o tabuleiro t esteja terminado, ou seja, caso esteja cheio e nao existam movimentos possiveis, e False em caso contrario.'''
    J = ('N','S','W','E')
    for i in J:
        if not tabuleiros_iguais(t,tabuleiro_reduz(copia_tabuleiro(t),i)):
            return False
    return True    
        
        

def tabuleiros_iguais(t1,t2):
    ''' tabuleiro_iguais: tabuleiro tabuleiro --> True/False
    A funcao tabuleiros_iguais recebe como argumentos dois elementos t1 e t2 do tipo tabuleiro e devolve True caso t1 e t2 correspondam a dois tabuleiros com a mesma configuracao e pontuacao, e False em caso contrario.'''
    return t1 == t2

         
def escreve_tabuleiro(t):
    ''' escreve_tabuleiro: tabuleiro --> {}
    A funcao escreve_tabuleiro recebe como argumento um elemento t do tipo tabuleiro e escreve para o ecra a representacao externa de um tabuleiro de 2048. Deve ainda verificar se t e um tabuleiro valido,gerando um ValueError em caso contrario.'''
    x = 1
    if e_tabuleiro(t):
        for l in range(1,5):
            x = 1
            for c in range(1,5):
                coord = cria_coordenada(l,c)
                pos = tabuleiro_posicao(t, coord)
                if x == 4:
                    print('[', pos, '] ')
                else:
                    print('[', pos, ']', end = ' ')
                x = x + 1  
        print('Pontuacao:', tabuleiro_pontuacao(t))
    else:
        raise ValueError('escreve_tabuleiro: argumentos invalidos')
    
    
def copia_tabuleiro(t):
    ''' copia_tabuleiro: tabuleiro --> tabuleiro 
    copia_tabuleiro recebe um tabuleiro e devolve uma copia do mesmo tabuleiro''' 
    if not e_tabuleiro(t):
        raise ValueError('copia_tabuleiro: argumentos invalidos')
    else:
        T = cria_tabuleiro()
        T[4] = t[4] 
        for l in range(1,5):
            for c in range(1,5):
                coord = cria_coordenada(l,c)
                pos = tabuleiro_posicao(t,coord)
                tabuleiro_preenche_posicao(T,coord,pos)
        return T

def preenche_posicao_aleatoria(t):
    ''' preenche_posicao_aleatoria: tabuleiro --> tabuleiro
    A funcao preenche_posicao_aleatoria recebe um elemento tipo tabuleiro e preenche uma posicao livre escolhida aleatoriamente com um dos numeros (2 ou 4)  e devolve o tabuleiro modificado''' 
    v = int(random() * 10)
    if 0 <= v <= 1:
        novo = 4
    else:
        novo = 2
    coor = cria_coordenada(int(random() * 4) + 1,int(random() * 4) + 1)
    pos = tabuleiro_posicao(t,coor)
    while pos != 0:
        coor = cria_coordenada(int(random() * 4) + 1,int(random() * 4) + 1)    
        pos = tabuleiro_posicao(t,coor)
    return tabuleiro_preenche_posicao(t,coor,novo)
        


# _______________________Pede Jogada_________________________________________  


def pede_jogada():
    ''' pede_jogada: {} --> tabuleiro
    Esta funcao nao recebe qualquer argumento, limitando-se a pedir ao utilizador para introduzir uma direcao (N, S, E ou W). Caso o valor introduzido pelo utilizador seja invalido, a funcao deve pedir novamente a informacao de jogada ao utilizador. A funcao devolve uma cadeia de caracteres correspondente a direcao escolhida pelo utilizador.'''
    d = ['N','S','W','E']
    j = input('Introduza uma jogada (N, S, E, W): ')
    while j not in d:
        print('Jogada invalida.')
        j = input('Introduza uma jogada (N, S, E, W): ')
    return j     

# _______________________Jogo 2048__________________________________________


def jogo_2048():
    ''' jogo_2048: {} --> {}
    Esta função corresponde à função principal do jogo. Não recebe qualquer argu-
    mento, e permite a um utilizador jogar um jogo completo de 2048.'''
    t = cria_tabuleiro()
    preenche_posicao_aleatoria(t)
    preenche_posicao_aleatoria(t)
    escreve_tabuleiro(t)
    while tabuleiro_terminado(t) == False:
        j = pede_jogada()
        A = copia_tabuleiro(t)
        A = tabuleiro_reduz(A,j)
        if tabuleiros_iguais(t,A):
            escreve_tabuleiro(t)
        elif tabuleiros_iguais(t,A) == False:
            t = tabuleiro_reduz(t,j)
            preenche_posicao_aleatoria(t)
            escreve_tabuleiro(t)
    print('Jogo Terminado')
    
                    
        
    
    

