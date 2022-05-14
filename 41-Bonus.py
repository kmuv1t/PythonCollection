# Ler o valor da hora de trabalho e horas trabalhadas e imprimir o salário final do funcionário adicionando 10%

vh = float(input('Digite o valor da hora de trabalho em R$: '))
ht = float(input('Digite o número de horas trabalhadas: '))

vt = (ht * vh) * 1.1
print(f'O salário com acréscimo de 10% ficou em R${vt}')
