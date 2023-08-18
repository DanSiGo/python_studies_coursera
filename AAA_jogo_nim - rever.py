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

def computador_escolhe_jogada(n, m):
    pecas = 1
    sobraram = n
    jogada = 1

    while (pecas <= m) and (pecas <= sobraram):        
        if pecas % (m+1) != 0:
            jogada = pecas
            pecas = pecas + 1            
        elif (pecas % (m+1) == 0) and (pecas <= m):
            jogada = pecas
            pecas = pecas + 1
        else:
            pecas = pecas + 1
            jogada = pecas
    if jogada == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou ", jogada, " pecas.")
    sobraram = sobraram - jogada

    if sobraram == 0:
        print("Fim do jogo! O compuador ganhou")
    else:
        if sobraram == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            return usuario_escolhe_jogada(sobraram, m)
        else:
            print("Agora restam", sobraram, "peças no tabuleiro.")
            return usuario_escolhe_jogada(sobraram, m)


def usuario_escolhe_jogada(n, m):
    pecas = int(input("\nQuantas peças você vai tirar? "))
    sobraram = n
    if pecas > sobraram:
        print("Ops! Jogava inválida")
        return usuario_escolhe_jogada(n,m)
    elif pecas > m:
        print("\nOps! Jogada inválida! Tente de novo.")
        return usuario_escolhe_jogada(n,m)
    elif pecas <= m:
        if pecas == 1:
            print("\nVocê tirou uma peça.")
            sobraram = n - pecas
        else:
            print("\nVocê tirou ", pecas, " pecas")
            sobraram = n - pecas
        if sobraram == 0:
            print("Fim do jogo! Você ganhou")
        else:
            if sobraram == 1:
                print("Agora resta apenas uma peça no tabuleiro.\n")
                return computador_escolhe_jogada(sobraram, m)
            else:
                print("Agora restam", sobraram, "pecas no tabuleiro\n")
                return computador_escolhe_jogada(sobraram, m)



def partida():    
    tipo_jogo = int(input("Bem-vindo ao jogo do NIM! Escolha: \n\n1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
    if tipo_jogo == 1 or tipo_jogo == 2:
        if tipo_jogo == 1:
            print("\nVoce escolheu uma partida isolada!\n")
            return rodada()
        if tipo_jogo == 2:
            print("\nVoce escolheu um campeonato!")
            jogos = 3
            rod = 1
    else:
        print("\nOpção inválida, escolha novamente\n")
        return partida()

    while jogos > 0:       
        print("\n**** Rodada ", rod," ****\n")
        rod = rod + 1
        jogos = jogos - 1
        rodada()
        
        if jogos == 0:
            print("\n**** Final do campoenato! ****\n")
            # print("Placar: Voce ", vc_ganhou," X ", pc_ganhou, " Computador")
        

def rodada():
            
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (n % (m+1) == 0):
        print("\nVoce começa!")
        return usuario_escolhe_jogada(n, m)

    else:
        print("\nComputador começa!\n")
        return computador_escolhe_jogada(n, m)

partida()































