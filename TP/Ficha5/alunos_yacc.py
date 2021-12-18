import ply.yacc as yacc

import sys

from alunos_lex import tokens

def p_alunos_grammar(p):
    """
    TURMAS : TURMAS TURMA
    TURMAS : TURMA
    TURMA : Turma ID DPONTO ALUNOS
    ALUNOS : ALUNOS ALUNO
    ALUNOS : ALUNO
    ALUNO : Aluno ID NOTAS PONTO
    NOTAS : NOTAS VIRG NOTA
    NOTAS : NOTA
    NOTA : NUM
    """

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