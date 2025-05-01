from time import sleep
escolha = 0

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20 + "\n")

while escolha != 1:

    reta1 = -1

    while reta1 <= 0:
        reta1 = float(input('Qual o comprimento do primeiro segmento: '))

        if reta1 <= 0:
            print("\033[1:31mInforme um comprimento válido\033[m\n")

    reta2 = -1
    while reta2 <= 0:
        reta2 = float(input('Qual o comprimento do segundo segmento: '))

        if reta2 <= 0:
            print("\033[1:31mInforme um comprimento válido\033[m\n")

    reta3 = -1
    while reta3 <= 0:
        reta3 = float(input('Qual o comprimento do terceiro segmento: '))

        if reta3 <= 0:
            print("\033[1:31mInforme um comprimento válido\033[m\n")

    print('\nAnalisando\n')
    sleep(2)

    if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
        print('As retas informadas acima \033[1;32mPODEM formar\033[m um \033[35mtriângulo\033[m')

        if reta1 == reta2 == reta3:
            print('\033[1;34mCategoria do Triângulo: EQUILÁTERO\033[m')
        elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
            print('\033[1;34mCategoria do Triângulo: ISÓSCELES\033[m')
        else:
            print('\033[1;34mCategoria do Triângulo: ESCALENO\033[m')
    else:
        print('As retas informadas acima \033[1;31mNÃO PODEM\033[m formar um \033[35mtriângulo\033[m')

    escolha = 2
    while escolha != 0 and escolha != 1:

        print("\n------------------------------")
        print("0 - Verificar novo triângulo")
        print("1 - Encerrar programa ")
        print("------------------------------")

        escolha = int(input("\nQual a sua escolha? "))

        if escolha != 0 and escolha != 1:
            print("\033[1:31mInforme uma opção válida\033[m\n")