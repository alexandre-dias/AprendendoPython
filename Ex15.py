salario = float(input('Informe seu salário por hora: '))
horas = float(input('Informe as horas trabalhadas: '))

# Salário Bruto / Sem descontos
bruto = salario*horas
print('Salário bruto: R$', bruto)

# Salário - IR
ir = bruto*0.11
print('IR: R$', ir)

# Salário - INSS
inss = bruto*0.08
print('INSS: R$', inss)

# Salário - Sindicato
sindicato = bruto*0.05
print('Sindicato: R$', sindicato)

# Salário Liquído
liquido = bruto-ir-inss-sindicato
print('Liquído: R$', liquido)
