'''
Função que informa as jogadas do usuário
r = quantidade de peças retiradas do tabuleiro
'''
def usuario_escolhe_jogada(n,m):
    r = int(input("Quantas peças você vai tirar: "))
    if n >= m:
        while r > m:
            print(f'Esse valor não é válido. O número máximo de peças a serem retiradas é {m}. Informe um novo valor: ')
            r = int(input("Quantas peças você vai tirar: "))
    else:
        if r > n:
            r = print(f'Esse valor não é válido. O número de peças no tabuleiro é {n}. Informe um novo valor: ')
    return r #número de peças a serem retiradas


'''
Função que indica a jogada do computador de acordo com a estratégia vencedora que consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
r = quantidade de peças retiradas do tabuleiro
'''
def computador_escolhe_jogada(n,m):
    i = m #inicio
    if n >= m:
        while (n - i) % (m + 1) != 0:
            i = i - 1 #número de peças a serem retiradas
            if i == 0:
                break
        p = n - i #peças
        if p == n:
            n = n - m
            r = m
        else:
            n = p
            r = i
    else:
        r = n
    return r #número de peças a serem retiradas
    

'''
Função principal que dá início ao jogo.

n = número de peças no tabuleiro
m = número máximo de peças que podem ser retiradas em uma jogada
'''
def partida():    
    n = int(input("Informe o número de peças no tabuleiro: "))
    if n <= 0:
        print("Esse valor não é válido. Digite um valor maior que zero")
        n = int(input("Informe o número de peças no tabuleiro: "))
    m = int(input("Informe o número máximo de peças a serem retiradas por jogada: "))
    if m > n:
        print("Esse valor não é válido. Digite um valor maior que zero")
        m = int(input("Informe o número máximo de peças a serem retiradas por jogada: "))
        
    if n % (m +1) == 0:
            print("Você começa")
            while n >= 1:
                r = usuario_escolhe_jogada(n,m)
                n = n - r
                print(f'Você tirou {r} peça(s).\nAgora restam {n} peça(s) no tabuleiro.\n')
                if n == 0:
                    break
                r = computador_escolhe_jogada(n,m)
                n = n - r
                print(f'O computador tirou {r} peça(s).\nAgora restam {n} peças no tabuleiro.\n')
                if n == 0:
                    break
    else:
        print("Computador começa")
        while n >= 1:
            r = computador_escolhe_jogada(n,m)
            n = n - r
            print(f'O computador tirou {r} peça(s).\nAgora restam {n} peças no tabuleiro.\n')
            if n == 0:
                break
            r = usuario_escolhe_jogada(n,m)
            n = n - r
            print(f'Você tirou {r} peça(s).\nAgora restam {n} peça(s) no tabuleiro.\n')
            if n == 0:
                break
        
    print("O computador ganhou!\n")

'''
Função criada para gerar 3 rodadas sequenciais automaticamente.
'''
def campeonato():
    cont = 1
    while cont <= 3:
        print(f'**** Rodada {cont} ****\n')
        partida()
        cont = cont + 1
    print('**** Final do campeonato! ****\n\nPlacar: Você 0 x 3 Computador')
        

'''
Iniciando o Jogo!!!!!
'''
iniciar = int(input("Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato \n"))
if iniciar == 1:
    print("Voce escolheu uma partida isolada!\n")
    partida()
else:
    print("Voce escolheu um campeonato!\n")
    campeonato()

