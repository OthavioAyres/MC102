n = int(input())
candidatos_ord = []
candidatos = []
votos_ord = []
votos=[]
for i in range(n):
	candidatos.append(input())

for j in range(n):
	votos_ord.append(int(input()))

for q in range(len(votos_ord)):
    votos.append(votos_ord[q])
    candidatos_ord.append(candidatos[q])
v_b = int(input())

v_n = int(input())
v_total = sum(votos_ord)
votos_ord.sort(reverse=True)



for c in range(n):
    if votos[c] == votos_ord[0]:
        candidatos_ord[0] = candidatos[c]
    
    if votos[c] == votos_ord[1]:
        candidatos_ord[1] = candidatos[c]
       
   
if votos_ord[0] > v_total/2:
	    print(candidatos_ord[0], 'foi o vencedor da eleição')
else:
        print('Haverá segundo turno entre:',candidatos_ord[0],candidatos_ord[1],sep='\n')
print('Total de votos:', v_total + v_b + v_n)
print('Votos válidos:', v_total)        