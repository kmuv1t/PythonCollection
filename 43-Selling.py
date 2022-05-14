# Ler um valor total de um produto e imprimir o valor final

v = float(input('Digite o valor do produto: '))
vd = v - (v * 0.1)
vp = v / 3
vcd = vd * 0.05
vcp = v * 0.05
print(f'Valores:\n'
      f'- Valor com desconto de 10%: R${vd}\n'
      f'- Valor da parcela em 3x sem juros: R${vp}\n'
      f'- Comissão do vendedor da compra à vista: R${vcd}\n'
      f'- Comissão do vendedor da compra parcelada: R${vcp}')
