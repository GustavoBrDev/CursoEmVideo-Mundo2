peso = float ( input("Insira o seu peso em KG: ") )
altura = float ( input("Insira a sua altura em metros: ") )

imc = peso / ( altura * altura )

if imc < 18.5:
    print("Você está ABAIXO DO PESO")
elif imc < 25:
    print("Você está no PESO IDEAL")
elif imc < 30:
    print("Você está com SOBREPESO")
elif imc < 40:
    print("Você está com OBESIDADE")
    print("Procure ajuda médica se possível")
else:
    print("Você está com OBESIDADE MÓRBIDA")
    print("Procure ajuda médica o quanto antes")