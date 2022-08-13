# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros = float(input('Digite a quantia de metros quadrados: '))
qtd_litros = metros / 3

qtd_latas = int(qtd_litros/18)
preco_latas = qtd_latas * 80


print('Quantidade de latas: ', qtd_latas)
print('Preço total: ', preco_latas)
