# entrada
sexo = input()
peso = int(input())
alt = int(input())

if sexo == 'M':
    if peso <= 70 and alt <= 165:
        print('LX-39')
    if 70 < peso <= 100 and alt <= 165:
        print('LX-40')
    if 100 < peso:
        print('CX-102')
    if peso <= 80 and 165 < alt <= 190:
        print('BW-02')
    if (80 < peso <= 100 and 165 < alt <= 190) or (peso <= 80 and 190 < alt):
        print('MM-107')
if sexo == 'F':
    if  alt <= 140:
        print('LX-38')
    if  (peso <= 70  and 140 < alt <= 170) or (70 < peso <= 90 and 140 < alt <= 155):
        print('BW-03')
    if (90 < peso and 140 < alt <= 170) or (70 < peso <= 90 and 155 < alt <= 170):
        print('CX-101')
    if peso <= 90 and 170 < alt:
        print('BW-02')
    if 90 < peso and 170 < alt:
        print('CX-102')