# ------------------------------------------------------------
# somador-ply.py
#
# somador de números
# tokens: on, off, = e \d+
# ------------------------------------------------------------
import ply.lex as lex
import sys

# Declare the state
states = (
   ('semaforo','inclusive'),
)
 
# List of token names.   This is always required
tokens = (
    'ON',
    'OFF',
    'DISPLAY',
    'NUMBER'
)
 
# Regular expression rules for tokens in initial state
def t_ON(t):
    r'[Oo][Nn]'
    t.lexer.begin('semaforo')
 
def t_DISPLAY(t):
    r'='
    print("soma = ", t.lexer.soma)
 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule: remaining chars
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# ---------------------------------------------------------------
# Regular expression rules for tokens in semaforo state
def t_semaforo_OFF(t):
    r'[oO][fF][fF]'
    t.lexer.begin('INITIAL')

def t_semaforo_NUMBER(t):
    r'\d+'
    t.lexer.soma += int(t.value)  


# Build the lexer
lexer = lex.lex()

# My state
lexer.soma = 0
 
# Reading input
for linha in sys.stdin:
    lexer.input(linha) 
    tok = lexer.token()
    while tok:
        #print(tok)
        tok = lexer.token()

print("A soma calculada final e: ", lexer.soma)
      
