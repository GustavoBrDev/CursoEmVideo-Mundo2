escolha = 2

while escolha != 1:

    salario = 0

    while salario <= 0:
        salario = float(input("Qual o seu salário? R$ "))

        if salario <= 0:
            print("\033[1:31mInsira um salário válido\033[m\n")

    anos = 0

    while anos <= 0:
        anos = int(input("Em quantos anos você pretende pagar a casa? "))

        if anos <= 0:
            print("\033[1:31mInsira uma quantidade de anos válida \033[m\n")

    valor = 0

    while valor <= 0:
        valor = float(input("Qual o valor da casa? "))

        if valor <= 0:
            print("\033[1:31mInsira um valor válido\033[m\n")

    parcela = valor / (anos * 12);

    if parcela >= salario * 0.3:
        print(f"O valor da parcela (R${parcela:.2f}) é superior que 30% do seu salário mensal (R${salario * 0.3:.2f})")
        print("Emprestimo negado")
    else:
        print(f"O empréstimo com um valor de parcela de R${parcela:.2f} foi aprovado")

    print("\033[1:32mConsultoria realizada com sucesso!\033[m\n")

    escolha = 2

    while escolha != 0 and escolha != 1:

        print("\n------------------------------")
        print("0 - Realizar nova consultoria")
        print("1 - Encerrar programa ")
        print("------------------------------")

        escolha = int(input("\nQual a sua escolha? "))

        if escolha != 0 and escolha != 1:
            print( "\033[1:31mInforme uma opção válida\033[m\n ")

print( "Fim do programa")