import random

print( "\n" + '=' * 20 )
print( "| OPÇÃO | SUA JOGADA |")
print( "|   1   |    PEDRA   |" )
print( "|   2   |    PAPEL   |" )
print( "|   3   |  TESOURA   |" )
print( '=' * 20 )

escolha = int ( input ( "\nEscolha uma opção: " ) )
computador = random.randint ( 1, 3 )

if escolha == 1:
  print ( "\nVocê escolheu PEDRA" )

  if computador == 1:
    print ( "\nComputador escolheu PEDRA" )
    print ( "EMPATE" )
  elif computador == 2:
    print ( "\nComputador escolheu PAPEL" )
    print ( "COMPUTADOR VENCE" )
  else:
    print ( "\nComputador escolheu TESOURA" )
    print ( "VOCÊ VENCE" )

elif escolha == 2:
  print ( "\nVocê escolheu PAPEL" )

  if computador == 1:
    print ( "\nComputador escolheu PEDRA" )
    print ( "VOCÊ VENCE" )
  elif computador == 2:
    print ( "\nComputador escolheu PAPEL" )
    print ( "EMPATE" )
  else:
    print ( "\nComputador escolheu TESOURA" )
    print ( "COMPUTADOR VENCE" )
    
elif escolha == 3:
  print ( "\nVocê escolheu TESOURA" )

  if computador == 1:
    print ( "\nComputador escolheu PEDRA" )
    print ( "COMPUTADOR VENCE" )
  elif computador == 2:
    print ( "\nComputador escolheu PAPEL" )
    print ( "VOCÊ VENCE" )
  else:
    print ( "\nComputador escolheu TESOURA" )
    print ( "EMPATE" )

else:
  print ( "\nOpção inválida" )
