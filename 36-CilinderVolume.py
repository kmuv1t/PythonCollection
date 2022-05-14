# Ler Altura e Raio de um cilindro e imprimir seu Volume

h = float(input('Digite a altura do cilindro: '))
r = float(input('Digite o raio do cilindro: '))

v = 3.141592 * pow(r, 2) * h
print(f'O volume do cilindro é {v}.')
