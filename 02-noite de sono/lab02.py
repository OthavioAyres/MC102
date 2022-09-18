###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Noite de Sono
# Nome: Othavio Henrique de Jesus Ayres
# RA: 246666
###################################################

# Leitura de dados

h_1 = int(input())
m_1 = int(input())
h_2 = int(input())
m_2 = int(input())


# Cálculo do tempo dormido E  Impressão da resposta
a = 23 - h_1 +(60- m_1)/60
b = h_2+m_2/60
print(a+b >= 8)