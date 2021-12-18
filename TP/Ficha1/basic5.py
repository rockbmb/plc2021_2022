import re


print("Split de uma linha por virgulas")

inputFromUser = input(">> ")

while inputFromUser != "":
  lista = re.split(r'[0-9]+', inputFromUser, maxsplit=2)
  for i in lista:
    print(i) 
  inputFromUser = input(">> ")

  
  
