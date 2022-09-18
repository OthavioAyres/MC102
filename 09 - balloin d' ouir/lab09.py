# da para fazer um contado: 
# para variação dos pontos somados vc faz um for para cada uma das entradas 
# e faz um repetidor que vai de 5 em 5 como por exemplo um tmp=1 que no ultimo ta = 5, e depois zera.
n = int(input()) * 5
lista = []
contador = dict()
t = 1
for i in range(n):
    lista.append(input())
    
    if t == 1 :
        if lista[i] not in contador:
            contador[lista[i]] = 6
        else:
            contador[lista[i]] += 6
        t += 1
    elif t == 2 :
        if lista[i] not in contador:
            contador[lista[i]] = 4
        else:
            contador[lista[i]] += 4
        t += 1
    elif t == 3 :
        if lista[i] not in contador:
            contador[lista[i]] = 3
        else:
            contador[lista[i]] += 3
        t += 1
    elif t == 4 :
        if lista[i] not in contador:
            contador[lista[i]] = 2
        else:
            contador[lista[i]] += 2
        t += 1
    else :
        if lista[i] not in contador:
            contador[lista[i]] = 1
        else:
            contador[lista[i]] += 1
        t = 1

pontuacao = list(reversed(sorted(contador.values())))
resultado = dict()
for ponto in pontuacao:
    for c in contador:
        if contador[c] == ponto:
            resultado[c] = ponto
for jogador in resultado:
    print(jogador,resultado[jogador],sep=': ')

   # for c in s:
    #    if c not in d:
     #       d[c] = 1
      #  else:
       #     d[c] += 1
