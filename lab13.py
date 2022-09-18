#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - 6174
# Nome: Othavio Henrique de Jesus Ayres
# RA: 246666
#####################################################
def listar_numero(a,b):
    ##transforma o numero em lista
    
    for i in range(4):
        b.append(a[i])
    

# Leitura do número N
N = input()


while N != '6174':
    print(N)
    lista_N = []
    listar_numero(N,lista_N)
    lista_C = sorted(lista_N)
    lista_D = list(reversed(lista_C))

    C = int(''.join(i for i in lista_C))

    D = int(''.join(i for i in lista_D))

    N = str(D-C)
print('6174')



# Repetição do processo para geração de f(N) até obtermos o número 6174