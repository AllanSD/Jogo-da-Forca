#Allan da Silva D´Avila RA 1130042 e Dennis Souza RA 1129521
#Para visualisar o histórico, ao final do game digite (jogarNovamente) em seguida digite (1)

from funcoes import jogarNovamente, dicasJogo, testarPalavra, banco, historico
import getpass
import os
os.system('cls') or None





def jogo(palavra,dicas,jogador1,jogador2):
    erros=5
    verif=['*' for letra in palavra]
    while('*' in verif and erros>0):
        os.system('cls') or None
        print('--== COMPETIDOR ==--')
        print('Palavra Secreta: ',' '.join(str(x)for x in verif))
        print('Vidas: ',erros)
        opcao=input(
        '\nArriscar letra: [1]\n'
        'Dicas: [2]\n')

        if opcao == '1':
          letra=input('Informe uma letra: ').upper()
          if(letra in verif):
           input('\nLetra já utilizada, tente outra!!')
          elif(letra in palavra):
            verif = testarPalavra(letra,palavra,verif)
            print(" ".join(str(x)for x in verif))
          else:
            erros-=1
            input('Letra incorreta.\nPressione ENTER para continuar')
        elif opcao == '2':
            print(dicasJogo(dicas))
            letra = input('Informe uma letra: ').upper()
            if(letra in verif):
                input('\nVocê já utilizou essa letra. ')
            elif(letra in palavra):
                palavraAux = testarPalavra(letra,palavra,verif)
                print(" ".join(str(x) for x in verif))
            else:
                erros-=1
                input('Letra errada. \nPressione ENTER para continuar')

        else:
            print('Opção Inválida, escolha uma das opções acima.')
            input('\nPressione ENTER para continuar.')
            os.system('cls') or None
    if erros>0:
        print('Parabéns você acertou a palavra!!!')
        input()
        vencedor = desafiante
        perdedor = competidor
        banco(palavraSecreta,desafiante,competidor,perdedor,vencedor)
        historico()
    else:
        print(jogador2+ ' Perdeu', ' '.join(str(x) for x in palavra))
        input()
        perdedor = desafiante
        vencedor = competidor
        banco(palavraSecreta,desafiante,competidor,vencedor,perdedor)
        historico()
x = True
while x:
    os.system('cls') or None
    print('---== Vamos iniciar o jogo ==---')
    desafiante = input('Nome do Desafiante: ').upper().strip()
    competidor = input('Nome do Competidor: ').upper().strip()
    input('\nPressione ENTER para continuar')
    os.system('cls') or None

    print('---== DESAFIANTE ==---')
    palavraSecreta=input('Informe a palavra que deseja esconder: ').upper().strip()
    dicas=['','','']
    dicas[0]=input('Informe a primeira dica: ')
    dicas[1]=input('Informe a segunda dica: ')
    dicas[2]=input('Informe a terceira dica: ')
    input('\nPressione ENTER para continuar')
    os.system('cls') or None

    jogo(palavraSecreta,dicas,desafiante,competidor)
    jogarNv = ''
    while jogarNv != 'S' and jogarNv != 'N':
      jogarNv = input('Deseja jogar novamente? Sim [s] ou Não [n]').upper()
      os.system('cls') or None
            
        
    jogarNovamente(jogarNv)