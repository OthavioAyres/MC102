#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Plataforma
# Nome: OTHAVIO HENRIQUE DE JESUS AYRES
# RA: 246666
#####################################################

"""
Esta função recebe como parâmetro uma lista que representa o tamanho do salto 
que pode ser dado em cada ponto de uma plataforma. Além disso, uma posição inicial 
na plataforma é determinada pelo parâmetro i. O retorno esperado para a função é 
um valor booleano, com True indicando que foi possível sair da plataforma e False 
indicando que o personagem ficou preso na plataforma (loop).
"""

plataforma = input().split()

i = int(input()) 
posicoes_anterioes = []

# ...
#A IDELIA É A SEGUINTE RECURSÁO, TESTAR SE É POSSIVEL SAIR DA PLATAFORMA PELA POSIÇAO INICIAL
#CASO NAO SEJA TESTAR SE É POSSIVEL PARA AS 2 * J POSSIVEIS SALTO, ONDE ENTRA A RECURSIVIDADE.
# Leitura dos dados
def salto(plataforma, i):

    aux = int(plataforma[i - 1 ])

   # print(aux,i)
     
    if (aux >= i) or (aux > len(plataforma) - i ):
        
        return True
         
    else:
        if i not in posicoes_anterioes:
            posicoes_anterioes.append(i)
            for k in range(1,aux+1):
                if salto(plataforma,i-k) == True:
                    return True
                elif salto(plataforma,i+k) == True:
                    return True    
            

        return False
    
        

# Verificação se é possível sair da plataforma
if salto(plataforma,i) == True:
    print("Saiu da plataforma")
else:
    print("Loop")