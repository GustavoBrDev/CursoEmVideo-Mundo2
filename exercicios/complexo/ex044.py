escolha = 1

while escolha != 0:

  valor = 0

  while valor <= 0:
     valor = float ( input("Informe o preço do produto: R$ "))
    
     if valor <= 0:
        print("\033[1:31mInforme um valor válido\033[m")
       
  total = 0
  escolha = 4
  
  while escolha != 0 and escolha != 1 and escolha != 2 and escolha != 3:

    print("\n" + '=' * 20)
    print("| OPÇÃO |  FORMA DE PAGAMENTO  |")
    print("|   0   |  Encerrar aplicação  |")
    print("|   1   |        Á vista       |")
    print("|   2   |   Até 2x no cartão   |")
    print("|   3   | 3x ou mais no cartão |")
    print('=' * 20 + "\n")

    escolha = int ( input( "Informe a escolha: ") )

    match escolha:
          case 0:
              print("Encerrando...")
              break
          case 1:

            escolha = 0

            while escolha != 1 and escolha != 2:

              print("\n" + '=' * 20)
              print("| OPÇÃO |  FORMA DE PAGAMENTO  |")
              print("|   1   |  Dinheiro ou cheque  |")
              print("|   2   |        Cartão        |")
              print('=' * 20 + "\n")

              escolha = int(input("Informe a escolha: "))

              match escolha :
                  case 1:
                      total = valor * 0.9
                      break
                  case 2:
                      total = valor * 0.95
                      break
                  case _:
                      print("\033[1:31mInforme uma opção válida\033[m")


            break
          case 2:
            total = valor
            break
          case 3:
            total = valor * 1.2
            break
          case _:
            print("\033[1:31mInforme uma opção válida\033[m")
  
  if total != 0 :
      print(f"O valor total é de R$ {total:.2f}")
  
