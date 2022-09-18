###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Conjectura de Collatz
# Nome: Othavio Henrique de jesus Ayres
# RA: 246666 
###################################################
n = int(input())
for q in range(n):
  qtd_par = 0
  qtd_impar = 1
  c = int(input())
  entrada = c
  maior_numero = 1
  
  while c != 1:
    if c > maior_numero:
      maior_numero = c
    if c % 2 == 0:
      c = c / 2
      qtd_par += 1
    else:
      c = 3 * c +1
      qtd_impar +=1
      
    
  print('Valor inicial:',entrada)
  print('Numeros Pares:',int(qtd_par))
  print('Numeros Impares:',int(qtd_impar))
  print('Maior Numero:',int(maior_numero))