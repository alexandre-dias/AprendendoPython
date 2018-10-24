peso = float(input('Qual é o peso? '))
excesso = 50
if peso > excesso :
    print('Você ultrapassou o limite')
    multa = (peso - excesso)*4
    print('Pague R$', multa, 'de multa')
else :
    print(peso, 'Kg. Fique tranquilo! Vc ainda ñ atingiu o limite')
