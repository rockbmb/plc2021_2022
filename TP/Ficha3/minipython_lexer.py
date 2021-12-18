from typing import Counter
import ply.lex as lex
import sys

tokens = ['LPAREN'
         ,'RPAREN'
         , 'COMMA'
         , 'ID'
         , 'INT'
         , 'REAL'
         , 'EQ'
         , 'PLUS'
         , 'FAC'
         , "SUB"
         , "MULT"
         , 'BOOL'
         , 'LIST'
         , "SEMICOLON"
         , 'EXP'
         ]

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA   = r','
t_SEMICOLON = r';'
t_EQ = r'='
t_PLUS = r'+'
t_FAC = '!'
t_SUB = r'-'
t_MULT = r'*'
t_LISTL = r'\['
t_LISTR = r'\]'

def t_REAL(t):
    r'[0-9]+\.[0-9]+'
    return t

def t_BOOL(t):
    r'True|False'
    return t

def t_FALSE(t):
    r'False'
    return t

def t_ID(t):
    r'[a-zA-Z]+'
    return t

def t_INT(t):
    r'\[0-9]+'
    t.value = int(t.value)
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