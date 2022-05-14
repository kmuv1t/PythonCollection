# Ler dias trabalhados do encanador e imprimir a renda líquida com o desconto de 8% pelo imposto de renda

d = int(input('Digite os dias trabalhados: '))
p = d * 30.0 - ((d * 30.0) * 0.08)
print(f'A quantia líquida com desconto de 8% ficou em R${p}')
