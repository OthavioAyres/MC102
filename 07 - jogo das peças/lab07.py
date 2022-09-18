###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Encaixe Perfeito
# Nome: Othavio henrique de Jesus Ayres
# RA:246666
###################################################

# Leitura do número de partidas
n = int(input())

for _ in range(n):
    # Leitura das peças 1 e 2
  P1 = [int(i) for i in input().split()]
  P2 = [int(i) for i in input().split()]
  P0 = P1.reverse
  posicoes_normal=[]
  pontuacao_normal=[]
  posicoes_reverse=[]
  pontuacao_reverse=[]
  # Processamento das possibilidades de encaixe
  for i in range(len(P2)-len(P1)+1):  
      J = []
      for k in range(len(P1)):
          J.append(P1[k]+P2[i+k])
       
      s = max(J) 
      for j in range(len(J)):
          J[j] = s - J[j]
      
      posicoes_normal.append(i+1)
      pontuacao_normal.append(sum(J))
      
      
      
  
  P1.reverse()
  for i in range(len(P2)-len(P1)+1):  
      J = []
      for k in range(len(P1)):
          J.append(P1[k] + P2[i+k])
      s = max(J)
      for j in range(len(J)):
          J[j] = s - J[j]
      posicoes_reverse.append(i+1)
      pontuacao_reverse.append(sum(J))
     
  
  min_normal= min(pontuacao_normal) 
  posic_min_normal = posicoes_normal[pontuacao_normal.index(min_normal)]
  min_reverse= min(pontuacao_reverse) 
  posic_min_reverse = posicoes_reverse[pontuacao_reverse.index(min_reverse)]
  if min_normal == 0:
      print('Encaixe Perfeito!')
      print('Posicao de Encaixe:',posic_min_normal)
      print('Peca 1: Normal')
  elif min_reverse == 0:
      print('Encaixe Perfeito!')
      print('Posicao de Encaixe:',posic_min_reverse)
      print('Peca 1: Invertida')
  elif min_normal <= min_reverse:
      print('Pontuacao:',min_normal)
      print('Posicao de Encaixe:',posic_min_normal)
      print('Peca 1: Normal')
  elif min_normal > min_reverse:
      print('Pontuacao:',min_reverse)
      print('Posicao de Encaixe:',posic_min_reverse)
      print('Peca 1: Invertida')
  