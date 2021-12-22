
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLTGTLEGEEQNEQleftPLUSMINUSleftTIMESDIVIDEleftANDleftORAND ASSIGN Bool BoolDecl DIVIDE Decl DeclBegin DeclEnd EQ GE GT IntDecl Integer LE LPAREN LT MINUS NEQ NOT Name OR PLUS RPAREN ReadString String StringDecl TIMES WriteStringProgram : DeclBlock CommandBlockDeclBlock : DeclBegin Vars DeclEndVars : Vars VarVars : VarVar : intvarVar : boolvarVar : stringvarintvar : IntDecl Name Decl Integerintvar : IntDecl Nameboolvar : BoolDecl Name Decl Boolboolvar : BoolDecl Namestringvar : StringDecl Name Decl Stringstringvar : StringDecl NameCommandBlock : CommandBlock CommandCommandBlock : CommandCommand : AssignAssign : Name ASSIGN ExpressionIAssign : Name ASSIGN ExpressionBAssign : Name ASSIGN StringAssign : Name ASSIGN ReadStringCommand : IOCommandIOCommand : ReadStringIOCommand : WriteStringExpressionI : ExpressionI PLUS TermIExpressionI : ExpressionI MINUS TermIExpressionI : TermITermI       : TermI TIMES factorITermI       : TermI DIVIDE factorITermI       : factorIfactorI     : IntegerfactorI     : NamefactorI     : LPAREN ExpressionI RPAREN\n    ExpressionB : Bool\n    ExpressionB : ExpressionB AND ExpressionB\n    ExpressionB : ExpressionB OR ExpressionB\n    ExpressionB : NOT LPAREN ExpressionB RPAREN\n    ExpressionB : LPAREN ExpressionB RPAREN\n\n    ExpressionB : ExpressionI LT ExpressionI\n    ExpressionB : ExpressionI LE ExpressionI\n    ExpressionB : ExpressionI GT ExpressionI\n    ExpressionB : ExpressionI GE ExpressionI\n    ExpressionB : ExpressionI EQ ExpressionI\n    ExpressionB : ExpressionI NEQ ExpressionI\n    '
    
