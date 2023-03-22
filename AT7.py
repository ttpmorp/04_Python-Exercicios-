'''7. Faça um programa para uma loja de tintas. O programa deverá
pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3
metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades
de latas de tinta a serem compradas e o preço total.'''
import math

a = float(input('Qual o tamanho em metro quadrado da área que será pintada? '))

cobertura_litro = 3.0
preco_lata = 80.0
capacidade_lata = 18


litro = a / cobertura_litro
latas = litro / capacidade_lata

qtdlatas = math.ceil(latas)


print(f'Você precisará comprar {qtdlatas} latas de tintas para pintar a área desejada e gastará R${preco_lata * qtdlatas}.')
