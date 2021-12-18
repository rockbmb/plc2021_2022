import ply.lex as lex

import sys

tokens = (
    'VIRG',
    'PONTO',
    'DPONTO',
    'Turma',
    'Aluno',
    'ID',
    'NUM'
)
t_VIRG   = r','
t_PONTO  = r'\.'
t_DPONTO = r'\:'

def t_NUM(t):
    r'(\d)+'
    t.value = int(t.value)
    return t

def t_Aluno(t):
    r'Aluno'
    return t

def t_Turma(t):
    r'Turma'
    return t

def t_ID(t):
    r'[a-zA-Z]+'
    return t

t_ignore = ' \r\n\t'

def t_error(t):
    print('Illegal character: ' + t.value[0])
    return

lexer = lex.lex() # cria um AnaLex especifico a partir da especificação acima usando o gerador 'lex' do objeto 'lex'

# Reading input
#for linha in sys.stdin:
#    lexer.input(linha) 
#    tok = lexer.token()
#    while tok:
#        print(tok)
#        tok = lexer.token()

