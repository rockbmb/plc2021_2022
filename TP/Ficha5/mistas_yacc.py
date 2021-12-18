import ply.yacc as yacc

import sys

from mistas_lex import tokens

def p_list(p):
    "LIST : LPAREN ELS RPAREN"
    print(p[2])

def p_els_varias(p):
    "ELS : ELS VIRG EL"
    parser.conta += 1
    p[0] = p[1]
    p[0].append(p[3])

def p_els_uma(p):
    "ELS : EL"
    parser.conta = 1
    p[0] = p[1]

def p_el_num(p):
    "EL : NUM"
    parser.soma += p[1]
    p[0] = []

def p_el_bool(p):
    "EL : BOOL"
    p[0] = p[1]

def p_el_id(p):
    "EL : ID"
    parser.pals.append(p[1])
    p[0] = []

def p_error(p):
    print("Syntax error!")
    parser.exito = False

parser = yacc.yacc()
parser.conta = 0
parser.soma = 0
parser.pals = []

parser.exito = True

fonte = ""
for linha in sys.stdin:
    fonte += linha

parser.parse(fonte)

if parser.exito:
    print ("Parsing teminou com sucesso!")
    print("O total de elementos é : ", parser.conta)
    print("A soma é : ", parser.soma)
    print("As palavras são : ", parser.pals)