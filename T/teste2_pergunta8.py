import re

texto = """ Oh Laurindinha, vem à janela.
Verso 1 de 4
Oh Laurindinha, vem à janela.
Verso (2 de 4)
Ver o teu amor, (ai ai ai) que ele vai p'ra guerra. Verso 3 de 4
Ver o teu amor, (ai ai ai) que ele vai p ́ra guerra.
Verso 4 de 4 """

count = 0
for line in texto.split("\n"):
    # Número em r'(\d+)' tem que ser igual ao que estará em r'\1'.
    if m := re.search(r'Verso (\d+) de \1', line):
        count += 1
print(count)
