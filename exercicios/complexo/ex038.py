lista = []

while True:

    try:
        print("\nInforme um valor que não é um número para encerrar a digitação")
        numero = int (input("Digite um número: "))
        lista.append(numero)
    except:
        print("Inserção encerrada... \n")
        break;


print(f"\033[1:34mO maior número é: {max(lista)}\033[m")
print(f"\033[1:34mO menor número é: {min(lista)}\033[m")