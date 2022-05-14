# Ler número de 3 digitos (100 a 999)

num = int(input('Digite um número entre 100 e 999: '))
if num < 100 or num > 999:
    print('Digite um número de 3 digitos.')
else:
    c = str(num)
    print(f'Seu número invertido fica: {c[::-1]}')
