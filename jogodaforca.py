import random

lista_de_palavras=["computador","notebook","liverpool","flamengo","banana","campeao","cafe","vinicius","junior","rodrigo"]
lista_de_dicas=["eletronicos","eletronicos","equipe futebol","equipe de futebol","fruta","ganhador","bebida","nome proprio","nome proprio","nome proprio"]

indice = random.randint(0,9)

palavra=lista_de_palavras[indice]
dica=lista_de_dicas[indice]

tentativas=""
turnos=5

nome=input("Digite seu nome: \n ")
print("Olá,",nome,", bem vindo ao jogo da forca, bora jogar! \n A dica é",dica,"Boa sorte")

while turnos >0:
  falhas=0
  tentativa_atual=input("Digite uma letra:  ")
  tentativas+=tentativa_atual
  for X in palavra:
    if X in tentativas:
      print(X)
    
    else:  
      print("**")
      falhas=1
  if falhas==0:  
    print ("Parabéns!, Você descobriu a palavra secreta!!!")
    break
  if tentativa_atual not in palavra:
    turnos-=1
    print("Essa letra não está na palavra secreta, Você perdeu uma vida. Você ainda tem",turnos,"Vidas restantes")
  if turnos==0:
    print("game over!!!")
    print("A palavra correta era",palavra)