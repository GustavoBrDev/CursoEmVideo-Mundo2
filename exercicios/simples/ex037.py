numero = int ( input("Digite o número a ser convertido: "))

print( "-------------------------")
print( "| OPÇÃO |   CONVERSÃO   |")
print( "|   1   |    Binário    |")
print( "|   2   |     Octal     |")
print( "|   3   |  Hexadecimal  |")
print( "-------------------------")

opcao = int ( input("Selecione a opção desejada: "))
conversao = 0

if opcao == 1:
    conversao = bin(numero)[2:]
elif opcao == 2:
    conversao = oct(numero)[2:]
elif opcao == 3:
    conversao = hex(numero)[2:]
else:
    print(f"A opção informada ({opcao}) é inválida!)")
    print( "Tente novamente mais tarde")

if conversao != 0:
    print( f"O número convertido é igual a {conversao}" )