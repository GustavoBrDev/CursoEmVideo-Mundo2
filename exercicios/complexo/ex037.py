continuar = 2

while continuar != 1:
    numero = 0

    while numero <= 0:
        numero = int(input("Digite o número a ser convertido: "))

        if numero <= 0:
            print("O número informado é inválido. Utilize um valor inteiro positivo.")

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
            print("Opção informada inválida")

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
        print(f"A opção informada ({opcao}) é inválida!)")
        print("Tente novamente mais tarde")


    print(f"O número convertido para a {metodo}  é igual a {conversao}")

    while continuar != 0 and continuar != 1:

        print("------------------------------")
        print("0 - Realizar nova conversão")
        print("1 - Encerrar programa ")
        print("------------------------------")

        continuar = int(input("Qual a sua escolha? "))

        if continuar != 0 and continuar != 1:
            print( "Informe uma opção válida\n ")