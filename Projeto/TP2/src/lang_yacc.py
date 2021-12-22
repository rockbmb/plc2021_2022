import ply.yacc as yacc
import os

import sys

from lang_lex import tokens

def p_lang_grammar(p):
    "Program : DeclBlock CommandBlock"
    p[0] = p[1]
    p[0].append("start\n")
    p[0] += p[2]
    print(p[0])
    if parser.exito:
        parser.program = ''.join(p[0])

def p_lang_decls(p):
    "DeclBlock : DeclBegin Vars DeclEnd"
    p[0] = p[2]

def p_lang_vars_1(p):
    "Vars : Vars Var"
    p[0] = p[1]
    p[0] += p[2]

def p_lang_vars_2(p):
    "Vars : Var"
    p[0] = p[1]

def p_lang_var_int(p):
    "Var : intvar"
    p[0] = p[1]

def p_lang_var_bool(p):
    "Var : boolvar"
    p[0] = p[1]

def p_lang_var_str(p):
    "Var : stringvar"
    p[0] = p[1]

def p_lang_intvar(p):
    "intvar : IntDecl Name Decl Integer"
    parser.var_values[p[2]] = p[4]
    parser.var_types[p[2]] = int
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"pushi {parser.var_values[p[2]]}\n"]

def p_lang_intvar_default(p):
    "intvar : IntDecl Name"
    parser.var_values[p[2]] = 0
    parser.var_types[p[2]] = int
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"pushi {0}\n"]

def p_lang_boolvar(p):
    "boolvar : BoolDecl Name Decl Bool"
    parser.var_values[p[2]] = p[4]
    parser.var_types[p[2]] = bool
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"pushi {int(parser.var_values[p[2]])}\n"]

def p_lang_boolvar_default(p):
    "boolvar : BoolDecl Name"
    parser.var_values[p[2]] = False
    parser.var_types[p[2]] = bool
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"pushi {int(False)}\n"]

def p_lang_stringvar(p):
    "stringvar : StringDecl Name Decl String"
    parser.var_values[p[2]] = p[4]
    parser.var_types[p[2]] = str
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"pushs {parser.var_values[p[2]]}\n"]

def p_lang_stringvar_default(p):
    "stringvar : StringDecl Name"
    parser.var_values[p[2]] = ""
    parser.var_types[p[2]] = str
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    empty = r'""'
    p[0] = [f"pushs {empty}\n"]

def p_lang_commandblock_1(p):
    "CommandBlock : CommandBlock Command"
    p[0] = p[1]
    p[0] += p[2]

def p_lang_commandblock_2(p):
    "CommandBlock : Command"
    p[0] = p[1]

def p_lang_command_1(p):
    "Command : Assign"
    p[0] = p[1]

def p_lang_command_assign_int(p):
    "Assign : Name ASSIGN ExpressionI"
    if parser.var_types[p[1]] not in [int, bool]:
        line   = p.lineno(2)        # line number of the ASSIGN token
        index  = p.lexpos(2)        # Position of the ASSIGN token
        print("Error: assigning integer expression to non-integer variable;")
        s = "{...}"
        print(f"Wrong types in variable assignment in line number {line}, character {index}: \n{' '.join(map(str, p[1:3]))} {s}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = p[3]
        p[0].append(f'storeg {parser.var_stack_loc[p[1]]}\n')

def p_lang_command_assign_2(p):
    "Assign : Name ASSIGN ExpressionB"
def p_lang_command_assign_3(p):
    "Assign : Name ASSIGN String"
def p_lang_command_assign_4(p):
    "Assign : Name ASSIGN ReadString"

#def p_lang_command_2(p):
#    "Command : IfThenElse"
#def p_lang_command_3(p):
#    "Command : While"

def p_lang_command_4(p):
    "Command : IOCommand"

def p_lang_command_IO_1(p):
    "IOCommand : ReadString"

def p_lang_command_IO_2(p):
    "IOCommand : WriteString"

def p_lang_expressionI_plus(p):
    "ExpressionI : ExpressionI PLUS TermI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("add\n")

def p_lang_expressionI_minus(p):
    "ExpressionI : ExpressionI MINUS TermI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("sub\n")

def p_lang_expressionI_termI(p):
    "ExpressionI : TermI"
    p[0] = p[1]

def p_lang_termI_mul(p):
    "TermI       : TermI TIMES factorI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("mul\n")

def p_lang_termI_div(p):
    "TermI       : TermI DIVIDE factorI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("div\n")

def p_lang_termI(p):
    "TermI       : factorI"
    p[0] = p[1]

def p_lang_factorI_int(p):
    "factorI     : Integer"
    p[0] = [f"pushi {p[1]}\n"]

def p_lang_factorI_var(p):
    "factorI     : Name"
    if parser.var_types[p[1]] not in [int, bool]:
        line   = p.lineno(2)        # line number of the ASSIGN token
        index  = p.lexpos(2)        # Position of the ASSIGN token
        print("Error: integer expression with non-integer variable;")
        s = "{...}"
        print(f"Expression in line number {line}, character {index}: \n{s} {p[1]} {s}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        # Usa-se "int" sobre o valor da variável no estado do parser para o
        # caso de não ser do tipo "int", mas ser numérica: bool, float, etc.
        p[0] = [f'pushg {int(parser.var_stack_loc[p[1]])}\n']

def p_lang_factorI_paren(p):
    "factorI     : LPAREN ExpressionI RPAREN"
    p[0] = p[2]

def p_lang_rest_2(p):
    """
    ExpressionB : Bool
    ExpressionB : ExpressionB AND ExpressionB
    ExpressionB : ExpressionB OR ExpressionB
    ExpressionB : NOT LPAREN ExpressionB RPAREN
    ExpressionB : LPAREN ExpressionB RPAREN

    ExpressionB : ExpressionI LT ExpressionI
    ExpressionB : ExpressionI LE ExpressionI
    ExpressionB : ExpressionI GT ExpressionI
    ExpressionB : ExpressionI GE ExpressionI
    ExpressionB : ExpressionI EQ ExpressionI
    ExpressionB : ExpressionI NEQ ExpressionI
    """

precedence = (
     ('nonassoc', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NEQ'),
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
     ('left', 'AND'),
     ('left', 'OR')
)

def p_error(p):
    parser.exito = False
    if p:
        print("Syntax error on token: ", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Unexpected EOF! Does the program have commands?")

parser = yacc.yacc()
# Dicionário que faz corresponder ao nome de cada variável no programa
# o seu valor, no momento da execução de cada instrução.
parser.var_values = {}
parser.var_types = {}
parser.nextvar_addr = 0
parser.var_stack_loc = {}

parser.exito = True

testfile_name = 'test/test4.mylang'

def get_file_path(filename):
    parentdir = os.path.split(os.path.dirname(__file__))[0]
    complete_filename = os.path.join(parentdir, filename)
    return complete_filename

input_fd = open(get_file_path(testfile_name), r'r', encoding="utf-8")
input_code = input_fd.read()

parser.parse(input_code, tracking=True)

testfile_output_name = "test/test4.vm"
output_fd = open(get_file_path(testfile_output_name), r'w', encoding='utf-8')

if parser.exito:
    print(input_code)
    print(parser.var_values)
    print(parser.var_types)
    print("Parsing teminou com sucesso!")
    print("---\nInput code:\n---")
    print(input_code)
    output_fd.write(parser.program)
    print("---\nOutput code:\n---")
    print(parser.program)

    import subprocess
    subprocess.run(["./vms", "../test/test4.vm"], cwd=get_file_path("vms"))

input_fd.close()
output_fd.close()
