AX = int(input('Digite o primeiro ponto:'))

AY = int(input('Digite o segundo ponto:'))

BX = int(input('Digite o terceiro ponto:'))

BY = int(input('Digite o quarto ponto:'))

PLANO = ((BX - AX) **2 + (BY - AY) **(1/2))

print(f"A distancia entre os dois pontos é: {PLANO}")
