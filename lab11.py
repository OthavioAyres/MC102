# Othavio henrique de jesus ayres ra 246666
# matriz = [(input().split()) for x in range(10)]
linhas = ['A','B','C','D','E','F','G','H','I','J']
matriz = []
navios = []
navios_posicoes = []

#Trabalhando com a entrada 

for _ in range(10):
    tmp = input().split()
    matriz.append(tmp)
    for x in range(len(tmp)):
        if tmp[x] != '.':
            navios.append(tmp[x])
            navios_posicoes.append(linhas[_] + ' ' +str(x+1))

#print(navios)
#print(navios_posicoes)

vida_navios = dict()

for _ in navios:
    if _ not in vida_navios:
        vida_navios[_] = 1
    else:
        vida_navios[_] += 1


#SAIDA:
n = int(input())
for k in range(n):
    p = input()
    if p in navios_posicoes:
        vida_navios[navios[navios_posicoes.index(p)]] -= 1
        if vida_navios[navios[navios_posicoes.index(p)]] > 0:
            print('atingiu o navio',navios[navios_posicoes.index(p)])
        else:
            print('afundou o navio',navios[navios_posicoes.index(p)])            
    else:
        print('agua')