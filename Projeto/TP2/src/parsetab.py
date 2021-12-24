
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLTGTLEGEEQNEQleftPLUSMINUSleftTIMESDIVIDEleftORleftANDAND ASSIGN Bool BoolDecl COMMA DIVIDE Decl DeclBegin DeclEnd EQ Else GE GT If IntDecl Integer LBRACKET LE LPAREN LT MINUS NEQ NOT Name OR PLUS RBRACKET RPAREN ReadString String StringDecl TIMES Then While WriteStringProgram : DeclBlock CommandBlockDeclBlock : DeclBegin Vars DeclEndVars : Vars VarVars : VarVar : intvarVar : boolvarVar : stringvarintvar : IntDecl Name Decl Integerintvar : IntDecl Nameboolvar : BoolDecl Name Decl Boolboolvar : BoolDecl Namestringvar : StringDecl Name Decl Stringstringvar : StringDecl NameCommandBlock : CommandBlock CommandCommandBlock : CommandCommand : AssignAssign : Name ASSIGN ExpressionIAssign : Name ASSIGN ExpressionBAssign : Name ASSIGN StringAssign : Name ASSIGN ReadString LPAREN RPARENPrintableElem : NamePrintableElem : IntegerPrintableElem : BoolPrintableElem : StringPrintableList : PrintableList COMMA PrintableElemPrintableList : PrintableElemCommand : WriteString LPAREN PrintableList RPARENExpressionI : ExpressionI PLUS TermIExpressionI : ExpressionI MINUS TermIExpressionI : TermITermI       : TermI TIMES factorITermI       : TermI DIVIDE factorITermI       : factorIfactorI     : IntegerfactorI     : NamefactorI     : LPAREN ExpressionI RPARENExpressionB : BoolExpressionB : ExpressionIExpressionB : ExpressionB AND ExpressionBExpressionB : ExpressionB OR ExpressionBExpressionB : NOT LPAREN ExpressionB RPARENExpressionB : LPAREN ExpressionB RPARENExpressionB : ExpressionI LT ExpressionIExpressionB : ExpressionI LE ExpressionIExpressionB : ExpressionI GT ExpressionIExpressionB : ExpressionI GE ExpressionIExpressionB : ExpressionI EQ ExpressionIExpressionB : ExpressionI NEQ ExpressionICommand : IfThenElseIfThenElse : If ExpressionB Then LBRACKET CommandBlock RBRACKET Else LBRACKET CommandBlock RBRACKETCommand : WhileDoWhileDo : While ExpressionB LBRACKET CommandBlock RBRACKET'
    
