# DICA: use os métodos lower, replace, split e index

def contagem_elemento(a,b):
    qtd = 0
    for element in b:
        if element == a:
            qtd += 1
    return qtd

# Leitura de dados
n = int(input())
palindromos = []
palindromos_original = []
for _ in range(n):
    texto = [t for t in input().split()]

# Leitura das linhas do texto e tratamento
    for i in range(len(texto)):
        texto[i]= texto[i].lower()
        for l in range(len(texto[i])):
            tmp = ''.join(l for l in texto[i] if l not in '{".", ",", ":", ";", "!", "?"}.')
    
        if tmp == tmp[::-1]:
            palindromos_original.append(tmp)

reverselist = list(reversed(palindromos_original))

for palavra in reverselist:
    while contagem_elemento(palavra,reverselist) > 1:
        reverselist.remove(palavra)

palindromos = list(reversed(reverselist))


contador = dict(zip(palindromos,[0 for i in range(len(palindromos))]))


for i in palindromos_original:
    contador[i] += 1

for i in (palindromos):
    print(i,contador[i])

# Processamento

# Impressão da saída