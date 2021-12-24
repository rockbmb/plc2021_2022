import ply.yacc as yacc
import os

import sys

from lang_lex import tokens

def p_lang_grammar(p):
    "Program : DeclBlock CommandBlock"
    p[0] = p[1]
    p[0].append("start\n")
    p[0] += p[2]
    p[0].append("stop")
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
    if p[2] in parser.var_types.keys() or p[2] in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: redeclaring variable;")
        print(f"Redeclaration in line number {line}, character {index}: \n{' '.join(map(str, p[1:5]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    parser.var_types[p[2]] = int
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"\tpushi {p[4]}\n"]

def p_lang_intvar_default(p):
    "intvar : IntDecl Name"
    if p[2] in parser.var_types.keys() or p[2] in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: redeclaring variable;")
        print(f"Redeclaration in line number {line}, character {index}: \n{' '.join(map(str, p[1:3]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    parser.var_types[p[2]] = int
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"\tpushi {0}\n"]

def p_lang_boolvar(p):
    "boolvar : BoolDecl Name Decl Bool"
    if p[2] in parser.var_types.keys() or p[2] in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: redeclaring variable;")
        print(f"Redeclaration in line number {line}, character {index}: \n{' '.join(map(str, p[1:5]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    parser.var_types[p[2]] = bool
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"\tpushi {int(p[4])}\n"]

def p_lang_boolvar_default(p):
    "boolvar : BoolDecl Name"
    if p[2] in parser.var_types.keys() or p[2] in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: redeclaring variable;")
        print(f"Redeclaration in line number {line}, character {index}: \n{' '.join(map(str, p[1:3]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    parser.var_types[p[2]] = bool
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"\tpushi {int(False)}\n"]

def p_lang_stringvar(p):
    "stringvar : StringDecl Name Decl String"
    if p[2] in parser.var_types.keys() or p[2] in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: redeclaring variable;")
        print(f"Redeclaration in line number {line}, character {index}: \n{' '.join(map(str, p[1:5]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    parser.var_types[p[2]] = str
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"\tpushs {p[4]}\n"]

def p_lang_stringvar_default(p):
    "stringvar : StringDecl Name"
    if p[2] in parser.var_types.keys() or p[2] in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: redeclaring variable;")
        print(f"Redeclaration in line number {line}, character {index}: \n{' '.join(map(str, p[1:3]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    parser.var_types[p[2]] = str
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    empty = r'""'
    p[0] = [f"\tpushs {empty}\n"]

def p_lang_commandblock_1(p):
    "CommandBlock : CommandBlock Command"
    p[0] = p[1]
    p[0] += p[2]

def p_lang_commandblock_2(p):
    "CommandBlock : Command"
    p[0] = p[1]

########################
# Assignment productions
########################
def p_lang_command_1(p):
    "Command : Assign"
    p[0] = p[1]

# TODO: prevent reassignments, and handle usage of nonexisting variables.
def p_lang_command_assign_int(p):
    "Assign : Name ASSIGN ExpressionI"
    if p[1] not in parser.var_types.keys() or p[1] not in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: use of undeclared variable;")
        print(f"Undeclared variable in line number {line}, character {index}: \n{' '.join(map(str, p[1:4]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    elif parser.var_types[p[1]] not in [int, bool]:
        line   = p.lineno(2)        # line number of the ASSIGN token
        index  = p.lexpos(2)        # Position of the ASSIGN token
        print("Error: assigning integer expression to non-integer variable;")
        print(f"Wrong types in variable assignment in line number {line}, character {index}: \n{' '.join(map(str, p[1:4]))}")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = p[3]
        p[0].append(f'\tstoreg {parser.var_stack_loc[p[1]]}\n')

def p_lang_command_assign_2(p):
    "Assign : Name ASSIGN ExpressionB"
    if p[1] not in parser.var_types.keys() or p[1] not in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: use of undeclared variable;")
        print(f"Undeclared variable in line number {line}, character {index}: \n{' '.join(map(str, p[1:4]))}")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    if parser.var_types[p[1]] not in [int, bool]:
        line   = p.lineno(2)        # line number of the ASSIGN token
        index  = p.lexpos(2)        # Position of the ASSIGN token
        print("Error: assigning boolean expression to non-integer variable;")
        s = "{...}"
        print(f"Wrong types in variable assignment in line number {line}, character {index}: \n{' '.join(map(str, p[1:4]))} {s}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = p[3]
        p[0].append(f'\tstoreg {parser.var_stack_loc[p[1]]}\n')

def p_lang_command_assign_3(p):
    "Assign : Name ASSIGN String"
    if p[1] not in parser.var_types.keys() or p[1] not in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: use of undeclared variable;")
        print(f"Undeclared variable in line number {line}, character {index}: \n{' '.join(map(str, p[1:4]))}")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    if parser.var_types[p[1]] not in [str]:
        line   = p.lineno(2)        # line number of the ASSIGN token
        index  = p.lexpos(2)        # Position of the ASSIGN token
        print("Error: assigning string to non-string variable;")
        print(f"Wrong types in variable assignment in line number {line}, character {index}: \n{' '.join(map(str, p[1:4]))}")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = [f"\tpushs {p[4]}"]
        p[0].append(f'\tstoreg {parser.var_stack_loc[p[1]]}\n')

def p_lang_command_assign_4(p):
    "Assign : Name ASSIGN ReadString LPAREN RPAREN"
    if p[1] not in parser.var_types.keys() or p[1] not in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: use of undeclared variable;")
        print(f"Undeclared variable in line number {line}, character {index}: \n{' '.join(map(str, p[1:4]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = ["\tread\n"]
        if parser.var_types[p[1]] in [int, bool]:
            p[0].append("\tatoi\n")
        p[0].append(f"\tstoreg {parser.var_stack_loc[p[1]]}")

def p_lang_comma_sep_var(p):
    "PrintableElem : Name"
    p[0] = [f"\tpushg {parser.var_stack_loc[p[1]]}\n"]
    if parser.var_types[p[1]] in [str]:
        p[0].append("\twrites\n")
    elif parser.var_types[p[1]] in [int, bool]:
        p[0].append("\twritei\n")
    else:
        print("Unknwon type variable being printed!")
        p[0] = []

def p_lang_comma_sep_int(p):
    "PrintableElem : Integer"
    p[0] = [f"\tpushi {p[1]}\n"]
    p[0].append("\twritei\n")

def p_lang_comma_sep_bool(p):
    "PrintableElem : Bool"
    p[0] = [f"\tpushi {p[1]}\n"]
    p[0].append("\twritei\n")

def p_lang_comma_sep_string(p):
    "PrintableElem : String"
    p[0] = [f"\tpushs {p[1]}\n"]
    p[0].append("\twrites\n")

def p_lang_comma_sep_list_not_empty(p):
    "PrintableList : PrintableList COMMA PrintableElem"
    p[0] = p[1]
    p[0] += p[3]

def p_lang_comma_sep_list_empty(p):
    "PrintableList : PrintableElem"
    p[0] = p[1]

def p_lang_command_4(p):
    "Command : WriteString LPAREN PrintableList RPAREN"
    p[0] = p[3]

def p_lang_expressionI_plus(p):
    "ExpressionI : ExpressionI PLUS TermI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tadd\n")

def p_lang_expressionI_minus(p):
    "ExpressionI : ExpressionI MINUS TermI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tsub\n")

def p_lang_expressionI_termI(p):
    "ExpressionI : TermI"
    p[0] = p[1]

def p_lang_termI_mul(p):
    "TermI       : TermI TIMES factorI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tmul\n")

def p_lang_termI_div(p):
    "TermI       : TermI DIVIDE factorI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tdiv\n")

