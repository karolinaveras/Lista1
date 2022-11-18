altura = float(input('Digite sua altura:'))

peso = float(input('Digite o seu peso:'))

imc = altura / peso **2

if imc <= 18.5:
    print(f'Seu IMC é {imc}, você esta abaixo do peso')

elif imc == 18.5 or 24.9:
    print(f'Seu IMC é {imc}, você esta com o peso normal!')

elif imc == 25 or 29.9:
    print(f'Seu IMC é {imc}, voc~e esta com sobrepeso!')

elif imc == 30 or 34.9:
    print(f'Seu IMC é {imc} e indica obesidade Grau I')

elif
