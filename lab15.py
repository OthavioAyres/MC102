###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Dia do Progresso II
# Nome: Othavio Henrique de Jesus Ayres
# RA: 246666
###################################################

# lendo a matriz
L = int(input())
M = []
P = dict()

# Dica: construa um dicionário com as posições de cada par de portais

for _ in range(L):
    tmp = input().split()
    M.append(tmp)
    for i in range(len(tmp)):
        if tmp[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if tmp[i] not in P:
                P[tmp[i]]= [[_,i]]
            else:
                a = [_,i]
                P[tmp[i]].append(a)

# lendo a posição inicial
x_i, y_i = (int(i) for i in input().split())


'''
Dada uma matriz, a posição (x,y) e os portais, 
verifica se é possível chegar em Piltover 
'''
M_aux = [[0 for x in range(len(M[0]))] for x in M]

sentido = [0]



def busca_caminho(M, x, y, P):
    if 0 > x or x > len(M) -1 or 0 > y or y > len(M[0]) -1 :
        return False

    if M[x][y] in P:
#            print('portal')
            x,y  = P[M[x][y]][P[M[x][y]].index([x,y])-1]
            if sentido[-1] == 'N':
                x -= 1
            if sentido[-1] == 'S':
                x += 1  
            if sentido[-1] == 'L':
                y += 1
            if sentido[-1] == 'O' :
                y -= 1 

    if 0 > x or x > len(M) -1 or 0 > y or y > len(M[0]) -1 :
        return False

    if M[x][y] == "*":
        return True
    if M[x][y] == '#':
        M_aux[x][y] = 1
        return False
    if M_aux[x][y] != 1:
        M_aux[x][y] = 1
#        print(x,y)
        
        
        sentido[-1] = 'S'
        if busca_caminho(M, x+1, y, P) == True:
            return True

        sentido[-1] = 'N'
        if busca_caminho(M, x-1, y, P) == True:
            return True

        sentido[-1] = 'L'
        if busca_caminho(M, x, y+1, P) == True:
            return True
        
        sentido[-1] = 'O'
        if busca_caminho(M, x, y-1, P) == True:
            return True

        return False
#print(busca_caminho(M,x_i,y_i,P))



        
    
    
    




# verificação do caminho até Piltover


# saída de dados

if busca_caminho(M,x_i,y_i,P) == True:
    print('Jayce conseguiu chegar em Piltover')
else:
    print('Jayce nao conseguiu chegar em Piltover')