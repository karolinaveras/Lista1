altura = float(input('Digite sua altura:'))

peso = float(input('Digite o seu peso:'))

imc = altura / peso **2

if imc <= 18.5:
    print(f'Seu IMC é {imc}, você esta abaixo do peso')

elif imc == 18.5 or 24.9:
    print(f'Seu IMC é {imc}, você esta com o peso normal!')

elif
