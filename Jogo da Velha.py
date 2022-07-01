#Jogo da velha
#Estou importando uma biblioteca que gera números aleatórios
import random 

tabuleiro = ['_','_','_','_','_','_','_','_','_']

#Criei uma função tabuleiro
def visual_tabuleiro(tabuleiro):
    print('O tabuleiro está assim:\n')
    print('')
    #Vou criar um laço de repetição com o tamanho da minha variável tabuleiro.
    for i in range(len(tabuleiro)):
        print(tabuleiro[i], end = ' ')
        if i == 2 or i == 5 or i == 8:
            print('')

quantidade_jogadas = 0
quantidade_jogadascomputador = 0

#Essa função vai verificar se houve algum ganhador
def analise_vitoria(tabuleiro, jogador):
    #Fazendo a checagem das linhas.
    if tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador:
        if jogador == 'X':
            return 1
        else:
            return 2
    if tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador:
        if jogador == 'X':    
            return 1
        else:
            return 2
    if tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador:
        if jogador == 'X':    
            return 1
        else:
            return 2

    #Fazendo a checagem das colunas
    if tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador:
        if jogador == 'X':    
            return 1
        else:
            return 2    
    if tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador:
        if jogador == 'X':    
            return 1
        else:
            return 2
    if tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador:
        if jogador == 'X':    
            return 1
        else:
            return 2

    #fazendo a checagem de diagonais
    if tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador:
        if jogador == 'X':    
            return 1
        else:
            return 2
    if tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador:
        if jogador == 'X':    
            return 1
        else:
            return 2
    
    return 0
    
print('Seja muito bem vindo ao meu jogo da velha!')
print('Esse jogo foi desenvolvido por Ellioth, Marcos Aurélio e Vitor Valente.')
print('Para jogar é muito simples,basta você conseguir preencher as linhas ou colunas com o X ou O')
print('Insira números de 1 a 9 para fazer a sua jogada.')
print('___|___|___')
print('___|___|___')
print('   |   |')
    
nome_usuario = input('Insira o seu nome: \n')

escolha = int(input('Digite 1 se você quiser começar e digite 2 para você jogar contra mim.\n'))
if escolha == 1:
    print('Ótimo, você vai começar!')
elif escolha == 2:
    print('Obrigado pela cortesia!')
    print('Eu começo.')
else:
    print('Número errado.')
    
#Caso o usuário escolha jogar contra a máquina.
while True:
        jogada = int(input('Insira o número da sua jogada: \n'))
        
        while tabuleiro[jogada -1] != '_':
            print('Jogada inválida.')
            visual_tabuleiro(tabuleiro)
            jogada = int(input('Insira a sua jogada novamente.'))
            
        tabuleiro[jogada -1] = 'X'
        quantidade_jogadas += 1
        
        vencedor = analise_vitoria(tabuleiro,'X')
        
        visual_tabuleiro(tabuleiro)
        
        
        if vencedor != 0:
            break
        
        if quantidade_jogadas == 9:
            break
        
        visual_tabuleiro(tabuleiro)
        
        jogada_computador = random.randint(1,9)
               
        while tabuleiro[jogada_computador-1] != '_':
            jogada_computador = random.randint(1,9)
            visual_tabuleiro(tabuleiro)

        tabuleiro[jogada_computador -1] = 'O'
        quantidade_jogadascomputador += 1
        
        vencedor = analise_vitoria(tabuleiro, 'O')
        if vencedor != 0:
            break
        
        if quantidade_jogadas == 9:
            break
        
        print('A minha jogada foi essa \n')
        visual_tabuleiro(tabuleiro)

#Quando a opção é o computador,ele começa e não printa pra mim o tabuleiro antes de eu jogar e isso eu não consigo evitar.
while escolha == 2:
    jogada_computador = random.randint(1,9)
    
    visual_tabuleiro(tabuleiro)
           
    while tabuleiro[jogada_computador-1] != '_':
        jogada_computador = random.randint(1,9)
        visual_tabuleiro(tabuleiro)

    tabuleiro[jogada_computador -1] = 'X'
    quantidade_jogadascomputador += 1
    
    vencedor = analise_vitoria(tabuleiro)
    
    print('A minha jogada foi essa \n')
    visual_tabuleiro(tabuleiro)
    
    if vencedor != 0:
        break
    
    if quantidade_jogadas == 9:
        break
    
    jogada = int(input('Insira o número da sua jogada: \n'))
    
    while tabuleiro[jogada -1] != '_':
        print('Jogada inválida.')
        visual_tabuleiro(tabuleiro)
        jogada = int(input('Insira a sua jogada novamente.'))
        
    tabuleiro[jogada -1] = 'O'
    quantidade_jogadas += 1
    
    vencedor = analise_vitoria(tabuleiro)
    
    visual_tabuleiro(tabuleiro)
    
    if vencedor != 0:
        break
    
    if quantidade_jogadas == 9:
        break

#Eu não consigo parar o loop quando dá velha por algum motivo,então meu código está incompleto
if vencedor == 1:
	print ('Parabéns ', nome_usuario,' você provou ser um adversário forte ao ponto de me derrotar.')
elif vencedor == 2:
	print ('Você foi derrotado,isso era inevitável já que sou invencível mas fico triste porque você parece uma pessoa legal.')
else:
	print ("Deu velha, ninguém venceu, foi empate!")
    

visual_tabuleiro(tabuleiro)



        
