import re
# output only the lines with the following characteristics:
# 1. that contains the word hello anywhere on the line

print("1. Linhas que contêm as tags XML <(/)?[a-zA-Z]>")
inputFromUser = input(">> ")
while inputFromUser != "":
  y = re.findall(r'<\/?(?i:[a-z])+>', inputFromUser)
  if(y):
    for s in y:
      print(s)
    #print("Encontrada: ", y.group(), " em: ", y.string) 
    #(ini,fim)=y.span()
    #comp = fim-ini
    #print("na posição ", y.span()," com carateres ",comp)  
  else:
    print("hello não encontrado")
  inputFromUser = input(">> ")
