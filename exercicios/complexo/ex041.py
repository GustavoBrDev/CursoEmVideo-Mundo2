import datetime

anoAtual = datetime.date.today().year
escolha = 0

while escolha != 1:

    ano = 0

    while ano <= 0:
        ano = int(input("Informe o seu ano de nascimento: "))

        if ano <= 0:
            print("\033[1:31mInforme um ano de nascimento válido\033[m")

    idade = anoAtual - ano

    print(f"\nO atleta tem {idade} {'anos' if idade > 1 else 'ano'}")

    if idade <= 9:
        print("\033[1:35mCategoria: MIRIM\033[m")
    elif idade <= 14:
        print("\033[1:35mCategoria: INFANTIL\033[m")
    elif idade <= 19:
        print("\033[1:35mCategoria: JUNIOR\033[m")
    elif idade <= 25:
        print("\033[1:35mCategoria: SENIOR\033[m")
    else:
        print("\033[1:35mCategoria: MASTER\033[m")

    escolha = 2
    while escolha != 0 and escolha != 1:

        print("\n------------------------------")
        print("0 - Verificar novo atleta")
        print("1 - Encerrar programa ")
        print("------------------------------")

        escolha = int(input("\nQual a sua escolha? "))

        if escolha != 0 and escolha != 1:
            print("\033[1:31mInforme uma opção válida\033[m\n")
