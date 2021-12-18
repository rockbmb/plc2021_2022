import re
frase =  input()
while frase != "":
    frase = re.sub(r'([0-9]+)(\s+\1)+', r'\1 + \2', frase)
    print(frase)
    frase = input()