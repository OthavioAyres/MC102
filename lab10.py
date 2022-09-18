#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Aventura na Amazônia
# Nome:
# RA:
#####################################################

# Criação da matriz

matriz = [['.' for _ in range(20)] for _ in range(20)]

# Leitura da entrada e preenchimento da matriz

linha, coluna = input().split() # posição inicial
linha = int(linha)
coluna = int(coluna)

listatmp = input()
listatmp= listatmp.split()
if len(listatmp) == 2:
    sentido = listatmp[0]
    distancia = int(listatmp[1])


f = 0
while f == 0:
    if sentido == 'N':
        for p in range(distancia+1):
            if matriz[linha - p][coluna] == '.':
                matriz[linha - p][coluna] = '+'
        linha = linha - distancia
    if sentido == 'S':
        for p in range(distancia+1):
            if matriz[linha+p][coluna] == '.':
                matriz[linha + p][coluna] = '+'
        linha = linha + distancia    
    if sentido == 'L':
        for p in range(distancia+1):
            if matriz[linha][coluna + p] == '.': 
                matriz[linha][coluna + p] = '+'
        coluna = coluna + distancia
    if sentido == 'O':  
        for p in range(distancia+1):
            if matriz[linha][coluna - p] == '.':
                matriz[linha][coluna - p] = '+'
        coluna = coluna - distancia
    if sentido == 'A':
        matriz [linha][coluna]= '#'
    
    
    #Reentrada das informações
    listatmp = input()
    listatmp= listatmp.split()
    if len(listatmp) == 2:
        sentido = listatmp[0]
        distancia = int(listatmp[1])
    else:
        sentido = listatmp[0]
    

    if sentido == 'F':
        f = 1




# Impressão da matriz

for l in matriz:
    print(" ".join(l))

