import re
frase = input()
while frase != "":
    key = re.match(r'\|([^|]+)\|([^\n]*)', frase)
    if (key):
        frase = key.group(2)
        frase = re.sub(rf'({key.group(1)})-({key.group(1)})', r'\2 \1', frase)
        print(frase)
    frase = input()