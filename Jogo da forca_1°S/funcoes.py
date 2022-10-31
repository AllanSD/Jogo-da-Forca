#Allan da Silva D´Avila RA 1130042 e Dennis Souza RA 1129521

from datetime import datetime

import os

def jogarNovamente(jogarNv):
    if jogarNv == 'S':
      x = True
    else:
      x = False

def dicasJogo(texto):
    try:
        dica=texto[0]
        texto.pop(0)
        return '\n' +dica
    except:
        return 'Acabaram as Dicas!'

def testarPalavra(letra,palavra1,palavra2):
    for ind,valor in enumerate(palavra1):
        if valor == letra:
            palavra2 [ind] = letra
    return palavra2

def banco(palavra,jogador1,jogador2,vencedor,perdedor):
    date=datetime.now().strftime('%d/%m/%Y %H:%M')
    arq = open('log.txt','a')
    arq.write('\n\nInicio do jogo: '+str(date)+'\nPalavra Secreta: '+palavra+'\nDesafiante: '+jogador1+'\nCompetidor: '+jogador2+ '\nVencedor: '+vencedor+ '\nPerdedor: '+perdedor)
    arq.close()

def historico():
    os.system('cls') or None
    historico=input('Você deseja visualizar o histórico?\n1 Sim \t2 Não\n') .upper()
    if historico == '1' or historico[0] == 'S':
        arq = open("log.txt","r")
        resultados = arq.readlines()
        os.system('cls') or None
        print("-----=== Resultados ===-----\n")
        for linha in resultados:
            print(linha)
        arq.close()
        input('\n Pressione ENTER para continuar! ')