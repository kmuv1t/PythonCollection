# Ler salário e imprimir o cálculo do salário a ser recebido.

sal = float(input('Digite o seu salário: '))
pag = (sal * 1.05) - (sal * 0.07)
print(f'Seu salário final com acréscimo de 5% e imposto de 7% ficou em: {pag}')
