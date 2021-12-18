from typing import Counter
import ply.lex as lex
import sys

tokens = ['LPAREN', 'RPAREN', 'VIRG', 'REAL', 'IDENTI', 'BOOL', 'NUM']

t_LPAREN = r'\['
t_RPAREN = r'\]'
t_VIRG   = r'[;,]'

def t_REAL(t):
    r'([1-9][0-9]*\.[0-9]+|0\.[0-9]+)'
    return t

def t_BOOL(t):
    r'True|False'
    return t

def t_FALSE(t):
    r'False'
    return t

def t_IDENTI(t):
    r'[a-zA-Z]+'
    return t

soma = 0
def t_NUM(t):
    r'\[0-9]+'
    global soma
    soma += int(t.value)
    return t

t_ignore = ' \r\n\t'

def t_error(t):
    print('Illegal character: ' + t.value[0])
    return


lexer = lex.lex() # cria um AnaLex especifico a partir da especificação acima usando o gerador 'lex' do objeto 'lex'

# Reading input
for linha in sys.stdin:
    lexer.input(linha) 
    tok = lexer.token()
    while tok:
        print(tok)
        print(f'SOMA: {soma}')
        tok = lexer.token()