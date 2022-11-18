altura = float(input('Digite sua altura:'))

peso = float(input('Digite o seu peso:'))

imc = peso / altura **2

if imc <= 18.5:
    print(f'Seu IMC é {imc}, você esta abaixo do peso!')

elif imc == 18.5 and 24.9:
    print(f'Seu IMC é {imc}, você esta com o peso normal!')

elif imc == 25 and 29.9:
    print(f'Seu IMC é {imc}, você esta com sobrepeso!')

elif imc == 30 and 34.9:
    print(f'Seu IMC é {imc} e indica obesidade Grau I!')

elif imc == 35 and 39.9:
    print(f'Seu IMC é {imc}, você está com obesidade de grau II!')

elif imc >= 40:
    print(f'Seu IMC é {imc}, você esá com obesidade mórbida!')

else:
    print('IMC Invalido!')