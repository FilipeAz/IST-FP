#numero: 82468 nome: Filipe Azevedo.
#A funcao retira_ult retira o ultimo digito a string dada. retira_ult: str -> str
def retira_ult(x):
    x1 = x[:len(x)-1]
    return x1

#A funcao invert inverte a string dada. invert: str -> str
def invert(num):
    inv = ''
    for n in range(len(num)-1,-1,-1):
        i = eval(num[n])
        inv = str(inv) + str(i)
    return inv

#A funcao soma_pos_imp recebe uma string e duplica os digitos que se encontram em posicoes impares e subtrai 9 aos digitos em posicoes impares que depois de duplicados sejam maiores do que 9 e devolve a string com as respetivas modificacoes. soma_pos_imp: str -> str
def soma_pos_imp(x):
    soma = 0
    for i in range(len(x)):
        if i % 2 == 0:
            q = eval(x[i]) * 2 - 9
            if q < 0:
                soma = soma * 10 + (q + 9)
            elif q > 0:
                soma = soma * 10 + q
        else:
            soma = soma * 10 + eval(x[i])
    return soma
    
#A funcao calc_soma recebe uma cadeia de carateres, representando um numero de cartao, sem o ultimo digito e devolve a soma ponderada dos digitos de n, calculada de acordo com o algoritmo de Luhn. calc_soma: str -> int
def calc_soma(n):
    n = str(n)
    n = invert(n)
    n = soma_pos_imp(n)
    x = 0
    while n > 0:
        i = n % 10
        n = n // 10
        x = x + i
    return x

#A funcao luhn_verifica utiliza as funcoes acima descritas para verificar se a string dada satisfaz o algoritmo de luhn. luhn_verifica: str -> True/False
def luhn_verifica(x):
    r = eval(x[len(x)-1])
    x1 = retira_ult(x)
    x2 = calc_soma(x1)
    if (x2 + r) % 10 == 0:
        return True
    else:
        return False

#A funcao comeca_por devolve verdadeiro se a primeira string comeca pela segunda string
def comeca_por(cad1,cad2):
    return cad1[:len(cad2)] == cad2  

#A funcao comeca_por_um devolve verdadeiro se a a primeira string comecar por uma das strings do tuplo do segundo argumento.
def comeca_por_um(cad,t_cads):   
    for i in range(len(t_cads)):
        if comeca_por(cad,t_cads[i]):
            return True
    return False

#A funcao valida_iin devolve a abreviatura da rede emissora se o inicio da string dada for igual aos respetivos digitos iniciais do IIN e se tiver o respetivo comprimento. valida_iin: str/int -> str
def valida_iin(x):
    x = str(x)
    if comeca_por_um(x,('34','37')) == True and len(x) == 15:
        return 'American Express'
    elif comeca_por_um(x,('309','36','38','39')) == True and len(x) == 14:
        return 'Diners Club International'
    elif comeca_por_um(x,('65',)) == True and len(x) == 16:
        return 'Discover Card'
    elif comeca_por_um(x,('5018','5020','5038')) == True and (len(x) == 13 or len(x) == 19):
        return 'Maestro'
    elif comeca_por_um(x,('50','51','52','53','54','19')) == True and len(x) == 16:
        return 'Master Card'
    elif comeca_por_um(x,('4026','426','4405','4508')) == True and len(x) == 16:
        return 'Visa Electron'
    elif comeca_por_um(x,('4024','4532','4556')) == True and (len(x) == 13 or len(x) == 16):
        return 'Visa'
    else:
        return ''
    
#A funcao categoria define a categoria do emissor atraves da analise do primeiro digito da string dada. categoria: str/int -> str
def categoria(x):
    x = str(x)
    if eval(x[0]) == 1:
        return 'Companhias aereas'
    elif eval(x[0]) == 2:
        return 'Companhias aereas e outras tarefas futuras da industria'
    elif eval(x[0]) == 3:
        return 'Viagens e entretenimento e bancario / financeiro'
    elif eval(x[0]) == 4:
        return 'Servicos bancarios e financeiros'
    elif eval(x[0]) == 5:
        return 'Servicos bancarios e financeiros'
    elif eval(x[0]) == 6:
        return 'Merchandising e bancario / financeiro'
    elif eval(x[0]) == 7:
        return 'Petroleo e outras atribuicoes futuras da industria'
    elif eval(x[0]) == 8:
        return 'Saude, telecomunicacoes e outras atribuicoes futuras da industria'
    elif eval(x[0]) == 9:
        return 'Atribuicao nacional'
    else:
        return ''

