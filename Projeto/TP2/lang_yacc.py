import ply.yacc as yacc

import sys

from lang_lex import tokens

def p_lang_grammar(p):
    """
    program : VARBLOCK

    VARBLOCK : VARBEGIN VARS VAREND
    
    VARS : VARS VAR
    VARS : 

    VAR : intvar
    VAR : boolvar

    intvar : INTDECL NAME DECL expressionI
    intvar : INTDECL NAME
    boolvar : BOOLDECL NAME DECL expressionB

    expressionI : expressionI PLUS termI
    expressionI : expressionI MINUS termI
    expressionI : termI
    termI       : termI TIMES factorI
    termI       : termI DIVIDE factorI
    termI       : factorI

    factorI     : INTEGER
    factorI     : NAME
    factorI     : LPAREN expressionI RPAREN

    expressionB : TRUE
    expressionB : FALSE
    expressionB : expressionB AND expressionB
    expressionB : expressionB OR expressionB
    expressionB : NOT LPAREN expressionB RPAREN
    expressionB : LPAREN expressionB RPAREN

    expressionB : expressionI LT expressionI
    expressionB : expressionI LE expressionI
    expressionB : expressionI GT expressionI
    expressionB : expressionI GE expressionI
    expressionB : expressionI EQ expressionI
    expressionB : expressionI NEQ expressionI
    """

precedence = (
     ('nonassoc', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NEQ'),
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
     ('left', 'AND'),
     ('left', 'OR')
)

def p_error(p):
    print("Syntax error!: ", p)
    parser.exito = False

parser = yacc.yacc()

parser.exito = True

fonte = ""
for linha in sys.stdin:
    fonte += linha

parser.parse(fonte)

if parser.exito:
    print ("Parsing teminou com sucesso!")
