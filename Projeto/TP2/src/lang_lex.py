import ply.lex as lex

import sys

t_PLUS     = r'\+'
t_MINUS    = r'\-'
t_TIMES    = r'\*'
t_DIVIDE   = r'\/'
t_ATTRIB   = r'\<\-'
t_Decl     = r'\='
t_LPAREN   = r'\('
t_RPAREN   = r'\)'

t_GT       = r'\>'
t_GE       = r'\>\='
t_LT       = r'\<'
t_LE       = r'\<\='
t_EQ       = r'\=\='
t_NEQ      = r'\!\='

t_AND      = r'\&\&'
t_OR       = r'\|\|'
t_NOT      = r'\~'

reserved = {
    'DeclBegin' : 'DeclBegin',
    'DeclEnd' : 'DeclEnd',
    'int' : 'IntDecl',
    'bool' : 'BoolDecl',
    'string' : 'StringDecl'
}

def t_Name(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'Name')
    return t

def t_Integer(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_String(t):
    r'\".*\"'
    return t

def t_Bool(t):
    r'True|False'
    import distutils.util
    t.value = bool(distutils.util.strtobool(t.value))
    return t

t_ignore = ' \r\n\t'

def t_error(t):
    print('Illegal character: ' + t.value[0])
    return

tokens = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ATTRIB',
    'Decl',
    'LPAREN',
    'RPAREN',

    "GT",
    "GE",
    "LT",
    "LE",
    "EQ",
    "NEQ",
    'AND',
    'OR',
    'NOT',

    'Name',
    'Integer',
    'String',
    'Bool'
] + list(reserved.values())

lexer = lex.lex() # cria um AnaLex especifico a partir da especificação acima usando o gerador 'lex' do objeto 'lex'

# Reading input
#for linha in sys.stdin:
#    lexer.input(linha) 
#    tok = lexer.token()
#    while tok:
#        print(tok)
#        tok = lexer.token()