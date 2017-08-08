import random
#O módulo random gera números aleatórios.

palavras = []
#Essas são as palavras que vão ser sorteadas para o jogo da forca.
letrasErradas = ''
#Aqui vai fazer o armazenamento das letras erradas digitadas pelo jogador.
letrasCertas = ''
#Aqui vai fazer o armazenamento das letras certas digitadas pelo jogador.
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#Esses desenhos servem mais para a estética do jogo, mas a cada letra errada
#vai adicionando uma cabeça, perna, etc ao corpo do bonequinho. Quando o corpo
#estiver completo significa que o jogador perdeu.


#Função que recebe as palavras para serem sorteadas.
def receberPalavras():
    global palavras
    while True:
        p= input('Digite uma palavra para ser sorteada: ')
        if p == '':
            break
        palavras.append(p)



def principal():
#O comando def define uma função onde terá uma série de comandos, que no caso
#foi chamada de principal.

    """
    Função Princial do programa
    """
    print('F O R C A')
#print serve para imprimir determinado conteúdo na tela. 

    receberPalavras()
    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True:
#(while = enquanto)Enquanto o que estiver dentro do comando while for verdade,
#esse comando continuará repetindo, ou seja estará em loop.
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            print('Voce Perdeu!!!')
            break
#(if = se) Se o jogador tiver perdido o jogo, imprimirá na tela 'Você perdeu!!!'
#e o break fará com que o loop acabe.
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            

def perdeuJogo():
    global FORCAIMG
#O global serve pra dizer que vai utilizar uma variável de fora dessa função.
    if len(letrasErradas) == len(FORCAIMG):
        return True
#O len vai dizer quantos caracteres tem na lista ou string. No caso, se a
#quantidade de letras erradas for igual ao desenho da forca vai retornar que a 
#função é verdadeira.
    else:
#(else = senão) 
        return False
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:
#for gera um loop dentro de uma lista, se a letra digitada estiver dentro da
#palavraSecreta o programa vai retornar que a letra está certa.
        if letra not in letrasCertas:
            ganhou = False
# Se a letra não estiver na palavraSecreta, retornará que a letra está
#incorreta.
    return ganhou        
        

def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
#A função input dará a oportunidade do usuário digitar o seu palpite.
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
#O elif só funcionará se todas as instruções anteriores forem falsas.
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
#Desenha o bonequinho, de acordo com a quantidade de erros.
    
    vazio = len(palavraSecreta)*'-'
#Vai colocar a quantidade de '-' de acordo com a quantidade de letras que tem
#na palavra sorteada.
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite
#Se o palpite tiver correto adiciona a letra nas letrasCertas e se tiver errado
#adiciona a letra nas letrasErradas

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
#Se a letra estiver correta vai colocá-la no lugar do '-' e mostrar para o
#usuário.
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()
#'choice' sorteia uma palavra e o 'upper' deixa em letras maiusculas. 

    
principal()
