salario = float(input("Qual o seu salário? R$ "))
anos = int(input("Em quantos anos você pretende pagar a casa? ") )
valor = float ( input( "Qual o valor da casa? " ) )

parcela = valor  / ( anos * 12 ) ;

if parcela >= salario * 0.3:
    print( f"O valor da parcela (R${parcela:.2f}) é superior que 30% do seu salário mensal (R${salario*0.3:.2f})")
    print("Emprestimo negado")
else:
    print( f"O empréstimo com um valor de parcela de R${parcela:.2f} foi aprovado")

print( "Consultoria realizada com sucesso!")