def p_lang_termI(p):
    "TermI       : factorI"
    p[0] = p[1]

def p_lang_factorI_int(p):
    "factorI     : Integer"
    p[0] = [f"\tpushi {p[1]}\n"]

def p_lang_factorI_var(p):
    "factorI     : Name"
    if p[1] not in parser.var_types.keys() or p[1] not in parser.var_stack_loc.keys():
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: use of undeclared variable;")
        print(f"Undeclared variable in line number {line}, character {index}: \n{p[1]}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    elif parser.var_types[p[1]] not in [int, bool]:
        line   = p.lineno(2)        # line number of the ASSIGN token
        index  = p.lexpos(2)        # Position of the ASSIGN token
        print("Error: integer expression with non-integer variable;")
        s = "{...}"
        print(f"Expression in line number {line}, character {index}: \n{s} {p[1]} {s}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = [f'\tpushg {parser.var_stack_loc[p[1]]}\n']

def p_lang_factorI_paren(p):
    "factorI     : LPAREN ExpressionI RPAREN"
    p[0] = p[2]

def p_lang_expressionB_base(p):
    "ExpressionB : Bool"
    if p[1]:
        p[0] = ["\tpushi 1\n"]
    else:
        p[0] = ["\tpushi 0\n"]

def p_lang_expressionB_expressionI(p):
    "ExpressionB : ExpressionI"
    p[0] = p[1]
    p[0].append("\tnot\n")
    p[0].append("\tnot\n")

#def p_lang_expressionB_var(p):
#    "ExpressionB : Name"
#    if p[1] not in parser.var_types.keys() or p[1] not in parser.var_stack_loc.keys():
#        line   = p.lineno(1)
#        index  = p.lexpos(1)
#        print("Error: use of undeclared variable;")
#        print(f"Undeclared variable in line number {line}, character {index}: \n{p[1]}.")
#        parser.exito = False
#        p[0] = []
#        raise SyntaxError
#    elif parser.var_types[p[1]] not in [int, bool]:
#        line   = p.lineno(2)        # line number of the ASSIGN token
#        index  = p.lexpos(2)        # Position of the ASSIGN token
#        print("Error: boolean expression with non-integer variable;")
#        s = "{...}"
#        print(f"Expression in line number {line}, character {index}: \n{s} {p[1]} {s}.")
#        parser.exito = False
#        p[0] = []
#        raise SyntaxError
#    else:
#        # Se a variável x for inteira, assume-se que qualquer valor diferente
#        # de 0 é True, e 0 é False.
#        # A instrução not compara um número a 0 e devolve 0 ou 1, logo fazê-lo
#        # vezes a um inteiro tem o resultado pretendido.
#        p[0] = [f'\tpushg {parser.var_stack_loc[p[1]]}\n']
#        p[0].append("\tnot\n")
#        p[0].append("\tnot\n")
#    if p[1]:
#        p[0] = 1
#    else:
#        p[0] = 0

def p_lang_expressionB_and(p):
    "ExpressionB : ExpressionB AND ExpressionB"
    # Conjunção lógica corresponde a multiplicação em álgebra grupo booleana.
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tmul\n")

def p_lang_expressionB_or(p):
    "ExpressionB : ExpressionB OR ExpressionB"
    # Disjunção lógica entre x e y corresponde a x + y - xy em álgebra booleana,
    # ou seja, x + y + (-1)*x*y
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tdup 2\n")
    p[0].append("\tmul\n")
    p[0].append("\tpushi -1\n")
    p[0].append("\tmul\n")
    p[0].append("\tadd\n")
    p[0].append("\tadd\n")

def p_lang_expressionB_not(p):
    "ExpressionB : NOT LPAREN ExpressionB RPAREN"
    p[0] = p[3]
    p[0].append("\tnot\n")

def p_lang_expressionB_paren(p):
    "ExpressionB : LPAREN ExpressionB RPAREN"
    p[0] = p[2]

def p_lang_expressionB_lt(p):
    "ExpressionB : ExpressionI LT ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tinf\n")

def p_lang_expressionB_le(p):
    "ExpressionB : ExpressionI LE ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tinfeq\n")

