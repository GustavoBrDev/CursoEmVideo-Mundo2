lista = []

while True:

    try:
        print("\nInforme um valor que não é um número para encerrar a digitação")
        numero = int (input("Digite um número: "))
        lista.append(numero)
    except:
        print("Inserção encerrada... \n")
        break;


print(f"O maior número é: {max(lista)}")
print(f"O menor número é: {min(lista)}")