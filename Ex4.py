def inicio() :
    contador = 0
    media = 0
    soma = 0
    cnt = 0
    while contador < 4 :
        cnt = cnt+1
        n1 = float(input('Informe a '+ str(cnt) +'º nota: '))
        contador = contador+1
        soma += n1 # Incrementa (soma) o valor do while
        media = soma/4
    # print(soma) -- Exibe a soma
    print(media)
inicio()


