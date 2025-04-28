import datetime

anoAtual = datetime.date.today().year
anoNascimento = int( input("Informe o ano de nascimento do atleta: "))

idade = anoAtual - anoNascimento

print(f"\nO atleta tem {idade} { 'anos' if idade > 1 else 'ano' }")

if idade <= 9:
    print("Categoria: MIRIM")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JUNIOR")
elif idade <= 25:
    print("Categoria: SENIOR")
else:
    print("Categoria: MASTER")
