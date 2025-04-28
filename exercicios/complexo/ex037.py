continuar = 2

while continuar != 1:
    numero = 0

    while numero <= 0:
        numero = int(input("Digite o número a ser convertido: "))

        if numero <= 0:
            print("\033[1:31mO número informado é inválido. Utilize um valor inteiro positivo.\033[m")

    opcao = 0

    while opcao != 1 and opcao != 2 and opcao != 3:
        print("-------------------------")
        print("| OPÇÃO |   CONVERSÃO   |")
        print("|   1   |    Binário    |")
        print("|   2   |     Octal     |")
        print("|   3   |  Hexadecimal  |")
        print("-------------------------")

        opcao = int(input("Selecione a opção desejada: "))

        if opcao != 1 and opcao != 2 and opcao != 3:
            print("\033[1:31mInforme uma opção válida\033[m\n ")

    conversao = 0
    metodo = ""

    if opcao == 1:
        conversao = bin(numero)[2:]
        metodo = "base binária"
    elif opcao == 2:
        conversao = oct(numero)[2:]
        metodo = "base octal"
    elif opcao == 3:
        conversao = hex(numero)[2:]
        metodo = " base hexadecimal"
    else:
        print("f\033[1:31mA opção informada ({opcao}) é inválida!\033[m\n ")
        print("\033[1:31mTente novamente mais tarde\033[m\n ")


    print(f"\033[1:32mO número convertido para a {metodo} é igual a {conversao}\033[m\n")

    while continuar != 0 and continuar != 1:

        print("\n------------------------------")
        print("0 - Realizar nova conversão")
        print("1 - Encerrar programa ")
        print("------------------------------")

        continuar = int(input("\nQual a sua escolha? "))

        if continuar != 0 and continuar != 1:
            print("\033[1:31mInforme uma opção válida\033[m\n ")