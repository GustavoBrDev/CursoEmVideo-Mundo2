import datetime

escolha = 0
anoAutal = datetime.datetime.now().year

while escolha != 1:

    ano = 0

    while ano <= 0:
        ano = int(input("Informe o seu ano de nascimento: "))

        if ano <= 0:
            print("\033[1:31mInforme um ano de nascimento válido\033[m")

    idade = anoAutal - ano

    print("\nVocê tem {} anos de idade".format(idade))

    sexo = ""

    while sexo.upper() != "F" and sexo.upper() != "M":
        sexo = input("\nInforme seu sexo [M/F]: ")

        if sexo.upper() != "F" and sexo.upper() != "M":
            print("\033[1:31mInforme um sexo válido\033[m")

    if idade == 18:
        print("\033[1:31mVocê deve fazer o alistamento militar.\033[m")
    elif idade > 18:
        print(f"\033[1:33mVocê já deveria ter se alistado a {idade - 18} {'anos' if idade - 18 > 1 else 'ano'}\033[m")
        print(f"Seu alistamento foi em {anoAutal - (idade - 18)}")
    else:
        print(f"\033[1:33mVocê deve se alistar em {18 - idade} {'anos' if 18 - idade > 1 else 'ano'}\033[m")
        print(f"Seu alistamento será em {anoAutal + (18 - idade)}")

    escolha = 2
    while escolha != 0 and escolha != 1:

        print("\n------------------------------")
        print("0 - Realizar nova verificação")
        print("1 - Encerrar programa ")
        print("------------------------------")

        escolha = int(input("\nQual a sua escolha? "))

        if escolha != 0 and escolha != 1:
            print( "\033[1:31mInforme uma opção válida\033[m\n ")