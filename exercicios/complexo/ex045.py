import random
from time import sleep

escolha = -1

# PEDRA, PAPEL, TESOURA
# JOGADOR, COMPUTADOR
jogadas = [
    [0, 0, 0],
    [0, 0, 0]
]

# JOGADOR, COMPUTADOR, EMPATE
vitorias = [0, 0, 0]

while escolha != 0:

  escolha = -1

  while escolha < 0 or escolha > 3:
    print( "\n" + '=' * 20 )
    print( "| OPÇÃO | SUA JOGADA |")
    print( "|   0   |  DESISTIR  |")
    print( "|   1   |    PEDRA   |" )
    print( "|   2   |    PAPEL   |" )
    print( "|   3   |  TESOURA   |" )
    print( '=' * 20 )

    escolha = int ( input ( "\nEscolha uma opção: " ) )

    if escolha < 0 or escolha > 3:
      print ( "\n\033[1:31mOpção inválida, tente novamente\033[m" )
    
  computador = random.randint ( 1, 3 )

  match escolha:
  
    case 0:
        break
    case 1:

      print ( "\n\033[1:34mVocê escolheu PEDRA\033[m" )
      jogadas[0][0] += 1

      if computador == 1:
        jogadas[1][0] += 1
        vitorias [2] += 1
        print ( "\nComputador escolheu PEDRA" )
        print ( "\033[1:37mEMPATE\033[m" )
      elif computador == 2:
        jogadas[1][1] += 1
        vitorias [1] += 1
        print ( "\nComputador escolheu PAPEL" )
        print ( "\033[1:31mCOMPUTADOR VENCE\033[m" )
      else:
        jogadas[1][2] += 1
        vitorias [0] += 1
        print ( "\nComputador escolheu TESOURA" )
        print ( "\033[1:32mVOCÊ VENCE\033[m" )
        
    case 2:
      print ( "\n\033[1:34mVocê escolheu PAPEL\033[m" )
      jogadas[0][1] += 1
  
      if computador == 1:
        jogadas[1][0] += 1
        vitorias [0] += 1
        print ( "\nComputador escolheu PEDRA" )
        print ( "\033[1:32mVOCÊ VENCE\033[m" )
      elif computador == 2:
        jogadas[1][1] += 1
        vitorias [2] += 1
        print ( "\nComputador escolheu PAPEL" )
        print ( "\033[1:37mEMPATE\033[m" )
      else:
        jogadas[1][2] += 1
        vitorias [1] += 1
        print ( "\nComputador escolheu TESOURA" )
        print("\033[1:31mCOMPUTADOR VENCE\033[m")
    case 3:
      print ( "\n\033[1:34mVocê escolheu TESOURA\033[m" )
      jogadas[0][2] += 1
  
      if computador == 1:
        jogadas[1][0] += 1
        vitorias [1] += 1
        print ( "\nComputador escolheu PEDRA" )
        print ( "\033[1:31mCOMPUTADOR VENCE\033[m" )
      elif computador == 2:
        jogadas[1][1] += 1
        vitorias [0] += 1
        print ( "\nComputador escolheu PAPEL" )
        print ( "\033[1:32mVOCÊ VENCE\033[m" )
      else:
        jogadas[1][2] += 1
        vitorias [2] += 1
        print ( "\nComputador escolheu TESOURA" )
        print ( "\033[1:37mEMPATE\033[m" )


# TABELA DE JOGADAS
print ( "\n" + '=' * 40 )
print ( "| COMPETIDOR | PEDRA | PAPEL | TESOURA |" )
print ( f"|  JOGADOR   |  {jogadas[0][0]}    |   {jogadas[0][1]}   |   {jogadas[0][2]}     | " )
print ( f"| COMPUTADOR |  {jogadas[1][0]}    |   {jogadas[1][1]}   |   {jogadas[1][2]}     | " )
print ( '=' * 40 )

# TABELA DE VITÓRIAS
print ( "\n" + '=' * 50 )
print ( "| COMPETIDOR | VITÓRIAS | DERROTAS | PERCENTUAL |" )
print ( f"|  JOGADOR   |    {vitorias[0]}     |    {vitorias[1]}    | { round ( vitorias[0] / ( vitorias[0] + vitorias[1] ) * 100, 2 )} " )
print ( f"| COMPUTADOR |    {vitorias[1]}     |    {vitorias[0]}    | { round ( vitorias[1] / ( vitorias[0] + vitorias[1] ) * 100, 2 )} " )
print ( '=' * 50 )

# OUTROS RESULTADOS
print ( "\n" + '=' * 15 )
print ( f"| EMPATES | {vitorias[2]} |" )
print ( f"| TOTAL   | {vitorias[0] + vitorias[1] + vitorias[2]} |" )
print ( '=' * 15 )

if vitorias[0] != vitorias[1]:
  print ( "\nO VENCENDOR É ...")

sleep(3)

if vitorias[0] > vitorias[1]:
  print ( "\033[1:32mJOGADOR\033[m" )
elif vitorias[0] < vitorias[1]:
  print ( "\033[1:31mCOMPUTADOR\033[m" )
else:
  print ( "\033[1:37mHOUVE UM EMPATE\033[m" )

print("\nFIM DO JOGO")