#A funcao verifica_cc utiliza as funcoes acima definidas para verificar se uma string e um numero de cartao valido e, se for, devolve um tuplo com a categoria do emissor correspondente e a rede emissora correspondente. verifica_cc: int -> str
def verifica_cc(x):
    x = str(x)
    if isinstance(eval(x), int) == False:
        return 'cartao invalido'    
    if luhn_verifica(x) == True:
        if categoria(x) == '':
            return 'cartao invalido'
        elif valida_iin(x) == '':
            return 'cartao invalido'
        return (categoria(x), valida_iin(x))
    else:
        return 'cartao invalido'

from random import random
#As funcoes dois, tres, quatro e seis servem para escolher aleatoriamente um numero dentro de um tuplo com comprimento de 2, 3, 4 ou 6 respetivamente.    
def dois(t):
    q = int(random() *10)
    if 0 <= q <= 4:
        return t[0]
    else:
        return t[1]
    
def tres(t):
    q = int(random() * 10)
    while q == 0:
        q = int(random() * 10)
    if 1 <= q <= 3:
        return t[0]
    elif 4 <= q <= 6:
        return t[1] 
    else:
        return t[2]
    
def quatro(t):
    q = int(random() * 10)
    while 0 <= q <= 1:
        q = int(random() * 10)
    if 2 <= q <= 3:
        return t[0]
    elif 4 <= q <= 5:
        return t[1] 
    elif 6 <= q <= 7:
        return t[2]        
    else:
        return t[3]

def seis(t):
    q = int(random() * 10)
    while 6 <= q <= 9:
        q = int(random() * 10)
    if q == 0:
        return t[0]
    elif q == 1:
        return t[1]
    elif q == 2:
        return t[2]
    elif q == 3:
        return t[3]
    elif q == 4:
        return t[4]
    else:
        return t[5]
    
#A funcao rede utiliza as funcoes acima descritas para escolher aleatoriamente um dos possiveis digitos iniciais do IIN. rede: str -> str
def rede(x):
    if x == 'AE':
        i = ('34','37')
        return dois(i)
    elif x == 'DCI':
        i = ('309','36','38','39')
        return quatro(i)
    elif x == 'DC':
        return '65'
    elif x == 'M':
        i = ('5018','5020','5038')
        return tres(i)
    elif x == 'MC':
        i = ('50','51','52','53','54','19')
        return seis(i)
    elif x == 'VE':
        i = ('4026', '426', '4405', '4508')
        return quatro(i)
    elif x == 'V':
        i = ('4024', '4532', '4556')
        return tres(i)
    
#A funcao comp utiliza as funcoes acima descritas para escolher aleatoriamente um dos possiveis comprimentos que o numero de cartao de credito correspondente a uma dada emissora pode ter. comp: str -> int
def comp(x):
    if x == 'AE':
        return 15
    elif x == 'DCI':
        return 14
    elif x == 'DC' or x =='MC' or x == 'VE':
        return 16
    elif x == 'M':
        i = (13,19)
        return dois(i)
    elif x == 'V':
        i = (13,16)
        return dois(i) 

#A funcao gera_num utiliza as funcoes rede e comp acima definidas para gerar um numero aleatorio correspondente a uma rede emissora mas sem o ultimo digito (com menos um digito), que vai ser o digito de verificacao. gera_num: str -> str
def gera_num(x):
    soma = rede(x)
    c = comp(x)
    while len(soma) < c - 1:
        soma = soma + str(int(random() * 10))
    return soma
 
#A funcao digito_verificacao recebe uma string de um numero e calcula um digito que, adicionado ao fim do numero da string dada, faz com que este passe o algoritmo de luhn. digito_verificacao: str/int -> str
def digito_verificacao(x):
    x = calc_soma(x)
    if x % 10 == 0:
        return '0'
    else:
        return str(10 - (x % 10))
 
#A funcao gera_num_cc recebe uma string com uma abreviatura de uma rede emissora e, atraves das funcoes descritas acima, calcula um numero de cartao de credito valido aleatorio. gera_num_cc: str -> str
def gera_num_cc(n):
    x = gera_num(n)
    x1 = digito_verificacao(x)
    return x + x1

#Se usarmos o numero aletorio gerado pela funcao gera_um_cc como argumento da funcao verifica_cc, verifica-se que o tuplo resultante desta contem a categoria da rede emissora e o nome da rede emissora a que corresponde a abreviatura utilizada como argumento da gera_num_cc.