import datetime

anoAutal = datetime.datetime.now().year
ano = int ( input("Informe o seu ano de nascimento: "))

idade = anoAutal - ano

print("\nVocê tem {} anos de idade".format(idade))

sexo = input("\nInforme seu sexo [M/F]:")

if sexo.upper() == "M":

    if idade == 18:
        print("Você deve fazer o alistamento militar.")
    elif idade > 18:
        print(f"Você já deveria ter se alistado a {idade - 18} {'anos' if idade - 18 > 1 else 'ano'}")
        print(f"Seu alistamento foi em {anoAutal - (idade - 18)}")
    else:
        print(f"Você deve se alistar em {18 - idade} {'anos' if 18 - idade > 1 else 'ano'}")
        print(f"Seu alistamento será em {anoAutal + (18 - idade)}")
elif sexo.upper() == "F":

    print("Você está dispensada do alistamento militar.")