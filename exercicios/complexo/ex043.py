escolha = 0
while escolha != 1:

    peso = 0
    while peso <= 0:
        peso = float(input("Insira o seu peso em KG: "))

        if peso <= 0:
            print("\033[1:31mInsira um peso válido\033[m\n")

    altura = 0

    while altura <= 0 or altura >= 3:
        altura = float(input("Insira a sua altura em metros: "))

        if altura <= 0 or altura >= 3:
            print("\033[1:31mInsira uma altura válida\033[m\n")

    imc = peso / (altura * altura)

    if imc < 18.5:
        print("\nVocê está \033[1:33mABAIXO DO PESO\033[m")
    elif imc < 25:
        print("\nVocê está no \033[1:32mPESO IDEAL\033[m")
    elif imc < 30:
        print("\nVocê está com \033[1:33mSOBREPESO\033[m")
    elif imc < 40:
        print("\nVocê está com \033[1:31mOBESIDADE\033[m")
        print("\033[1:33mProcure ajuda médica se possível\033[m")
    else:
        print("\n\033[1:31mVocê está com OBESIDADE MÓRBIDA\033[m")
        print("\033[1:31mProcure ajuda médica o quanto antes\033[m")

    escolha = 2
    while escolha != 0 and escolha != 1:

        print("\n------------------------------")
        print("0 - Calcular novo IMC")
        print("1 - Encerrar programa ")
        print("------------------------------")

        escolha = int(input("\nQual a sua escolha? "))

        if escolha != 0 and escolha != 1:
            print("\033[1:31mInforme uma opção válida\033[m\n")