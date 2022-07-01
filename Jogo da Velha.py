#Exercício 1
#nome = input('Insira o nome do usuário: \n')
#senha = input('Insira a senha: \n')

#while (nome == senha):
#    print('A senha não pode ser igual ao usuário!')
#    nome = input('Insira o nome do usuário: \n')
#    senha = input('Insira a senha: \n')
    
#Exercício 2
#eleitores = int(input('Digite o número total de eleitores: \n'))
#candidato_1 = 0
#candidato_2 = 0
#candidato_3 = 0
#nulo = 0

#for i in range(eleitores):
#    voto = int(input('Digite 1 para votar no candidato A,digite 2 para votar no candidato B,digite 3 para votar no candidato C,digite 4 para votar nulo \n'))
#    if voto == 1:
#        candidato_1 = candidato_1 + 1
#    elif voto == 2:
#        candidato_2 = candidato_2 + 1
#    elif voto == 3:
#        candidato_3 = candidato_3 + 1
#    else:
#        nulo = nulo + 1

#print('O número de eleitores foi de: ',eleitores)
#print('O candidato número 1 recebeu ', candidato_1,' votos')
#print('O candidato número 2 recebeu ', candidato_2,' votos')
#print('O candidato número 3 recebeu ', candidato_3,' votos')
#print('Votos nulos: ',nulo)

#Exercício 3
#turmas = int(input('Insira o número de turmas: \n'))
#count_alunos = 0
#count_turmas = 0

#while count_turmas < turmas:
#    alunos = int(input('Insira o número de alunos por turma: '))
#    if alunos <= 40:
#        count_alunos = count_alunos + alunos
#        count_turmas = count_turmas + 1
#    else:
#        print('Não é possível colocar mais de 40 alunos em uma turma!')

#media = count_alunos/count_turmas
#print('O número de turmas é: ',count_turmas)
#print('O número total de alunos é: ',count_alunos)
#print('A média de alunos por turma é: ',media)

#Exercício 4
'''menu=int(input('Olá, digite 1 para ver o menu e 0 para sair.\n'))

if menu == 1:
    print('Especificação    Código    Preço','\nCachorro Quente    100    R$1,20','\nBauru Simples      101    R$1,30')
    print('Bauru com ovo      102    R$1,50','\nHambúrguer         103    R$1,20')
    print('Cheeseburguer      104    R$1,30','\nRefrigerante       105    R$1,00')
    codigo = int(input('Insira o código do lanche desejado: \n'))
    while (codigo == 100):
        lanche = 1.20
        quantidade = int(input('Insira a quantidade desejada: \n'))
        valor_compra = lanche * quantidade
        if quantidade > 0:  
            print('O valor individual do lanche é: R$ %.2f'%lanche)
            print('O valor total da compra é: R$ %.2f'%valor_compra)
        else:
                print('É necessário comprar ao menos 1 lanche')
    while (codigo == 101):
        lanche = 1.30
        quantidade = int(input('Insira a quantidade desejada: \n'))
        valor_compra = lanche * quantidade
    if quantidade > 0:  
        print('O valor individual do lanche é: R$ %.2f'%lanche)
        print('O valor total da compra é: R$ %.2f'%valor_compra)
    else:
        print('É necessário comprar ao menos 1 lanche')
    while (codigo == 102):
        lanche = 1.50
        quantidade = int(input('Insira a quantidade desejada: \n'))
        valor_compra = lanche * quantidade
    if quantidade > 0:  
        print('O valor individual do lanche é: R$ %.2f'%lanche)
        print('O valor total da compra é: R$ %.2f'%valor_compra)
    else:
        print('É necessário comprar ao menos 1 lanche')     
    while (codigo == 103):
        lanche = 1.20
        quantidade = int(input('Insira a quantidade desejada: \n'))
        valor_compra = lanche * quantidade
    if quantidade > 0:  
        print('O valor individual do lanche é: R$ %.2f'%lanche)
        print('O valor total da compra é: R$ %.2f'%valor_compra)
    else:
        print('É necessário comprar ao menos 1 lanche')
    while (codigo == 104):
        lanche = 1.30
        quantidade = int(input('Insira a quantidade desejada: \n'))
        valor_compra = lanche * quantidade
    if quantidade > 0:  
        print('O valor individual do lanche é: R$ %.2f'%lanche)
        print('O valor total da compra é: R$ %.2f'%valor_compra)
    else:
        print('É necessário comprar ao menos 1 lanche')
    while (codigo == 105):
        lanche = 1.30
        quantidade = int(input('Insira a quantidade desejada: \n'))
        valor_compra = lanche * quantidade
    if quantidade > 0:  
        print('O valor individual do lanche é: R$ %.2f'%lanche)
        print('O valor total da compra é: R$ %.2f'%valor_compra)
    else:
        print('É necessário comprar ao menos 1 lanche')
else:
    print('Volte sempre!')'''
    
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



        
