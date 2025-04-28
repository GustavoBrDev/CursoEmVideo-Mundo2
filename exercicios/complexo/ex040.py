escolha = 0

while escolha != 1:

    notas = []

    while True:

        try:

            nota = -1

            while nota < 0 or nota > 10:
                print("\n\033[1:35mInsira um valor não numérico para encerrar\033[m")
                nota = float(input("Insira a nota do aluno: "))

                if nota < 0 or nota > 10:
                    print("\n\033[1:31mInsira uma nota válida (0 a 10)\033[m")
                else:
                    notas.append(nota)
        except:
            if len(notas) < 2:
                print("\033[1:31mÉ preciso de ao menos duas notas para calcular uma média\033[m")
            else:
                print("\n\033[1:32mInserção realizada com sucesso!\033[m")
                break

    media = sum(notas) / len(notas)

    if media >= 7:
        print('\033[1:32mO aluno está APROVADO\033[m')
    elif media >= 5:
        print('\033[1:33mO aluno está em RECUPERAÇÃO\033[m')
    else:
        print('\033[1:31mO aluno está REPROVADO\033[m')

    escolha = 2
    while escolha != 0 and escolha != 1:

        print("\n------------------------------")
        print("0 - Calcular nova média")
        print("1 - Encerrar programa ")
        print("------------------------------")

        escolha = int(input("\nQual a sua escolha? "))

        if escolha != 0 and escolha != 1:
            print("\033[1:31mInforme uma opção válida\033[m\n")
