# JogoDoNIM
Jogo do NIN é um programa proposto pelo curso <i>Introdução a Ciência da Computação com Python</i> ministrado pela USP no Coursera.
Consiste em um jogo de tabuleiro para dois jogadores, computador e usuário, e que possui como estratégia ganhadora deixar sempre múltiplos de (m+1) peças ao jogador oponente.
<p><b>É o meu primeiro programa desenvolvido em python totalmente sozinha. Uma etapa vencida, apesar de ainda ter muito a ser aprimorado.</b></p>

<h3> Objetivo do Jogo</h3>

Escrever um programa na linguagem Python que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:
<li>Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"
<li>Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
