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
    "Var : IntVar"
    p[0] = p[1]

def p_lang_var_bool(p):
    "Var : BoolVar"
    p[0] = p[1]

def p_lang_var_str(p):
    "Var : StringVar"
    p[0] = p[1]

def p_lang_var_arr(p):
    "Var : ArrVar"
    p[0] = p[1]

def p_lang_var_arr2(p):
    "Var : Arr2Var"
    p[0] = p[1]

def p_lang_IntVar(p):
    "IntVar : IntDecl Name Decl ExpressionI"
    redeclaration_error(p, 2)
    parser.var_types[p[2]] = int
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = p[4]

def redeclaration_error(p, prod_index):
    if p[prod_index] in parser.var_types.keys() or p[prod_index] in parser.var_stack_loc.keys():
        line   = p.lineno(prod_index)
        index  = p.lexpos(prod_index)
        print("Error: redeclaring variable;")
        print(f"Redeclaration in line number {line}, character {index}: \n(..) {' '.join(p[1:(prod_index+1)])} (..)")
        parser.exito = False
        p[0] = []
        raise SyntaxError

def p_lang_IntVar_default(p):
    "IntVar : IntDecl Name"
    redeclaration_error(p, 2)
    parser.var_types[p[2]] = int
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"\tpushi {0}\n"]

def p_lang_BoolVar(p):
    "BoolVar : BoolDecl Name Decl ExpressionB"
    redeclaration_error(p, 2)
    parser.var_types[p[2]] = bool
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"\tpushi {int(p[4])}\n"]

def p_lang_BoolVar_default(p):
    "BoolVar : BoolDecl Name"
    redeclaration_error(p, 2)
    parser.var_types[p[2]] = bool
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"\tpushi {int(False)}\n"]

def p_lang_StringVar(p):
    "StringVar : StringDecl Name Decl String"
    redeclaration_error(p, 2)
    parser.var_types[p[2]] = str
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    p[0] = [f"\tpushs {p[4]}\n"]

def p_lang_StringVar_default(p):
    "StringVar : StringDecl Name"
    redeclaration_error(p, 2)
    parser.var_types[p[2]] = str
    parser.var_stack_loc[p[2]] = parser.nextvar_addr
    parser.nextvar_addr += 1
    empty = r'""'
    p[0] = [f"\tpushs {empty}\n"]

