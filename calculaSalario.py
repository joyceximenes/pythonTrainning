# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_hora = float(input('Quanto voce ganha por hora? '))
horas_mes = float(input('Digite a quantidade de horas trabalhadas por mes: '))

salario_bruto = ganho_hora * horas_mes
imposto = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_minimo = salario_bruto - imposto - inss - sindicato

print('salario bruto =', salario_bruto)
print('imposto = ', imposto)
print('inss= = ', inss)
print('sindicato = ', sindicato)
print('salario minimo = ', salario_minimo)
