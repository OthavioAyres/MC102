###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Dia do Progresso I
# Nome: OTHAVIO HENRIQUE DE JESUS AYRES
# RA: 246666
###################################################
M = []
L = int(input())

# separando os portais em um dicionario
gates = dict()
for _ in range(L):
    tmp = input().split()
    M.append(tmp)
    for i in range(len(tmp)):
        if tmp[i] not in 'NSLO#*':
            if tmp[i] not in gates:
                gates[tmp[i]]= [[_,i]]
            else:
                a = [_,i]
                gates[tmp[i]].append(a)

#posição inicial jayce               
linha, coluna = (int(i) for i in input().split())

# locomoção
sentido = ''

f = len(M)*len(M[0])*2
while f > 0:
    if abs(coluna) < len(M[0]) and abs(linha) < L:
    
        if M[linha][coluna] in 'NSLO#*':
            if M[linha][coluna] == 'N':
                linha -= 1
                f -= 1
                sentido = 'N'
        
            elif M[linha][coluna] == 'S':
                linha += 1
                f -= 1
                sentido = 'S'
            elif M[linha][coluna] == 'L':
                coluna += 1
                f -= 1
                sentido = 'L'
            elif M[linha][coluna] == 'O':
                coluna -= 1
                f -= 1
                sentido = 'O'
            elif M[linha][coluna] == '#':
                
                f = 0
        
            elif  M[linha][coluna] == '*':
                print('Jayce conseguiu chegar em Piltover')
                f = -1
        else:
            tmp2 = [linha,coluna]
            
            linha,coluna  = gates[M[linha][coluna]][gates[M[linha][coluna]].index(tmp2)-1]

            if sentido == 'N':
                linha -= 1
            elif sentido == 'S':
                linha += 1
            elif sentido == 'L':
                coluna += 1
            else :
                coluna -= 1 
    else :
        f = 0
if f == 0:
    print('Jayce nao conseguiu chegar em Piltover')
