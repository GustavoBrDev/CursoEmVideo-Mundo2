import datetime

anoAutal = datetime.datetime.now().year
ano = int ( input("Informe o seu ano de nascimento: "))

idade = anoAutal - ano

if idade == 18:
    print("Você deve fazer o alistamento militar.")
elif idade > 18:
    print(f"Você já deveria ter se alistado a {idade - 18} {'anos' if idade - 18 > 1 else 'ano'}")
else:
    print(f"Você deve se alistar em {18 - idade} {'anos' if 18 - idade > 1 else 'ano'}")