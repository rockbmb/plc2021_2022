import re
# output only the lines with the following characteristics:
# 1. that contains the word hello at the beginning of the line

print("substituição de hello na linha")
inputFromUser = input(">> ")
while inputFromUser != "":
  new_text = re.sub(r'((\+351[ ]*)?2[0-9]{8})', '*YEPPER*', inputFromUser)
  print(new_text) 
  inputFromUser = input(">> ")

  
  
