altura = float(input('Digite sua altura:'))

peso = float(input('Digite o seu peso:'))

imc = altura / peso **2

if imc == 18.5:
    print(f'Seu IMC é {imc}, você esta abaixo do peso')
