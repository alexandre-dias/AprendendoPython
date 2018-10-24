aux = 0
somaInteiro = 0
cnt = 0

# Inteiro
while aux < 2 :
    cnt = cnt+1
    inteiro = int(input('Informe o '+ str(cnt) + 'º número: '))
    somaInteiro += inteiro
    aux = aux+1

# Real
real = float(input('Informe o número real: '))

# Cálculo
resultadoUm = (somaInteiro*2)+(real/2)
print('A: ', resultadoUm)
resultadoDois = (somaInteiro*3)+real
print('B: ', resultadoDois)
resultadoTres = real**3
print('C: ', resultadoTres)