def p_lang_ArrVar_default(p):
    "ArrVar : IntDecl LSQBRACKET Integer RSQBRACKET Name"
    line   = p.lineno(1)
    index  = p.lexpos(1)
    redeclaration_error(p, 5)
    if p[3] < 0:
        print("Declaring array with negative length.")
        print(f"Array with invalid length in line number {line}, character {index}: \n{' '.join(map(str, p[1:6]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    parser.var_types[p[5]] = list
    parser.var_stack_loc[p[5]] = parser.nextvar_addr
    parser.nextvar_addr += p[3]
    # by default, just creates a pointer to array with specified length, with all
    # positions set to 0.
    p[0] = [f"\tpushn {p[3]}\n"]

def p_lang_Arr2Var_default(p):
    "Arr2Var : IntDecl LSQBRACKET Integer RSQBRACKET LSQBRACKET Integer RSQBRACKET Name"
    line   = p.lineno(1)
    index  = p.lexpos(1)
    redeclaration_error(p, 8)
    if p[3] < 0 or p[6] < 0:
        print("Declaring two-dimensional array with negative lengths.")
        print(f"Array with invalid length in line number {line}, character {index}: \n{' '.join(map(str, p[1:9]))}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    parser.var_types[p[8]] = (list, list)
    parser.var_stack_loc[p[8]] = parser.nextvar_addr
    parser.nextvar_addr += p[3] * p[6]
    parser.arr2_row_len[p[8]] = p[3]
    # by default, just creates a pointer to array with specified length, with all
    # positions set to 0.
    p[0] = [f"\tpushn {p[3] * p[6]}\n"]

def p_lang_commandblock_1(p):
    "CommandBlock : CommandBlock Command"
    p[0] = p[1]
    p[0] += p[2]

def p_lang_commandblock_2(p):
    "CommandBlock : Command"
    p[0] = p[1]

########################
# Command productions
########################
def p_lang_command_1(p):
    "Command : Assign"
    p[0] = p[1]

def undeclared_error(p, production_index):
    if p[production_index] not in parser.var_types.keys() or p[production_index] not in parser.var_stack_loc.keys():
        line   = p.lineno(production_index)
        index  = p.lexpos(production_index)
        print("Error: use of undeclared variable;")
        print(f"Undeclared variable in line number {line}, character {index}: \n(..) {p[production_index]} (..)")
        parser.exito = False
        p[0] = []
        raise SyntaxError

def p_lang_command_assign_arr_position(p):
    "Assign : Name LSQBRACKET ExpressionI RSQBRACKET ASSIGN ExpressionI"
    undeclared_error(p, 1)
    if parser.var_types[p[1]] not in [list]:
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: assigning integer expression to non-array variable;")
        print(f"Wrong types in variable assignment in line number {line}, character {index}: \n{' '.join(map(str, p[1:6]))}")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = ["\tpushgp\n"]
        p[0].append(f'\tpushi {parser.var_stack_loc[p[1]]}\n')
        p[0].append("\tpadd\n")
        p[0] += p[3]
        p[0] += p[6]
        p[0].append("\tstoren\n")

def p_lang_command_assign_arr2_position(p):
    "Assign : Name LSQBRACKET ExpressionI RSQBRACKET LSQBRACKET ExpressionI RSQBRACKET ASSIGN ExpressionI"
    undeclared_error(p, 1)
    if parser.var_types[p[1]] not in [(list, list)]:
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: assigning integer expression to non-array variable;")
        print(f"Wrong types in variable assignment in line number {line}, character {index}: \n{p[1]}[..][..] <- (..)")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = ["\tpushgp\n"]
        p[0].append(f'\tpushi {parser.var_stack_loc[p[1]]}\n')
        p[0].append("\tpadd\n")
        p[0] += p[3]
        p[0].append(f"\tpushi {parser.arr2_row_len[p[1]]}\n")
        p[0].append("\tmul\n")
        p[0] += p[6]
        p[0].append("\tadd\n")
        p[0].append("\tstoren\n")

def p_lang_command_assign_2(p):
    "Assign : Name ASSIGN ExpressionB"
    undeclared_error(p, 1)
    if parser.var_types[p[1]] not in [int, bool]:
        line   = p.lineno(1)
        index  = p.lexpos(1)
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
    undeclared_error(p, 1)
    if parser.var_types[p[1]] not in [str]:
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: assigning string to non-string variable;")
        print(f"Wrong types in variable assignment in line number {line}, character {index}: \n{' '.join(map(str, p[1:4]))}")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = [f"\tpushs {p[4]}\n"]
        p[0].append(f'\tstoreg {parser.var_stack_loc[p[1]]}\n')

def p_lang_command_assign_4(p):
    "Assign : Name ASSIGN ReadString LPAREN RPAREN"
    undeclared_error(p, 1)
    p[0] = ["\tread\n"]
    if parser.var_types[p[1]] in [int, bool]:
        p[0].append("\tatoi\n")
    if parser.var_types[p[1]] is bool:
        p[0].append("\tnot\n")
        p[0].append("\tnot\n")
    p[0].append(f"\tstoreg {parser.var_stack_loc[p[1]]}\n")

def p_lang_command_assign_arr_read(p):
    "Assign : Name LSQBRACKET ExpressionI RSQBRACKET ASSIGN ReadString LPAREN RPAREN"
    undeclared_error(p, 1)
    if parser.var_types[p[1]] not in [list]:
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: using indexes on non-array variable;")
        print(f"Wrong types in variable assignment in line number {line}, character {index}: \n{' '.join(map(str, p[1:6]))}")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = ["\tpushgp\n"]
        p[0].append(f'\tpushi {parser.var_stack_loc[p[1]]}\n')
        p[0].append("\tpadd\n")
        p[0] += p[3]
        p[0].append("\tread\n")
        p[0].append("\tatoi\n")
        p[0].append("\tstoren\n")

def p_lang_command_assign_arr2_read(p):
    "Assign : Name LSQBRACKET ExpressionI RSQBRACKET LSQBRACKET ExpressionI RSQBRACKET ASSIGN ReadString LPAREN RPAREN"
    undeclared_error(p, 1)
    if parser.var_types[p[1]] not in [(list, list)]:
        line   = p.lineno(1)
        index  = p.lexpos(1)
        print("Error: using indexes on non-array variable;")
        print(f"Wrong types in variable assignment in line number {line}, character {index}: \n{p[1]}[..][..] <- (..)")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = ["\tpushgp\n"]
        p[0].append(f'\tpushi {parser.var_stack_loc[p[1]]}\n')
        p[0].append("\tpadd\n")
        p[0] += p[3]
        p[0].append(f"\tpushi {parser.arr2_row_len[p[1]]}\n")
        p[0].append("\tmul\n")
        p[0] += p[6]
        p[0].append("\tadd\n")
        p[0].append("\tread\n")
        p[0].append("\tatoi\n")
        p[0].append("\tstoren\n")

def p_lang_comma_sep_name(p):
    "PrintableElem : Name"
    undeclared_error(p, 1)
    if parser.var_types[p[1]] is str:
        p[0] = [f"\tpushg {parser.var_stack_loc[p[1]]}\n"]
        p[0].append("\twrites\n")
    if parser.var_types[p[1]] in [int, bool]:
        p[0] = [f'\tpushg {parser.var_stack_loc[p[1]]}\n']
        p[0].append("\twritei\n")
    if parser.var_types[p[1]] in [list, (list, list)]:
        p[0] = [f"\tpushs \"\n\"\n"]
        p[0].append(f"\tpushi {parser.var_stack_loc[p[1]]}\n")
        p[0].append("\tpushs \"Array com endereço inicial \"\n")
        p[0].append("\twrites\n")
        p[0].append("\twritei\n")
        p[0].append("\twrites\n")

def p_lang_comma_sep_expressionB(p):
    "PrintableElem : ExpressionB"
    p[0] = p[1]
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

def p_lang_command_error(p):
    "Command : Err LPAREN String RPAREN"
    p[0] = [f"\terr {p[3]}\n"]

def p_lang_expressionB_or(p):
    "ExpressionB    : ExpressionB OR AndExpressionB"
    # Disjunção lógica entre x e y corresponde a x + y - xy em álgebra booleana,
    # ou seja, x + y + (-1)*x*y
    p[0] = p[1]
    p[0].append("\tnot\n")
    p[0].append("\tnot\n")
    p[0] += p[3]
    p[0].append("\tnot\n")
    p[0].append("\tnot\n")
    p[0].append("\tdup 2\n")
    p[0].append("\tmul\n")
    p[0].append("\tpushi -1\n")
    p[0].append("\tmul\n")
    p[0].append("\tadd\n")
    p[0].append("\tadd\n")

def p_lang_expressionB_and(p):
    "ExpressionB    : AndExpressionB"
    p[0] = p[1]

def p_lang_andExpressionB_and(p):
    "AndExpressionB : AndExpressionB AND EqExpressionB"
    # Conjunção lógica corresponde a multiplicação em álgebra grupo booleana.
    p[0] = p[1]
    p[0].append("\tnot\n")
    p[0].append("\tnot\n")
    p[0] += p[3]
    p[0].append("\tnot\n")
    p[0].append("\tnot\n")
    p[0].append("\tmul\n")

def p_lang_andExpressionB_eq(p):
    "AndExpressionB : EqExpressionB"
    p[0] = p[1]

def p_lang_eqExpressionB_eq(p):
    "EqExpressionB  : EqExpressionB EQ RelExpressionB"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tequal\n")

def p_lang_eqExpressionB_neq(p):
    "EqExpressionB  : EqExpressionB NEQ RelExpressionB"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tequal\n")
    p[0].append("\tnot\n")

def p_lang_eqExpressionB_rel(p):
    "EqExpressionB  : RelExpressionB"
    p[0] = p[1]

def p_lang_relExpressionB_lt(p):
    "RelExpressionB : RelExpressionB LT ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tinf\n")

def p_lang_relExpressionB_le(p):
    "RelExpressionB : RelExpressionB LE ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tinfeq\n")

