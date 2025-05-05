valor = float ( input("Informe o preço do produto: R$ "))
total = 0

print("\n" + '=' * 20)
print("| OPÇÃO |  FORMA DE PAGAMENTO  |")
print("|   1   |        Á vista       |")
print("|   2   |   Até 2x no cartão   |")
print("|   3   | 3x ou mais no cartão |")
print('=' * 20 + "\n")

escolha = int ( input( "Informe a escolha: ") )

if escolha == 1:

    print("\n" + '=' * 20)
    print("| OPÇÃO |  FORMA DE PAGAMENTO  |")
    print("|   1   |  Dinheiro ou cheque  |")
    print("|   2   |        Cartão        |")
    print('=' * 20 + "\n")

    escolha = int(input("Informe a escolha: "))

    if escolha == 1:
        total = valor * 0.9
    elif escolha == 2:
        total = valor * 0.95
    else:
        print("Informe uma opção válida")

elif escolha == 2:

    total = valor
    print(f"\nO valor da parcela é de R$ {total / 2:.2f}")

elif escolha == 3:

    total = valor * 1.2
    parcelas = int(input("\nInforme o número de parcelas: "))

    if parcelas >= 3:
        print(f"\nO valor da parcela é de R$ {total / parcelas:.2f}")
    else:
        print("Informe uma opção válida")

else:
    print("Informe uma opção válida")

if total != 0 :
    print(f"\nO valor total é de R$ {total:.2f}")

print("Encerrando...")
