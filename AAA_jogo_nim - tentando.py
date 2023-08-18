"""

Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas
numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, retirando pelo
menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis
ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste
em deixar sempre múltiplos de (m+1) peças ao jogador oponente.

Objetivo
Você deverá escrever um programa na linguagem Python, versão 3, que permita
a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá
seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível
retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso
considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o
jogador a iniciar a partida com a frase "Você começa!"

Caso contrário, o computador toma a inciativa de começar o jogo, declarando
"Computador começa!"

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em
deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso
isso não seja possível, deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador se
utilize da estratégia vencedora.


O programa deve implementar:

Uma função computador_escolhe_jogada que recebe, como parâmetros, os números
n e m descritos acima e devolve um inteiro correspondente à próxima jogada do
computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de
acordo com a estratégia vencedora.

Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita
que o jogador informe sua jogada e verifica se o valor informado é válido. Se
o valor informado for válido, a função deve devolvê-lo; caso contrário, deve
solicitar novamente ao usuário que informe uma jogada válida.

Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que
informe os valores de n e m e inicia o jogo, alternando entre jogadas do
computador e do usuário (ou seja, chamadas às duas funções anteriores).
A escolha da jogada inicial deve ser feita em função da estratégia vencedora,
como dito anteriormente. A cada jogada, deve ser impresso na tela o estado
atual do jogo, ou seja, quantas peças foram removidas na última jogada e
quantas restam na mesa. Quando a última peça é removida, essa função imprime
na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.

Quantas peças? 3
Limite de peças por jogada? 1

Computador começa!

O computador tirou uma peça.
Agora restam 2 peças no tabuleiro.

Quantas peças você vai tirar? 2

Oops! Jogada inválida! Tente de novo.

Quantas peças você vai tirar? 1

Você tirou uma peça.
Agora resta apenas uma peça no tabuleiro.

O computador tirou uma peça.
Fim do jogo! O computador ganhou!

"""
# O jogo começa chamando a função "partida"

def partida():

# Variaveis pra contar o placar

    pc = 0  
    vc = 0
        
# Iniciando uma partida
           
    tipo_jogo = int(input("Bem-vindo ao jogo do NIM! Escolha: \n\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))

# Opções inválidas:
        
    if tipo_jogo !=1 and tipo_jogo !=2:
        print("\nOpção inválida, escolha novamente\n")
        return partida()

# Ao escolher 1 ou 2:

    elif tipo_jogo == 1 or tipo_jogo == 2:
        if tipo_jogo == 1:
            rod = 3  # ao escolher partida unica essa variável indica que o
                     # while vai rodar apenas 1 vez
            print("\nVoce escolheu uma partida isolada!\n")
            
        elif tipo_jogo == 2:
            print("\nVoce escolheu um campeonato!")            
            rod = 1  # ao escolher campeonato essa variável indica que o:
                     # while vai rodar de 1 a 3, ou seja, 3 vezes = 3 partidas
                        
        while rod <= 3:
        
            if tipo_jogo == 2:       
                print("\n**** Rodada ", rod,"****\n")                
        
# Iniciando uma rodada
            
            if rod <= 3:       
                n = int(input("Quantas peças? "))
                m = int(input("Limite de peças por jogada? "))
                rod = rod + 1
                
# Se a quantidade de peças for divisível pelo limite de peças + 1, o usuário começa
                
                if (n % (m+1) == 0):                    
                    print("\nVoce começa!\n")

# Jogadas iniciando pelo usuario
                    
                    while n > 0:                        
                        n = n - usuario_escolhe_jogada(n, m)                                                                         
                        if n > 0:
                            if n == 1:
                                print("Agora resta apenas uma peça no tabuleiro.\n")
                            else:
                                print("Agora restam", n, "pecas no tabuleiro\n")
                            n = n - computador_escolhe_jogada(n, m)
                            if n == 1:
                                print("Agora resta apenas uma peça no tabuleiro.\n")
                            elif n == 0:
                                print("Fim do jogo! O computador ganhou") 
                                pc = pc + 1  # conta que o computador ganhou 
                            else:
                                print("Agora restam", n, "pecas no tabuleiro\n") 
                        else:
                            print("Fim do jogo! Você ganhou")
                            vc = vc + 1  # conta que o usuario ganhou                        
                            
# Se a quantidade de peças não for divisível pelo limite de peças + 1, o computador começa

                else:                    
                    print("\nComputador começa!\n")

# jogadas iniciando pelo computador
                    
                    while n > 0:                        
                        n = n - computador_escolhe_jogada(n, m)                                                
                        if n > 0:
                            if n == 1: # cenário : se sobrou 1 peça ou mais de 1 peça
                                print("Agora resta apenas uma peça no tabuleiro.\n") 
                            else:
                                print("Agora restam", n, "peças no tabuleiro.\n") 
                            n = n - usuario_escolhe_jogada(n, m)
                            if n == 1:
                                print("Agora resta apenas uma peça no tabuleiro.\n")
                            elif n == 0:
                                print("Fim do jogo! Você ganhou")
                                vc = vc + 1  # conta que o usuario ganhou
                            else:
                                print("Agora restam", n, "pecas no tabuleiro\n") 
                        else: # cenário : se o computador tirou o suficiente para ganhar
                            print("Fim do jogo! O computador ganhou") 
                            pc = pc + 1  # conta que o computador ganhou                                  
                            
            if rod == 4 and tipo_jogo == 2:                           
                print("\n**** Final do campeonato! ****\n")
                print("Placar: Você", vc, "X", pc, "Computador")
                break  # mais fácil que torcer para as booleanas do
                       # while darem certo

def computador_escolhe_jogada(n, m):
    pecas = 0
    jogada = 0
    while pecas < m:
        pecas = pecas + 1
        if (n - pecas) % (m+1) == 0:
            jogada = pecas                   
        elif (n == m or n > (m+1)) and ((n - jogada) % (m+1) != 0):
            jogada = m

# Aqui são as frases que serão de acordo com a jogada
                        
    if jogada == 1:  # Cenário : se computador tira 1 peça ou mais de 1 peça
        print("O computador tirou uma peça.\n")
        return jogada 
    else:
        print("O computador tirou", jogada, "pecas.\n")
        return jogada

def usuario_escolhe_jogada(n, m):
    pecas = int(input("Quantas peças você vai tirar? \n"))
    
# Em caso de opções invalidas:
    
    if pecas > n or pecas > m:
        print("\nOps! Jogada inválida! Tente de novo.")
        return usuario_escolhe_jogada(n,m)
    
# Opções possíveis, situação em que o jogo acaba:

    else:
        if pecas == 1:
            print("\nVocê tirou uma peça.\n")
            return pecas            
            
        else:
            print("\nVocê tirou", pecas, "peças.\n")
            return pecas  

partida()
    
    































