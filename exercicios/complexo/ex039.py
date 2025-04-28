import datetime

escolha = 0
anoAutal = datetime.datetime.now().year

while escolha != 1:

    ano = int(input("Informe o seu ano de nascimento: "))

    idade = anoAutal - ano

    if idade == 18:
        print("Você deve fazer o alistamento militar.")
    elif idade > 18:
        print(f"Você já deveria ter se alistado a {idade - 18} {'anos' if idade - 18 > 1 else 'ano'}")
    else:
        print(f"Você deve se alistar em {18 - idade} {'anos' if 18 - idade > 1 else 'ano'}")

    escolha = 2
    while escolha != 0 and escolha != 1:

        print("------------------------------")
        print("0 - Realizar nova verificação")
        print("1 - Encerrar programa ")
        print("------------------------------")

        escolha = int(input("Qual a sua escolha? "))

        if escolha != 0 and escolha != 1:
            print( "\033[1:31mInforme uma opção válida\033[m\n ")