def p_lang_relExpressionB_gt(p):
    "RelExpressionB : RelExpressionB GT ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tsup\n")

def p_lang_relExpressionB_ge(p):
    "RelExpressionB : RelExpressionB GE ExpressionI"
    p[0] = p[1]
    p[0] += p [3]
    p[0].append("\tsupeq\n")

def p_lang_relExpressionB_not(p):
    "RelExpressionB : ExpressionI"
    p[0] = p[1]

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
    "TermI       : TermI TIMES FactorI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tmul\n")

def p_lang_termI_div(p):
    "TermI       : TermI DIVIDE FactorI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tdiv\n")

def p_lang_termI_mod(p):
    "TermI       : TermI MOD FactorI"
    p[0] = p[1]
    p[0] += p[3]
    p[0].append("\tmod\n")

def p_lang_termI(p):
    "TermI       : FactorI"
    p[0] = p[1]

def p_lang_factorI_ArrVar(p):
    "FactorI     : Name LSQBRACKET ExpressionI RSQBRACKET"
    undeclared_error(p, 1)
    if parser.var_types[p[1]] not in [list]:
        line   = p.lineno(1)        # line number of the ASSIGN token
        index  = p.lexpos(1)        # Position of the ASSIGN token
        print("Error: array expression with non-array variable;")
        s = "{...}"
        print(f"Expression in line number {line}, character {index}: \n{s} {p[1]} {s}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = ["\tpushgp\n"]
        p[0].append(f'\tpushi {parser.var_stack_loc[p[1]]}\n')
        p[0].append("\tpadd\n")
        p[0] += p[3]
        p[0].append("\tloadn\n")

def p_lang_factorI_Arr2Var(p):
    "FactorI     : Name LSQBRACKET ExpressionI RSQBRACKET LSQBRACKET ExpressionI RSQBRACKET"
    undeclared_error(p ,1)
    if parser.var_types[p[1]] not in [(list, list)]:
        line   = p.lineno(1)        # line number of the ASSIGN token
        index  = p.lexpos(1)        # Position of the ASSIGN token
        print("Error: array expression with non-array variable;")
        s = "{...}"
        print(f"Expression in line number {line}, character {index}: \n{s} {p[1]} {s}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = ["\tpushgp\n"]
        p[0].append(f'\tpushi {parser.var_stack_loc[p[1]]}\n')
        p[0].append("\tpadd\n")
        p[0] += p[3]
        p[0].append(f"\tpushi {parser.arr2_row_len[p[1]]}\n")
        p[0].append("\tmul\n")
        p[0] += p[6]
        p[0].append("\tadd\n")
        p[0].append("\tloadn\n")

def p_lang_factorI_not(p):
    "FactorI : UnaryExpressionB"
    p[0] = p[1]

def p_lang_unaryExpressionB_not(p):
    "UnaryExpressionB : NOT FinalExpressionB"
    p[0] = p[2]
    p[0].append("\tnot\n")

def p_lang_factorI_minus_expressionI(p):
    "UnaryExpressionB  : MINUS FinalExpressionB"
    p[0] = ["\tpushi 0\n"]
    p[0] += p[2]
    p[0].append("\tsub\n")

def p_lang_unaryExpressionB_expB(p):
    "UnaryExpressionB : FinalExpressionB"
    p[0] = p[1]

def p_lang_finalExpressionB_int(p):
    "FinalExpressionB     : Integer"
    p[0] = [f"\tpushi {p[1]}\n"]

def p_lang_finalExpressionB_var(p):
    "FinalExpressionB     : Name"
    undeclared_error(p, 1)
    if parser.var_types[p[1]] not in [int, bool]:
        line   = p.lineno(1)        # line number of the ASSIGN token
        index  = p.lexpos(1)        # Position of the ASSIGN token
        print("Error: integer expression with non-integer variable;")
        s = "{...}"
        print(f"Expression in line number {line}, character {index}: \n{s} {p[1]} {s}.")
        parser.exito = False
        p[0] = []
        raise SyntaxError
    else:
        p[0] = [f'\tpushg {parser.var_stack_loc[p[1]]}\n']

def p_lang_finalExpressionB_bool(p):
    "FinalExpressionB : Bool"
    if p[1]:
        p[0] = ["\tpushi 1\n"]
    else:
        p[0] = ["\tpushi 0\n"]

def p_lang_expressionB_name(p):
    "FinalExpressionB : LPAREN ExpressionB RPAREN"
    p[0] = p[2]

#def p_lang_expressionB_not(p):
#    "ExpressionB    : ExpressionB OR AndExpressionB"
#    "ExpressionB    : AndExpressionB"
#    "AndExpressionB : AndExpressionB AND EqExpressionB"
#    "AndExpressionB : EqExpressionB"
#    "EqExpressionB  : EqExpressionB EQ RelExpressionB"
#    "EqExpressionB  : EqExpressionB NEQ RelExpressionB"
#    "EqExpressionB  : RelExpressionB"
#    "RelExpressionB : ExpressionI LT ExpressionI"
#    "RelExpressionB : ExpressionI LE ExpressionI"
#    "RelExpressionB : ExpressionI GT ExpressionI"
#    "RelExpressionB : ExpressionI GE ExpressionI"
#    "RelExpressionB : UnaryExpressionB"
#    "UnaryExpressionB : NOT FinalExpressionB"
#    "UnaryExpressionB : FinalExpressionB"
#    "FinalExpressionB : Name"
#    "FinalExpressionB : LPAREN ExpressionB RPAREN"
#    "FinalExpressionB : Bool"

def p_lang_command_ifthenelse(p):
    "Command : IfThenElse"
    p[0] = p[1]

def p_lang_command_ifthen(p):
    "Command : IfThen"
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

def p_lang_ifthen(p):
    "IfThen : If ExpressionB Then LBRACKET CommandBlock RBRACKET"
    p[0] = p[2]
    p[0].append(f"\tjz ifrest{parser.if_count}\n")
    p[0] += p[5]
    p[0].append(f"ifrest{parser.if_count}: ")
    parser.if_count += 1

def p_lang_command_while(p):
    "Command : WhileDo"
    p[0] = p[1]

def p_lang_while(p):
    "WhileDo : While ExpressionB LBRACKET CommandBlock RBRACKET"
    cnt = parser.while_count
    parser.while_count += 1
    p[0] = [f"while{cnt}: "]
    p[0] += p[2]
    p[0].append(f"\tjz whilerest{cnt}\n")
    p[0] += p[4]
    p[0].append(f"\tjump while{cnt}\n")
    p[0].append(f"whilerest{cnt}: ")

def p_error(p):
    parser.exito = False
    if p:
        print("Syntax error on token: ", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Unexpected EOF! Does the program have commands?")

parser_Notebook = yacc.yacc()

parser = yacc.yacc()

# Dicionário que faz corresponder ao nome de cada variável no programa
# o seu valor, no momento da execução de cada instrução.
parser.var_types = {}
parser.nextvar_addr = 0
parser.var_stack_loc = {}
# Used to keep track of each 2d array's row length.
# Needed for indexing and assignment.
parser.arr2_row_len = {}

# Used to tag if-then-else labels to make them unique.
parser.if_count = 0
parser.while_count = 0

parser.exito = True

# I/O do script
# Nome do ficheiro de entrada
mylang_file=sys.argv[1]

testfile_name = f'test/{mylang_file}.mylang'

def get_file_path(filename):
    parentdir = os.path.split(os.path.dirname(__file__))[0]
    complete_filename = os.path.join(parentdir, filename)
    return complete_filename

input_fd = open(get_file_path(testfile_name), r'r', encoding="utf-8")
input_code = input_fd.read()

parser.parse(input_code, tracking=True)

testfile_output_name = f"test/{mylang_file}.vm"
output_fd = open(get_file_path(testfile_output_name), r'w', encoding='utf-8')

if parser.exito:
    print("Parsing teminou com sucesso!")
    print("---\nInput code:\n---")
    print(input_code)
    print("---\nOutput code:\n---")
    print(parser.program)
    output_fd.write(parser.program)

input_fd.close()
output_fd.close()

if parser.exito:
    print("---\nProgram Execution\n---")
    from subprocess import run
    run(["./vms", f"../test/{mylang_file}.vm"], cwd=get_file_path("vms"))