'''5. Faça um Programa que peça para o usuário digitar 4 notas de
avaliação bimestrais e mostre a soma total das notas e a sua
média.
'''


n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))

nota = (n1 + n2 + n3 + n4)
media = (nota/4)

print(f'A soma das notas é: {nota} e a média é igual a: {media}')

