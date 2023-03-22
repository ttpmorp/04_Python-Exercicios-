'''4. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total
do seu salário no referido mês.
'''

valor = int(input('Quanto você ganha por hora? '))

hora = int(input('Quantas horas você trabalha no mês? '))

salario = valor * hora

print(f'Você recebe por mês: R${salario}')

