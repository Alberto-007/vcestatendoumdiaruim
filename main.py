import time
Satisfeito = ("ok")
name = input("Ola, qual seu nome?\n")
print('\n')
print("Oii " + name + " como você está hoje?") 
dia_bom = input("\nEspero que você esteja tendo um otímo dia, você esta? S/N \n")
if dia_bom == ("S"):
  print("Que bom, estou feliz que você esteja tendo um bom dia.")
  quit()
  
Meditar = input("Eita " + name + ", fico triste com isso, você gostaria de tentar e meditar? S/N \n")
if Meditar == ("S"):
  print("Respire fundo")
  time.sleep(5)
  print("Agora exale")
  time.sleep(5)
  print("Respire fundo")
  time.sleep(5)
  print("E agora exale")
  time.sleep(5)
  print("Respirando fundo dnv")
  time.sleep(5)
  print("E agr exala")
  time.sleep(5)
  Satisfeito  = input("Então " + name + ", você está satisfeito? S/N \n")
if Satisfeito == ("S"):
   print("Ok bom agora cai fora :) ")
   quit()
  

  

ler = input("seria bom você ler um livro, você quer? S/N \n")
if ler == ("S"):
  print("ok irei voltar daqui a 30 minutos")
  time.sleep(1800)
  print("você já leu por 30 minutos ")
  Satisfeito  = input("então,"+ name + " você esta satisfeito com isso?S/N \n")
if Satisfeito == ("S"):
  print("ok que bom agora cai fora XD ")
  quit()






  
music = input("você quer ouvir musica? S/N \n")
if music == ("S"):
  print("Ok eu irei voltar daqui a 15 minutos")
  time.sleep(900)
  print("voce ja ouviu musica por 15 minutos  ")
  Satisfeito  = input("então, " + name + " você esta satisfeito com isso?S/N \n")
if Satisfeito == ("S"):
  print("ok que bom agora cai fora TwT ")
  quit()
  


caminhada = input("você quer dar uma caminhada? S/N \n")
if caminhada == ("S"):
  input("Pressione ENTER quando você tiver terminado...")
  
  print("voce acabou de dar uma caminhada, que bom! ")
  Satisfeito  = input("então " + name + " você esta satisfeito com isso?S/N \n")
if Satisfeito == ("S"):
  print("ok que bom agora cai fora :3")
  quit()

print("bem " + name + " esses foram todos os metodos que eu tinha conhecimento pra melhorar seu dia, n sei mais oq dizer, ouça musica house, estoure o limite do cartao ou sla")


 
