import ply.yacc as yacc
import os

import sys

from lang_lex import tokens

def p_lang_grammar(p):
    "Program : DeclBlock"

def p_lang_decls(p):
    "DeclBlock : DeclBegin Vars DeclEnd"
    
def p_lang_vars(p):
    """
    Vars : Vars Var
    Vars : 
    """

def p_lang_var(p):
    """
    Var : intvar
    Var : boolvar
    Var : stringvar
    """

def p_lang_intvar(p):
    "intvar : IntDecl Name Decl Integer"
    parser.vars[p[2]] = p[4]
    parser.types[p[2]] = int

def p_lang_intvar_default(p):
    "intvar : IntDecl Name"
    parser.vars[p[2]] = 0
    parser.types[p[2]] = int

def p_lang_boolvar(p):
    "boolvar : BoolDecl Name Decl Bool"
    parser.vars[p[2]] = p[4]
    parser.types[p[2]] = bool

def p_lang_boolvar_default(p):
    "boolvar : BoolDecl Name"
    parser.vars[p[2]] = False
    parser.types[p[2]] = bool

def p_lang_stringvar(p):
    "stringvar : StringDecl Name Decl String"
    parser.vars[p[2]] = p[4]
    parser.types[p[2]] = str

def p_lang_stringvar_default(p):
    "stringvar : StringDecl Name"
    parser.vars[p[2]] = ""
    parser.types[p[2]] = str

def p_lang_rest(p):
    """
    expressionI : expressionI PLUS termI
    expressionI : expressionI MINUS termI
    expressionI : termI
    termI       : termI TIMES factorI
    termI       : termI DIVIDE factorI
    termI       : factorI

    factorI     : Integer
    factorI     : Name
    factorI     : LPAREN expressionI RPAREN

    expressionB : Bool
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
parser.vars = {}
parser.types = {}


parser.exito = True

testfile1_name = 'test/test2.mylang'

def find_test_file(filename):
    parentdir = os.path.split(os.path.dirname(__file__))[0]
    testfile_name = os.path.join(parentdir, filename)
    testfile = open(testfile_name, r'r', encoding="utf-8")
    return testfile.read()

input_code = find_test_file(testfile1_name)
parser.parse(input_code)

if parser.exito:
    print ("Parsing teminou com sucesso!")
    print (input_code)
    print(parser.vars)
    print(parser.types)
