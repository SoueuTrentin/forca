import os, time
from funcoes import limparTela, aguarde, forca
limparTela ()

acabouJogo = False

while True:
     print (" Bem vindos ao Jogo da Forca! ")
     nomeDesafiante = input ("Qual o nome do desafiante? ")
     nomeCompetidor = input ("Qual o nome do competidor? ")
     aguarde (1)
     limparTela ()

     palavraChave = input ("Desafiante, escolha a palavra chave para o jogo do forca: ")
     letrasAdivinhadas = []
     vidas = 6
     ganhou = False

     print (f" Agora, decida três dicas para ajudar o {nomeCompetidor} acertar a palavra chave: ")
     dica1 = input ("Dica número 1: ")
     dica2 = input ("Dica número 2: ")
     dica3 = input (" Dica número 3: ")
     dicas = [dica1, dica2, dica3]
     contador = 0
     aguarde (1)
     limparTela ()
     while True  :
          limparTela ()
          forca (vidas)
          for letra in palavraChave:
               if letra in letrasAdivinhadas:
                    print (letra, end=" ")

               else:
                    print ("*", end=" ")
          print ( "\n",f"você tem {vidas} chances restantes.")
          jogada = input (f"{nomeCompetidor}, você deseja arriscar uma letra(0) ou receber uma dica(1) ? ")
          if jogada == "1":
               contador = contador + 1
               if contador == 1 and jogada == "1":
                    print (dicas[0])
                    aguarde (3)
               elif contador == 2 and jogada == "1":
                    print (dicas[1])
                    aguarde (3)
               elif contador == 3 and jogada == "1":
                    print (dicas[2])
                    aguarde (3)
               elif contador >= 3:
                    print ("Você não tem mais dicas! ")
                    aguarde (3)
               tentativa = str (input ("escolha uma letra para adivinhar: "))
               letrasAdivinhadas.append(tentativa)
               if tentativa not in palavraChave:
                         vidas = vidas -1
                         aguarde (1)
          

          elif jogada == "0" :
               tentativa = str (input ("escolha uma letra para adivinhar: "))
               letrasAdivinhadas.append(tentativa)
               if tentativa not in palavraChave:
                         vidas = vidas -1
                         aguarde(1)
          else:
               print ("Tentativa inválida, tente novamente. ")
          ganhou = True
          for letra in palavraChave:
               if letra not in letrasAdivinhadas:
                    ganhou = False
          else:
                    pass
          if ganhou:
               limparTela ()
               print (f"Parabens {nomeCompetidor}, você ganhou! ")
               print ()
               print (" A palavra chave era :", palavraChave)
          elif vidas == 0:
               limparTela()
               print ("|      (_)   ")
               print ("|      /|\   ")
               print ("|      / \    ")
               print ()
               print (f"{nomeDesafiante}, você perdeu!")
               print ()
               print (" A palavra chave era :", palavraChave)
          else :
               limparTela()
               print (f" Parabens {nomeDesafiante}, você ganhou!")
               print ()
               print (" A palavra chave era :", palavraChave)
          if vidas == 0 or ganhou:
               break 
     
     print ("Voce deseja jogar novamente (0) ou abandonar o jogo (1)? ")
     jogarNovamente = input()
     if jogarNovamente == "0":
           print ("Reiniciando game! ")
           aguarde (3)
           limparTela()

     elif jogarNovamente == "1":
          limparTela()
          break
          
     else:
           print ("opção inválida! ")
