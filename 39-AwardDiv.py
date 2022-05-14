# Dividir R$780.000,00 entre três ganhadares (1° com 46%, 2° com 32%, 3° com o restante)

v = 780000.00
v1 = v * 0.46
v2 = v * 0.32
v3 = v - (v1 + v2)

print(f'O 1° ficou com {v1}, o 2° ficou com {v2} e o 3° ficou com {v3}')