_lr_action_items = {'DeclBegin':([0,],[3,]),'$end':([1,4,5,6,7,9,10,19,26,27,28,29,30,31,32,35,36,58,60,61,62,63,64,65,66,67,69,70,71,73,74,76,],[0,-1,-15,-16,-21,-22,-23,-14,-31,-17,-18,-19,-20,-26,-33,-29,-30,-24,-25,-38,-39,-40,-41,-42,-43,-34,-35,-27,-28,-37,-32,-36,]),'Name':([2,4,5,6,7,9,10,16,17,18,19,20,21,26,27,28,29,30,31,32,34,35,36,40,41,42,43,44,45,46,47,48,49,50,51,52,58,59,60,61,62,63,64,65,66,67,69,70,71,73,74,76,],[8,8,-15,-16,-21,-22,-23,23,24,25,-14,26,-2,-31,-17,-18,-19,-20,-26,-33,26,-29,-30,26,26,26,26,26,26,26,26,26,26,26,26,26,-24,26,-25,-38,-39,-40,-41,-42,-43,-34,-35,-27,-28,-37,-32,-36,]),'ReadString':([2,4,5,6,7,9,10,19,20,21,26,27,28,29,30,31,32,35,36,58,60,61,62,63,64,65,66,67,69,70,71,73,74,76,],[9,9,-15,-16,-21,-22,-23,-14,30,-2,-31,-17,-18,-19,-20,-26,-33,-29,-30,-24,-25,-38,-39,-40,-41,-42,-43,-34,-35,-27,-28,-37,-32,-36,]),'WriteString':([2,4,5,6,7,9,10,19,21,26,27,28,29,30,31,32,35,36,58,60,61,62,63,64,65,66,67,69,70,71,73,74,76,],[10,10,-15,-16,-21,-22,-23,-14,-2,-31,-17,-18,-19,-20,-26,-33,-29,-30,-24,-25,-38,-39,-40,-41,-42,-43,-34,-35,-27,-28,-37,-32,-36,]),'IntDecl':([3,11,12,13,14,15,22,23,24,25,55,56,57,],[16,16,-4,-5,-6,-7,-3,-9,-11,-13,-8,-10,-12,]),'BoolDecl':([3,11,12,13,14,15,22,23,24,25,55,56,57,],[17,17,-4,-5,-6,-7,-3,-9,-11,-13,-8,-10,-12,]),'StringDecl':([3,11,12,13,14,15,22,23,24,25,55,56,57,],[18,18,-4,-5,-6,-7,-3,-9,-11,-13,-8,-10,-12,]),'ASSIGN':([8,],[20,]),'DeclEnd':([11,12,13,14,15,22,23,24,25,55,56,57,],[21,-4,-5,-6,-7,-3,-9,-11,-13,-8,-10,-12,]),'String':([20,39,],[29,57,]),'Bool':([20,34,38,48,49,52,],[32,32,56,32,32,32,]),'NOT':([20,34,48,49,52,],[33,33,33,33,33,]),'LPAREN':([20,33,34,40,41,42,43,44,45,46,47,48,49,50,51,52,59,],[34,52,34,59,59,59,59,59,59,59,59,34,34,59,59,34,59,]),'Integer':([20,34,37,40,41,42,43,44,45,46,47,48,49,50,51,52,59,],[36,36,55,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'Decl':([23,24,25,],[37,38,39,]),'TIMES':([26,31,35,36,58,60,70,71,74,],[-31,50,-29,-30,50,50,-27,-28,-32,]),'DIVIDE':([26,31,35,36,58,60,70,71,74,],[-31,51,-29,-30,51,51,-27,-28,-32,]),'PLUS':([26,27,31,35,36,54,58,60,61,62,63,64,65,66,68,70,71,74,75,],[-31,40,-26,-29,-30,40,-24,-25,40,40,40,40,40,40,40,-27,-28,-32,40,]),'MINUS':([26,27,31,35,36,54,58,60,61,62,63,64,65,66,68,70,71,74,75,],[-31,41,-26,-29,-30,41,-24,-25,41,41,41,41,41,41,41,-27,-28,-32,41,]),'LT':([26,27,31,35,36,54,58,60,68,70,71,74,],[-31,42,-26,-29,-30,42,-24,-25,42,-27,-28,-32,]),'LE':([26,27,31,35,36,54,58,60,68,70,71,74,],[-31,43,-26,-29,-30,43,-24,-25,43,-27,-28,-32,]),'GT':([26,27,31,35,36,54,58,60,68,70,71,74,],[-31,44,-26,-29,-30,44,-24,-25,44,-27,-28,-32,]),'GE':([26,27,31,35,36,54,58,60,68,70,71,74,],[-31,45,-26,-29,-30,45,-24,-25,45,-27,-28,-32,]),'EQ':([26,27,31,35,36,54,58,60,68,70,71,74,],[-31,46,-26,-29,-30,46,-24,-25,46,-27,-28,-32,]),'NEQ':([26,27,31,35,36,54,58,60,68,70,71,74,],[-31,47,-26,-29,-30,47,-24,-25,47,-27,-28,-32,]),'RPAREN':([26,31,32,35,36,53,54,58,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,],[-31,-26,-33,-29,-30,73,74,-24,-25,-38,-39,-40,-41,-42,-43,-34,-35,-27,-28,76,-37,-32,74,-36,]),'AND':([26,28,31,32,35,36,53,58,60,61,62,63,64,65,66,67,69,70,71,72,73,74,76,],[-31,48,-26,-33,-29,-30,48,-24,-25,-38,-39,-40,-41,-42,-43,-34,-35,-27,-28,48,-37,-32,-36,]),'OR':([26,28,31,32,35,36,53,58,60,61,62,63,64,65,66,67,69,70,71,72,73,74,76,],[-31,49,-26,-33,-29,-30,49,-24,-25,-38,-39,-40,-41,-42,-43,49,-35,-27,-28,49,-37,-32,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'DeclBlock':([0,],[2,]),'CommandBlock':([2,],[4,]),'Command':([2,4,],[5,19,]),'Assign':([2,4,],[6,6,]),'IOCommand':([2,4,],[7,7,]),'Vars':([3,],[11,]),'Var':([3,11,],[12,22,]),'intvar':([3,11,],[13,13,]),'boolvar':([3,11,],[14,14,]),'stringvar':([3,11,],[15,15,]),'ExpressionI':([20,34,42,43,44,45,46,47,48,49,52,59,],[27,54,61,62,63,64,65,66,68,68,68,75,]),'ExpressionB':([20,34,48,49,52,],[28,53,67,69,72,]),'TermI':([20,34,40,41,42,43,44,45,46,47,48,49,52,59,],[31,31,58,60,31,31,31,31,31,31,31,31,31,31,]),'factorI':([20,34,40,41,42,43,44,45,46,47,48,49,50,51,52,59,],[35,35,35,35,35,35,35,35,35,35,35,35,70,71,35,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> DeclBlock CommandBlock','Program',2,'p_lang_grammar','lang_yacc.py',9),
  ('DeclBlock -> DeclBegin Vars DeclEnd','DeclBlock',3,'p_lang_decls','lang_yacc.py',16),
  ('Vars -> Vars Var','Vars',2,'p_lang_vars_1','lang_yacc.py',20),
  ('Vars -> Var','Vars',1,'p_lang_vars_2','lang_yacc.py',25),
  ('Var -> intvar','Var',1,'p_lang_var_int','lang_yacc.py',29),
  ('Var -> boolvar','Var',1,'p_lang_var_bool','lang_yacc.py',33),
  ('Var -> stringvar','Var',1,'p_lang_var_str','lang_yacc.py',37),
  ('intvar -> IntDecl Name Decl Integer','intvar',4,'p_lang_intvar','lang_yacc.py',41),
  ('intvar -> IntDecl Name','intvar',2,'p_lang_intvar_default','lang_yacc.py',49),
  ('boolvar -> BoolDecl Name Decl Bool','boolvar',4,'p_lang_boolvar','lang_yacc.py',57),
  ('boolvar -> BoolDecl Name','boolvar',2,'p_lang_boolvar_default','lang_yacc.py',65),
  ('stringvar -> StringDecl Name Decl String','stringvar',4,'p_lang_stringvar','lang_yacc.py',73),
  ('stringvar -> StringDecl Name','stringvar',2,'p_lang_stringvar_default','lang_yacc.py',81),
  ('CommandBlock -> CommandBlock Command','CommandBlock',2,'p_lang_commandblock_1','lang_yacc.py',90),
  ('CommandBlock -> Command','CommandBlock',1,'p_lang_commandblock_2','lang_yacc.py',95),
  ('Command -> Assign','Command',1,'p_lang_command_1','lang_yacc.py',99),
  ('Assign -> Name ASSIGN ExpressionI','Assign',3,'p_lang_command_assign_int','lang_yacc.py',103),
  ('Assign -> Name ASSIGN ExpressionB','Assign',3,'p_lang_command_assign_2','lang_yacc.py',118),
  ('Assign -> Name ASSIGN String','Assign',3,'p_lang_command_assign_3','lang_yacc.py',120),
  ('Assign -> Name ASSIGN ReadString','Assign',3,'p_lang_command_assign_4','lang_yacc.py',122),
  ('Command -> IOCommand','Command',1,'p_lang_command_4','lang_yacc.py',130),
  ('IOCommand -> ReadString','IOCommand',1,'p_lang_command_IO_1','lang_yacc.py',133),
  ('IOCommand -> WriteString','IOCommand',1,'p_lang_command_IO_2','lang_yacc.py',136),
  ('ExpressionI -> ExpressionI PLUS TermI','ExpressionI',3,'p_lang_expressionI_plus','lang_yacc.py',139),
  ('ExpressionI -> ExpressionI MINUS TermI','ExpressionI',3,'p_lang_expressionI_minus','lang_yacc.py',145),
  ('ExpressionI -> TermI','ExpressionI',1,'p_lang_expressionI_termI','lang_yacc.py',151),
  ('TermI -> TermI TIMES factorI','TermI',3,'p_lang_termI_mul','lang_yacc.py',155),
  ('TermI -> TermI DIVIDE factorI','TermI',3,'p_lang_termI_div','lang_yacc.py',161),
  ('TermI -> factorI','TermI',1,'p_lang_termI','lang_yacc.py',167),
  ('factorI -> Integer','factorI',1,'p_lang_factorI_int','lang_yacc.py',171),
  ('factorI -> Name','factorI',1,'p_lang_factorI_var','lang_yacc.py',175),
  ('factorI -> LPAREN ExpressionI RPAREN','factorI',3,'p_lang_factorI_paren','lang_yacc.py',191),
  ('ExpressionB -> Bool','ExpressionB',1,'p_lang_rest_2','lang_yacc.py',196),
  ('ExpressionB -> ExpressionB AND ExpressionB','ExpressionB',3,'p_lang_rest_2','lang_yacc.py',197),
  ('ExpressionB -> ExpressionB OR ExpressionB','ExpressionB',3,'p_lang_rest_2','lang_yacc.py',198),
  ('ExpressionB -> NOT LPAREN ExpressionB RPAREN','ExpressionB',4,'p_lang_rest_2','lang_yacc.py',199),
  ('ExpressionB -> LPAREN ExpressionB RPAREN','ExpressionB',3,'p_lang_rest_2','lang_yacc.py',200),
  ('ExpressionB -> ExpressionI LT ExpressionI','ExpressionB',3,'p_lang_rest_2','lang_yacc.py',202),
  ('ExpressionB -> ExpressionI LE ExpressionI','ExpressionB',3,'p_lang_rest_2','lang_yacc.py',203),
  ('ExpressionB -> ExpressionI GT ExpressionI','ExpressionB',3,'p_lang_rest_2','lang_yacc.py',204),
  ('ExpressionB -> ExpressionI GE ExpressionI','ExpressionB',3,'p_lang_rest_2','lang_yacc.py',205),
  ('ExpressionB -> ExpressionI EQ ExpressionI','ExpressionB',3,'p_lang_rest_2','lang_yacc.py',206),
  ('ExpressionB -> ExpressionI NEQ ExpressionI','ExpressionB',3,'p_lang_rest_2','lang_yacc.py',207),
]