def p_lang_expressionB_gt(p):
    "ExpressionB : ExpressionI GT ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tsup\n")

def p_lang_expressionB_ge(p):
    "ExpressionB : ExpressionI GE ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tsupeq\n")

def p_lang_expressionB_eq(p):
    "ExpressionB : ExpressionI EQ ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tequal\n")

def p_lang_expressionB_neq(p):
    "ExpressionB : ExpressionI NEQ ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tequal\n")
    p[0].append("\tnot\n")

def p_lang_command_ifthenelse(p):
    "Command : IfThenElse"
    p[0] = p[1]

def p_lang_ifthenelse(p):
    "IfThenElse : If ExpressionB Then LBRACKET CommandBlock RBRACKET Else LBRACKET CommandBlock RBRACKET"
    p[0] = p[2]
    p[0].append(f"\tjz iffalse{parser.if_count}\n")
    p[0] += p[5]
    p[0].append(f"\tjump ifrest{parser.if_count}\n")
    p[0].append(f"iffalse{parser.if_count}: ")
    p[0] += p[9]
    p[0].append(f"ifrest{parser.if_count}: ")
    parser.if_count += 1

def p_lang_command_while(p):
    "Command : WhileDo"
    p[0] = p[1]

def p_lang_while(p):
    "WhileDo : While ExpressionB LBRACKET CommandBlock RBRACKET"
    p[0] = [f"while{parser.while_count}: "]
    p[0] += p[2]
    p[0].append(f"\tjz whilerest{parser.while_count}\n")
    p[0] += p[4]
    p[0].append(f"\tjump while{parser.while_count}\n")
    p[0].append(f"whilerest{parser.while_count}: ")
    parser.while_count += 1

precedence = (
     ('nonassoc', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NEQ'),
     ('left', 'PLUS', 'MINUS'),
     ('left', 'TIMES', 'DIVIDE'),
     ('left', 'OR'),
     ('left', 'AND')
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
parser.var_types = {}
parser.nextvar_addr = 0
parser.var_stack_loc = {}

# Used to tag if-then-else labels to make them unique.
parser.if_count = 0
parser.while_count = 0

parser.exito = True

testfile_name = 'test/test8.mylang'

def get_file_path(filename):
    parentdir = os.path.split(os.path.dirname(__file__))[0]
    complete_filename = os.path.join(parentdir, filename)
    return complete_filename

input_fd = open(get_file_path(testfile_name), r'r', encoding="utf-8")
input_code = input_fd.read()

parser.parse(input_code, tracking=True)

testfile_output_name = "test/test8.vm"
output_fd = open(get_file_path(testfile_output_name), r'w', encoding='utf-8')

if parser.exito:
    print(input_code)
    print(parser.var_types)
    print("Parsing teminou com sucesso!")
    print("---\nInput code:\n---")
    print(input_code)
    output_fd.write(parser.program)
    print("---\nOutput code:\n---")
    print(parser.program)

    print("---\nProgram Execution\n---")
    import subprocess
    subprocess.run(["./vms", "../test/test8.vm"], cwd=get_file_path("vms"))

input_fd.close()
output_fd.close()