_lr_action_items = {'DeclBegin':([0,],[3,]),'$end':([1,4,5,6,8,9,21,25,26,29,30,31,32,45,46,47,69,73,74,75,77,78,79,80,81,82,83,85,86,87,88,94,97,98,103,],[0,-1,-15,-16,-49,-51,-14,-37,-38,-30,-33,-34,-35,-17,-18,-19,-27,-39,-40,-43,-44,-45,-46,-47,-48,-28,-29,-42,-36,-31,-32,-20,-41,-52,-50,]),'WriteString':([2,4,5,6,8,9,21,25,26,29,30,31,32,34,45,46,47,65,69,72,73,74,75,77,78,79,80,81,82,83,85,86,87,88,89,94,95,97,98,101,102,103,],[7,7,-15,-16,-49,-51,-14,-37,-38,-30,-33,-34,-35,-2,-17,-18,-19,7,-27,7,-39,-40,-43,-44,-45,-46,-47,-48,-28,-29,-42,-36,-31,-32,7,-20,7,-41,-52,7,7,-50,]),'Name':([2,4,5,6,8,9,11,12,18,19,20,21,22,23,25,26,28,29,30,31,32,34,45,46,47,50,51,52,53,54,55,56,57,58,59,60,63,64,65,69,70,72,73,74,75,76,77,78,79,80,81,82,83,85,86,87,88,89,94,95,97,98,101,102,103,],[10,10,-15,-16,-49,-51,32,32,36,37,38,-14,41,32,-37,-38,32,-30,-33,-34,-35,-2,-17,-18,-19,32,32,32,32,32,32,32,32,32,32,32,32,32,10,-27,41,10,-39,-40,-43,32,-44,-45,-46,-47,-48,-28,-29,-42,-36,-31,-32,10,-20,10,-41,-52,10,10,-50,]),'If':([2,4,5,6,8,9,21,25,26,29,30,31,32,34,45,46,47,65,69,72,73,74,75,77,78,79,80,81,82,83,85,86,87,88,89,94,95,97,98,101,102,103,],[11,11,-15,-16,-49,-51,-14,-37,-38,-30,-33,-34,-35,-2,-17,-18,-19,11,-27,11,-39,-40,-43,-44,-45,-46,-47,-48,-28,-29,-42,-36,-31,-32,11,-20,11,-41,-52,11,11,-50,]),'While':([2,4,5,6,8,9,21,25,26,29,30,31,32,34,45,46,47,65,69,72,73,74,75,77,78,79,80,81,82,83,85,86,87,88,89,94,95,97,98,101,102,103,],[12,12,-15,-16,-49,-51,-14,-37,-38,-30,-33,-34,-35,-2,-17,-18,-19,12,-27,12,-39,-40,-43,-44,-45,-46,-47,-48,-28,-29,-42,-36,-31,-32,12,-20,12,-41,-52,12,12,-50,]),'IntDecl':([3,13,14,15,16,17,35,36,37,38,90,91,92,],[18,18,-4,-5,-6,-7,-3,-9,-11,-13,-8,-10,-12,]),'BoolDecl':([3,13,14,15,16,17,35,36,37,38,90,91,92,],[19,19,-4,-5,-6,-7,-3,-9,-11,-13,-8,-10,-12,]),'StringDecl':([3,13,14,15,16,17,35,36,37,38,90,91,92,],[20,20,-4,-5,-6,-7,-3,-9,-11,-13,-8,-10,-12,]),'RBRACKET':([5,6,8,9,21,25,26,29,30,31,32,45,46,47,69,73,74,75,77,78,79,80,81,82,83,85,86,87,88,89,94,95,97,98,102,103,],[-15,-16,-49,-51,-14,-37,-38,-30,-33,-34,-35,-17,-18,-19,-27,-39,-40,-43,-44,-45,-46,-47,-48,-28,-29,-42,-36,-31,-32,98,-20,99,-41,-52,103,-50,]),'LPAREN':([7,11,12,23,27,28,48,50,51,52,53,54,55,56,57,58,59,60,63,64,76,],[22,28,28,28,60,28,71,28,28,76,76,76,76,76,76,76,76,28,76,76,76,]),'ASSIGN':([10,],[23,]),'Bool':([11,12,22,23,28,50,51,60,67,70,],[25,25,43,25,25,25,25,25,91,43,]),'NOT':([11,12,23,28,50,51,60,],[27,27,27,27,27,27,27,]),'Integer':([11,12,22,23,28,50,51,52,53,54,55,56,57,58,59,60,63,64,66,70,76,],[31,31,42,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,90,42,31,]),'DeclEnd':([13,14,15,16,17,35,36,37,38,90,91,92,],[34,-4,-5,-6,-7,-3,-9,-11,-13,-8,-10,-12,]),'String':([22,23,68,70,],[44,47,92,44,]),'ReadString':([23,],[48,]),'Then':([24,25,26,29,30,31,32,73,74,75,77,78,79,80,81,82,83,85,86,87,88,97,],[49,-37,-38,-30,-33,-34,-35,-39,-40,-43,-44,-45,-46,-47,-48,-28,-29,-42,-36,-31,-32,-41,]),'AND':([24,25,26,29,30,31,32,33,45,46,61,62,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,97,],[50,-37,-38,-30,-33,-34,-35,50,-38,50,50,-38,-39,50,-43,-44,-45,-46,-47,-48,-28,-29,50,-42,-36,-31,-32,-41,]),'OR':([24,25,26,29,30,31,32,33,45,46,61,62,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,97,],[51,-37,-38,-30,-33,-34,-35,51,-38,51,51,-38,-39,-40,-43,-44,-45,-46,-47,-48,-28,-29,51,-42,-36,-31,-32,-41,]),'LBRACKET':([25,26,29,30,31,32,33,49,73,74,75,77,78,79,80,81,82,83,85,86,87,88,97,100,],[-37,-38,-30,-33,-34,-35,65,72,-39,-40,-43,-44,-45,-46,-47,-48,-28,-29,-42,-36,-31,-32,-41,101,]),'RPAREN':([25,26,29,30,31,32,39,40,41,42,43,44,61,62,71,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,93,96,97,],[-37,-38,-30,-33,-34,-35,69,-26,-21,-22,-23,-24,85,86,94,-39,-40,-43,-44,-45,-46,-47,-48,-28,-29,97,-42,-36,-31,-32,-25,86,-41,]),'LT':([26,29,30,31,32,45,62,82,83,86,87,88,],[52,-30,-33,-34,-35,52,52,-28,-29,-36,-31,-32,]),'LE':([26,29,30,31,32,45,62,82,83,86,87,88,],[53,-30,-33,-34,-35,53,53,-28,-29,-36,-31,-32,]),'GT':([26,29,30,31,32,45,62,82,83,86,87,88,],[54,-30,-33,-34,-35,54,54,-28,-29,-36,-31,-32,]),'GE':([26,29,30,31,32,45,62,82,83,86,87,88,],[55,-30,-33,-34,-35,55,55,-28,-29,-36,-31,-32,]),'EQ':([26,29,30,31,32,45,62,82,83,86,87,88,],[56,-30,-33,-34,-35,56,56,-28,-29,-36,-31,-32,]),'NEQ':([26,29,30,31,32,45,62,82,83,86,87,88,],[57,-30,-33,-34,-35,57,57,-28,-29,-36,-31,-32,]),'PLUS':([26,29,30,31,32,45,62,75,77,78,79,80,81,82,83,86,87,88,96,],[58,-30,-33,-34,-35,58,58,58,58,58,58,58,58,-28,-29,-36,-31,-32,58,]),'MINUS':([26,29,30,31,32,45,62,75,77,78,79,80,81,82,83,86,87,88,96,],[59,-30,-33,-34,-35,59,59,59,59,59,59,59,59,-28,-29,-36,-31,-32,59,]),'TIMES':([29,30,31,32,82,83,86,87,88,],[63,-33,-34,-35,63,63,-36,-31,-32,]),'DIVIDE':([29,30,31,32,82,83,86,87,88,],[64,-33,-34,-35,64,64,-36,-31,-32,]),'Decl':([36,37,38,],[66,67,68,]),'COMMA':([39,40,41,42,43,44,93,],[70,-26,-21,-22,-23,-24,-25,]),'Else':([99,],[100,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'DeclBlock':([0,],[2,]),'CommandBlock':([2,65,72,101,],[4,89,95,102,]),'Command':([2,4,65,72,89,95,101,102,],[5,21,5,5,21,21,5,21,]),'Assign':([2,4,65,72,89,95,101,102,],[6,6,6,6,6,6,6,6,]),'IfThenElse':([2,4,65,72,89,95,101,102,],[8,8,8,8,8,8,8,8,]),'WhileDo':([2,4,65,72,89,95,101,102,],[9,9,9,9,9,9,9,9,]),'Vars':([3,],[13,]),'Var':([3,13,],[14,35,]),'intvar':([3,13,],[15,15,]),'boolvar':([3,13,],[16,16,]),'stringvar':([3,13,],[17,17,]),'ExpressionB':([11,12,23,28,50,51,60,],[24,33,46,61,73,74,84,]),'ExpressionI':([11,12,23,28,50,51,52,53,54,55,56,57,60,76,],[26,26,45,62,26,26,75,77,78,79,80,81,26,96,]),'TermI':([11,12,23,28,50,51,52,53,54,55,56,57,58,59,60,76,],[29,29,29,29,29,29,29,29,29,29,29,29,82,83,29,29,]),'factorI':([11,12,23,28,50,51,52,53,54,55,56,57,58,59,60,63,64,76,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,87,88,30,]),'PrintableList':([22,],[39,]),'PrintableElem':([22,70,],[40,93,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> DeclBlock CommandBlock','Program',2,'p_lang_grammar','lang_yacc.py',9),
  ('DeclBlock -> DeclBegin Vars DeclEnd','DeclBlock',3,'p_lang_decls','lang_yacc.py',19),
  ('Vars -> Vars Var','Vars',2,'p_lang_vars_1','lang_yacc.py',23),
  ('Vars -> Var','Vars',1,'p_lang_vars_2','lang_yacc.py',28),
  ('Var -> intvar','Var',1,'p_lang_var_int','lang_yacc.py',32),
  ('Var -> boolvar','Var',1,'p_lang_var_bool','lang_yacc.py',36),
  ('Var -> stringvar','Var',1,'p_lang_var_str','lang_yacc.py',40),
  ('intvar -> IntDecl Name Decl Integer','intvar',4,'p_lang_intvar','lang_yacc.py',44),
  ('intvar -> IntDecl Name','intvar',2,'p_lang_intvar_default','lang_yacc.py',59),
  ('boolvar -> BoolDecl Name Decl Bool','boolvar',4,'p_lang_boolvar','lang_yacc.py',74),
  ('boolvar -> BoolDecl Name','boolvar',2,'p_lang_boolvar_default','lang_yacc.py',89),
  ('stringvar -> StringDecl Name Decl String','stringvar',4,'p_lang_stringvar','lang_yacc.py',104),
  ('stringvar -> StringDecl Name','stringvar',2,'p_lang_stringvar_default','lang_yacc.py',119),
  ('CommandBlock -> CommandBlock Command','CommandBlock',2,'p_lang_commandblock_1','lang_yacc.py',135),
  ('CommandBlock -> Command','CommandBlock',1,'p_lang_commandblock_2','lang_yacc.py',140),
  ('Command -> Assign','Command',1,'p_lang_command_1','lang_yacc.py',147),
  ('Assign -> Name ASSIGN ExpressionI','Assign',3,'p_lang_command_assign_int','lang_yacc.py',152),
  ('Assign -> Name ASSIGN ExpressionB','Assign',3,'p_lang_command_assign_2','lang_yacc.py',174),
  ('Assign -> Name ASSIGN String','Assign',3,'p_lang_command_assign_3','lang_yacc.py',197),
  ('Assign -> Name ASSIGN ReadString LPAREN RPAREN','Assign',5,'p_lang_command_assign_4','lang_yacc.py',219),
  ('PrintableElem -> Name','PrintableElem',1,'p_lang_comma_sep_var','lang_yacc.py',241),
  ('PrintableElem -> Integer','PrintableElem',1,'p_lang_comma_sep_int','lang_yacc.py',252),
  ('PrintableElem -> Bool','PrintableElem',1,'p_lang_comma_sep_bool','lang_yacc.py',257),
  ('PrintableElem -> String','PrintableElem',1,'p_lang_comma_sep_string','lang_yacc.py',262),
  ('PrintableList -> PrintableList COMMA PrintableElem','PrintableList',3,'p_lang_comma_sep_list_not_empty','lang_yacc.py',267),
  ('PrintableList -> PrintableElem','PrintableList',1,'p_lang_comma_sep_list_empty','lang_yacc.py',272),
  ('Command -> WriteString LPAREN PrintableList RPAREN','Command',4,'p_lang_command_4','lang_yacc.py',276),
  ('ExpressionI -> ExpressionI PLUS TermI','ExpressionI',3,'p_lang_expressionI_plus','lang_yacc.py',280),
  ('ExpressionI -> ExpressionI MINUS TermI','ExpressionI',3,'p_lang_expressionI_minus','lang_yacc.py',286),
  ('ExpressionI -> TermI','ExpressionI',1,'p_lang_expressionI_termI','lang_yacc.py',292),
  ('TermI -> TermI TIMES factorI','TermI',3,'p_lang_termI_mul','lang_yacc.py',296),
  ('TermI -> TermI DIVIDE factorI','TermI',3,'p_lang_termI_div','lang_yacc.py',302),
  ('TermI -> factorI','TermI',1,'p_lang_termI','lang_yacc.py',308),
  ('factorI -> Integer','factorI',1,'p_lang_factorI_int','lang_yacc.py',312),
  ('factorI -> Name','factorI',1,'p_lang_factorI_var','lang_yacc.py',316),
  ('factorI -> LPAREN ExpressionI RPAREN','factorI',3,'p_lang_factorI_paren','lang_yacc.py',338),
  ('ExpressionB -> Bool','ExpressionB',1,'p_lang_expressionB_base','lang_yacc.py',342),
  ('ExpressionB -> ExpressionI','ExpressionB',1,'p_lang_expressionB_expressionI','lang_yacc.py',349),
  ('ExpressionB -> ExpressionB AND ExpressionB','ExpressionB',3,'p_lang_expressionB_and','lang_yacc.py',387),
  ('ExpressionB -> ExpressionB OR ExpressionB','ExpressionB',3,'p_lang_expressionB_or','lang_yacc.py',394),
  ('ExpressionB -> NOT LPAREN ExpressionB RPAREN','ExpressionB',4,'p_lang_expressionB_not','lang_yacc.py',407),
  ('ExpressionB -> LPAREN ExpressionB RPAREN','ExpressionB',3,'p_lang_expressionB_paren','lang_yacc.py',412),
  ('ExpressionB -> ExpressionI LT ExpressionI','ExpressionB',3,'p_lang_expressionB_lt','lang_yacc.py',416),
  ('ExpressionB -> ExpressionI LE ExpressionI','ExpressionB',3,'p_lang_expressionB_le','lang_yacc.py',422),
  ('ExpressionB -> ExpressionI GT ExpressionI','ExpressionB',3,'p_lang_expressionB_gt','lang_yacc.py',428),
  ('ExpressionB -> ExpressionI GE ExpressionI','ExpressionB',3,'p_lang_expressionB_ge','lang_yacc.py',434),
  ('ExpressionB -> ExpressionI EQ ExpressionI','ExpressionB',3,'p_lang_expressionB_eq','lang_yacc.py',440),
  ('ExpressionB -> ExpressionI NEQ ExpressionI','ExpressionB',3,'p_lang_expressionB_neq','lang_yacc.py',446),
  ('Command -> IfThenElse','Command',1,'p_lang_command_ifthenelse','lang_yacc.py',453),
  ('IfThenElse -> If ExpressionB Then LBRACKET CommandBlock RBRACKET Else LBRACKET CommandBlock RBRACKET','IfThenElse',10,'p_lang_ifthenelse','lang_yacc.py',457),
  ('Command -> WhileDo','Command',1,'p_lang_command_while','lang_yacc.py',468),
  ('WhileDo -> While ExpressionB LBRACKET CommandBlock RBRACKET','WhileDo',5,'p_lang_while','lang_yacc.py',472),
]
