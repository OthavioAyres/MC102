hp_j = int(input())
hp_e = int(input())
atk_j = int(input())
for j in range(atk_j):
    a = int(input())
    if hp_j < hp_e :
        hp_e -= a/2
    else:
        hp_e -= a
if hp_e < 1 :
    hp_e = 0
    print('Vida da Jinx:',int(hp_j))
    print('Vida do Ekko:',int(hp_e))
    print('Jinx foi a vencedora da batalha')
else:
    atk_e = int(input())
    for j in range(atk_e):
        a = int(input())
        if hp_e < hp_j :
            hp_j -= a/2
        else:
            hp_j -= a
    if hp_j < 1:
        hp_j = 0   
    
    if hp_e < hp_j:
        print('Vida da Jinx:',int(hp_j))
        print('Vida do Ekko:',int(hp_e))
        print('Jinx foi a vencedora da batalha')
    elif hp_j < hp_e:
        print('Vida da Jinx:',int(hp_j))
        print('Vida do Ekko:',int(hp_e))
        print('Ekko foi o vencedor da batalha')
    elif hp_j == hp_e :
        print('Vida da Jinx:',int(hp_j))
        print('Vida do Ekko:',int(hp_e))
        print('A batalha terminou empatada')