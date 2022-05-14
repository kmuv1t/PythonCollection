# Ler valor A e B e imprimir o valor da hipotenusa
from math import sqrt

a = float(input('Digite o valor A: '))
b = float(input('Digite o valor B: '))

hip = sqrt(pow(a, 2) + pow(b, 2))
print(f'O valor da hipotenusa é {hip}.')
