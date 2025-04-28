nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('O aluno está APROVADO')
elif media >= 5:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está REPROVADO')
