
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLTGTLEGEEQNEQleftPLUSMINUSleftMODTIMESDIVIDEleftORleftANDAND ASSIGN Bool BoolDecl COMMA DIVIDE Decl DeclBegin DeclEnd EQ Else Err GE GT If IntDecl Integer LBRACKET LE LPAREN LSQBRACKET LT MINUS MOD NEQ NOT Name OR PLUS RBRACKET RPAREN RSQBRACKET ReadString String StringDecl TIMES Then While WriteStringProgram : DeclBlock CommandBlockDeclBlock : DeclBegin Vars DeclEndVars : Vars VarVars : VarVar : intvarVar : boolvarVar : stringvarVar : arrvarintvar : IntDecl Name Decl ExpressionIintvar : IntDecl Nameboolvar : BoolDecl Name Decl Boolboolvar : BoolDecl Namestringvar : StringDecl Name Decl Stringstringvar : StringDecl Namearrvar : IntDecl LSQBRACKET Integer RSQBRACKET NameCommandBlock : CommandBlock CommandCommandBlock : CommandCommand : AssignAssign : Name ASSIGN ExpressionIAssign : Name LSQBRACKET ExpressionI RSQBRACKET ASSIGN ExpressionIAssign : Name ASSIGN ExpressionBAssign : Name ASSIGN StringAssign : Name ASSIGN ReadString LPAREN RPARENAssign : Name LSQBRACKET ExpressionI RSQBRACKET ASSIGN ReadString LPAREN RPARENPrintableElem : ExpressionIPrintableElem : ExpressionBPrintableElem : StringPrintableList : PrintableList COMMA PrintableElemPrintableList : PrintableElemCommand : WriteString LPAREN PrintableList RPARENCommand : Err LPAREN String RPARENExpressionI : ExpressionI PLUS TermIExpressionI : ExpressionI MINUS TermIExpressionI : TermITermI       : TermI TIMES factorITermI       : TermI DIVIDE factorITermI       : TermI MOD factorITermI       : factorIfactorI     : IntegerfactorI     : NamefactorI     : Name LSQBRACKET ExpressionI RSQBRACKETfactorI     : LPAREN ExpressionI RPARENfactorI     : MINUS LPAREN ExpressionI RPARENfactorI     : MINUS IntegerExpressionB : BoolExpressionB : ExpressionB AND ExpressionBExpressionB : ExpressionB OR ExpressionBExpressionB : NOT LPAREN ExpressionB RPARENExpressionB : LPAREN ExpressionB RPARENExpressionB : ExpressionI LT ExpressionIExpressionB : ExpressionI LE ExpressionIExpressionB : ExpressionI GT ExpressionIExpressionB : ExpressionI GE ExpressionIExpressionB : ExpressionI EQ ExpressionIExpressionB : ExpressionI NEQ ExpressionICommand : IfThenElseCommand : IfThenIfThenElse : If ExpressionB Then LBRACKET CommandBlock RBRACKET Else LBRACKET CommandBlock RBRACKETIfThen : If ExpressionB Then LBRACKET CommandBlock RBRACKETCommand : WhileDoWhileDo : While ExpressionB LBRACKET CommandBlock RBRACKET'
    
_lr_action_items = {'DeclBegin':([0,],[3,]),'$end':([1,4,5,6,9,10,11,24,30,34,36,37,38,52,53,54,76,83,85,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,114,117,118,119,120,122,124,127,130,],[0,-1,-17,-18,-56,-57,-60,-16,-45,-34,-38,-39,-40,-19,-21,-22,-44,-30,-31,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,-23,-48,-43,-41,-61,-20,-59,-24,-58,]),'WriteString':([2,4,5,6,9,10,11,24,30,34,36,37,38,40,52,53,54,76,78,83,85,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,108,114,116,117,118,119,120,122,124,127,128,129,130,],[7,7,-17,-18,-56,-57,-60,-16,-45,-34,-38,-39,-40,-2,-19,-21,-22,-44,7,-30,-31,7,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,7,-23,7,-48,-43,-41,-61,-20,-59,-24,7,7,-58,]),'Err':([2,4,5,6,9,10,11,24,30,34,36,37,38,40,52,53,54,76,78,83,85,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,108,114,116,117,118,119,120,122,124,127,128,129,130,],[8,8,-17,-18,-56,-57,-60,-16,-45,-34,-38,-39,-40,-2,-19,-21,-22,-44,8,-30,-31,8,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,8,-23,8,-48,-43,-41,-61,-20,-59,-24,8,8,-58,]),'Name':([2,4,5,6,9,10,11,13,14,21,22,23,24,25,27,28,30,32,34,36,37,38,40,52,53,54,57,59,60,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,84,85,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,108,110,114,115,116,117,118,119,120,122,124,127,128,129,130,],[12,12,-17,-18,-56,-57,-60,38,38,42,44,45,-16,38,38,38,-45,38,-34,-38,-39,-40,-2,-19,-21,-22,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-44,38,12,38,-30,38,-31,12,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,12,121,-23,38,12,-48,-43,-41,-61,-20,-59,-24,12,12,-58,]),'If':([2,4,5,6,9,10,11,24,30,34,36,37,38,40,52,53,54,76,78,83,85,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,108,114,116,117,118,119,120,122,124,127,128,129,130,],[13,13,-17,-18,-56,-57,-60,-16,-45,-34,-38,-39,-40,-2,-19,-21,-22,-44,13,-30,-31,13,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,13,-23,13,-48,-43,-41,-61,-20,-59,-24,13,13,-58,]),'While':([2,4,5,6,9,10,11,24,30,34,36,37,38,40,52,53,54,76,78,83,85,89,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,108,114,116,117,118,119,120,122,124,127,128,129,130,],[14,14,-17,-18,-56,-57,-60,-16,-45,-34,-38,-39,-40,-2,-19,-21,-22,-44,14,-30,-31,14,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,14,-23,14,-48,-43,-41,-61,-20,-59,-24,14,14,-58,]),'IntDecl':([3,15,16,17,18,19,20,34,36,37,38,41,42,44,45,76,94,101,102,103,104,105,109,111,112,118,119,121,],[21,21,-4,-5,-6,-7,-8,-34,-38,-39,-40,-3,-10,-12,-14,-44,-42,-32,-33,-35,-36,-37,-9,-11,-13,-43,-41,-15,]),'BoolDecl':([3,15,16,17,18,19,20,34,36,37,38,41,42,44,45,76,94,101,102,103,104,105,109,111,112,118,119,121,],[22,22,-4,-5,-6,-7,-8,-34,-38,-39,-40,-3,-10,-12,-14,-44,-42,-32,-33,-35,-36,-37,-9,-11,-13,-43,-41,-15,]),'StringDecl':([3,15,16,17,18,19,20,34,36,37,38,41,42,44,45,76,94,101,102,103,104,105,109,111,112,118,119,121,],[23,23,-4,-5,-6,-7,-8,-34,-38,-39,-40,-3,-10,-12,-14,-44,-42,-32,-33,-35,-36,-37,-9,-11,-13,-43,-41,-15,]),'RBRACKET':([5,6,9,10,11,24,30,34,36,37,38,52,53,54,76,83,85,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,108,114,116,117,118,119,120,122,124,127,129,130,],[-17,-18,-56,-57,-60,-16,-45,-34,-38,-39,-40,-19,-21,-22,-44,-30,-31,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,120,-23,124,-48,-43,-41,-61,-20,-59,-24,130,-58,]),'LPAREN':([7,8,13,14,25,27,28,31,32,35,55,57,59,60,61,64,65,66,67,68,69,70,71,72,73,74,75,77,79,84,115,123,],[25,26,32,32,32,32,57,61,32,75,86,57,32,32,32,57,57,57,57,57,57,57,57,57,57,57,57,57,57,32,57,125,]),'ASSIGN':([12,87,],[27,115,]),'LSQBRACKET':([12,21,38,],[28,43,77,]),'Bool':([13,14,25,27,32,59,60,61,81,84,],[30,30,30,30,30,30,30,30,111,30,]),'NOT':([13,14,25,27,32,59,60,61,84,],[31,31,31,31,31,31,31,31,31,]),'Integer':([13,14,25,27,28,32,35,43,57,59,60,61,64,65,66,67,68,69,70,71,72,73,74,75,77,79,84,115,],[37,37,37,37,37,37,76,80,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'MINUS':([13,14,25,27,28,32,33,34,36,37,38,48,52,56,57,59,60,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,84,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,115,118,119,122,],[35,35,35,35,35,35,71,-34,-38,-39,-40,71,71,71,35,35,35,35,71,35,35,35,35,35,35,35,35,35,35,35,35,-44,35,35,35,71,-42,71,71,71,71,71,71,-32,-33,-35,-36,-37,71,71,71,35,-43,-41,71,]),'DeclEnd':([15,16,17,18,19,20,34,36,37,38,41,42,44,45,76,94,101,102,103,104,105,109,111,112,118,119,121,],[40,-4,-5,-6,-7,-8,-34,-38,-39,-40,-3,-10,-12,-14,-44,-42,-32,-33,-35,-36,-37,-9,-11,-13,-43,-41,-15,]),'String':([25,26,27,82,84,],[50,51,54,112,50,]),'ReadString':([27,115,],[55,123,]),'Then':([29,30,34,36,37,38,76,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,117,118,119,],[58,-45,-34,-38,-39,-40,-44,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,-48,-43,-41,]),'AND':([29,30,34,36,37,38,39,49,53,62,76,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,117,118,119,],[59,-45,-34,-38,-39,-40,59,59,59,59,-44,-46,59,59,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,-48,-43,-41,]),'OR':([29,30,34,36,37,38,39,49,53,62,76,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,117,118,119,],[60,-45,-34,-38,-39,-40,60,60,60,60,-44,-46,-47,60,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,-48,-43,-41,]),'LBRACKET':([30,34,36,37,38,39,58,76,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,117,118,119,126,],[-45,-34,-38,-39,-40,78,89,-44,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,-48,-43,-41,128,]),'RPAREN':([30,34,36,37,38,46,47,48,49,50,51,62,63,76,86,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,113,117,118,119,125,],[-45,-34,-38,-39,-40,83,-29,-25,-26,-27,85,93,94,-44,114,94,-46,-47,117,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,118,-28,-48,-43,-41,127,]),'COMMA':([30,34,36,37,38,46,47,48,49,50,76,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,113,117,118,119,],[-45,-34,-38,-39,-40,84,-29,-25,-26,-27,-44,-46,-47,-49,-42,-50,-51,-52,-53,-54,-55,-32,-33,-35,-36,-37,-28,-48,-43,-41,]),'LT':([33,34,36,37,38,48,52,63,76,94,101,102,103,104,105,118,119,],[64,-34,-38,-39,-40,64,64,64,-44,-42,-32,-33,-35,-36,-37,-43,-41,]),'LE':([33,34,36,37,38,48,52,63,76,94,101,102,103,104,105,118,119,],[65,-34,-38,-39,-40,65,65,65,-44,-42,-32,-33,-35,-36,-37,-43,-41,]),'GT':([33,34,36,37,38,48,52,63,76,94,101,102,103,104,105,118,119,],[66,-34,-38,-39,-40,66,66,66,-44,-42,-32,-33,-35,-36,-37,-43,-41,]),'GE':([33,34,36,37,38,48,52,63,76,94,101,102,103,104,105,118,119,],[67,-34,-38,-39,-40,67,67,67,-44,-42,-32,-33,-35,-36,-37,-43,-41,]),'EQ':([33,34,36,37,38,48,52,63,76,94,101,102,103,104,105,118,119,],[68,-34,-38,-39,-40,68,68,68,-44,-42,-32,-33,-35,-36,-37,-43,-41,]),'NEQ':([33,34,36,37,38,48,52,63,76,94,101,102,103,104,105,118,119,],[69,-34,-38,-39,-40,69,69,69,-44,-42,-32,-33,-35,-36,-37,-43,-41,]),'PLUS':([33,34,36,37,38,48,52,56,63,76,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,109,118,119,122,],[70,-34,-38,-39,-40,70,70,70,70,-44,70,-42,70,70,70,70,70,70,-32,-33,-35,-36,-37,70,70,70,-43,-41,70,]),'RSQBRACKET':([34,36,37,38,56,76,80,94,101,102,103,104,105,107,118,119,],[-34,-38,-39,-40,87,-44,110,-42,-32,-33,-35,-36,-37,119,-43,-41,]),'TIMES':([34,36,37,38,76,94,101,102,103,104,105,118,119,],[72,-38,-39,-40,-44,-42,72,72,-35,-36,-37,-43,-41,]),'DIVIDE':([34,36,37,38,76,94,101,102,103,104,105,118,119,],[73,-38,-39,-40,-44,-42,73,73,-35,-36,-37,-43,-41,]),'MOD':([34,36,37,38,76,94,101,102,103,104,105,118,119,],[74,-38,-39,-40,-44,-42,74,74,-35,-36,-37,-43,-41,]),'Decl':([42,44,45,],[79,81,82,]),'Else':([124,],[126,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'DeclBlock':([0,],[2,]),'CommandBlock':([2,78,89,128,],[4,108,116,129,]),'Command':([2,4,78,89,108,116,128,129,],[5,24,5,5,24,24,5,24,]),'Assign':([2,4,78,89,108,116,128,129,],[6,6,6,6,6,6,6,6,]),'IfThenElse':([2,4,78,89,108,116,128,129,],[9,9,9,9,9,9,9,9,]),'IfThen':([2,4,78,89,108,116,128,129,],[10,10,10,10,10,10,10,10,]),'WhileDo':([2,4,78,89,108,116,128,129,],[11,11,11,11,11,11,11,11,]),'Vars':([3,],[15,]),'Var':([3,15,],[16,41,]),'intvar':([3,15,],[17,17,]),'boolvar':([3,15,],[18,18,]),'stringvar':([3,15,],[19,19,]),'arrvar':([3,15,],[20,20,]),'ExpressionB':([13,14,25,27,32,59,60,61,84,],[29,39,49,53,62,90,91,92,49,]),'ExpressionI':([13,14,25,27,28,32,57,59,60,61,64,65,66,67,68,69,75,77,79,84,115,],[33,33,48,52,56,63,88,33,33,33,95,96,97,98,99,100,106,107,109,48,122,]),'TermI':([13,14,25,27,28,32,57,59,60,61,64,65,66,67,68,69,70,71,75,77,79,84,115,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,101,102,34,34,34,34,34,]),'factorI':([13,14,25,27,28,32,57,59,60,61,64,65,66,67,68,69,70,71,72,73,74,75,77,79,84,115,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,103,104,105,36,36,36,36,36,]),'PrintableList':([25,],[46,]),'PrintableElem':([25,84,],[47,113,]),}

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
  ('Var -> arrvar','Var',1,'p_lang_var_arr','lang_yacc.py',44),
  ('intvar -> IntDecl Name Decl ExpressionI','intvar',4,'p_lang_intvar','lang_yacc.py',48),
  ('intvar -> IntDecl Name','intvar',2,'p_lang_intvar_default','lang_yacc.py',63),
  ('boolvar -> BoolDecl Name Decl Bool','boolvar',4,'p_lang_boolvar','lang_yacc.py',78),
  ('boolvar -> BoolDecl Name','boolvar',2,'p_lang_boolvar_default','lang_yacc.py',93),
  ('stringvar -> StringDecl Name Decl String','stringvar',4,'p_lang_stringvar','lang_yacc.py',108),
  ('stringvar -> StringDecl Name','stringvar',2,'p_lang_stringvar_default','lang_yacc.py',123),
  ('arrvar -> IntDecl LSQBRACKET Integer RSQBRACKET Name','arrvar',5,'p_lang_arrvar_default','lang_yacc.py',139),
  ('CommandBlock -> CommandBlock Command','CommandBlock',2,'p_lang_commandblock_1','lang_yacc.py',162),
  ('CommandBlock -> Command','CommandBlock',1,'p_lang_commandblock_2','lang_yacc.py',167),
  ('Command -> Assign','Command',1,'p_lang_command_1','lang_yacc.py',174),
  ('Assign -> Name ASSIGN ExpressionI','Assign',3,'p_lang_command_assign_int','lang_yacc.py',179),
  ('Assign -> Name LSQBRACKET ExpressionI RSQBRACKET ASSIGN ExpressionI','Assign',6,'p_lang_command_assign_arr_position','lang_yacc.py',226),
  ('Assign -> Name ASSIGN ExpressionB','Assign',3,'p_lang_command_assign_2','lang_yacc.py',252),
  ('Assign -> Name ASSIGN String','Assign',3,'p_lang_command_assign_3','lang_yacc.py',275),
  ('Assign -> Name ASSIGN ReadString LPAREN RPAREN','Assign',5,'p_lang_command_assign_4','lang_yacc.py',297),
  ('Assign -> Name LSQBRACKET ExpressionI RSQBRACKET ASSIGN ReadString LPAREN RPAREN','Assign',8,'p_lang_command_assign_arr_read','lang_yacc.py',313),
  ('PrintableElem -> ExpressionI','PrintableElem',1,'p_lang_comma_sep_expressionI','lang_yacc.py',340),
  ('PrintableElem -> ExpressionB','PrintableElem',1,'p_lang_comma_sep_expressionB','lang_yacc.py',345),
  ('PrintableElem -> String','PrintableElem',1,'p_lang_comma_sep_string','lang_yacc.py',350),
  ('PrintableList -> PrintableList COMMA PrintableElem','PrintableList',3,'p_lang_comma_sep_list_not_empty','lang_yacc.py',355),
  ('PrintableList -> PrintableElem','PrintableList',1,'p_lang_comma_sep_list_empty','lang_yacc.py',360),
  ('Command -> WriteString LPAREN PrintableList RPAREN','Command',4,'p_lang_command_4','lang_yacc.py',364),
  ('Command -> Err LPAREN String RPAREN','Command',4,'p_lang_command_error','lang_yacc.py',368),
  ('ExpressionI -> ExpressionI PLUS TermI','ExpressionI',3,'p_lang_expressionI_plus','lang_yacc.py',373),
  ('ExpressionI -> ExpressionI MINUS TermI','ExpressionI',3,'p_lang_expressionI_minus','lang_yacc.py',379),
  ('ExpressionI -> TermI','ExpressionI',1,'p_lang_expressionI_termI','lang_yacc.py',385),
  ('TermI -> TermI TIMES factorI','TermI',3,'p_lang_termI_mul','lang_yacc.py',389),
  ('TermI -> TermI DIVIDE factorI','TermI',3,'p_lang_termI_div','lang_yacc.py',395),
  ('TermI -> TermI MOD factorI','TermI',3,'p_lang_termI_mod','lang_yacc.py',401),
  ('TermI -> factorI','TermI',1,'p_lang_termI','lang_yacc.py',407),
  ('factorI -> Integer','factorI',1,'p_lang_factorI_int','lang_yacc.py',411),
  ('factorI -> Name','factorI',1,'p_lang_factorI_var','lang_yacc.py',415),
  ('factorI -> Name LSQBRACKET ExpressionI RSQBRACKET','factorI',4,'p_lang_factorI_arrvar','lang_yacc.py',437),
  ('factorI -> LPAREN ExpressionI RPAREN','factorI',3,'p_lang_factorI_paren','lang_yacc.py',463),
  ('factorI -> MINUS LPAREN ExpressionI RPAREN','factorI',4,'p_lang_factorI_minus_expressionI','lang_yacc.py',467),
  ('factorI -> MINUS Integer','factorI',2,'p_lang_factorI_minus_integer','lang_yacc.py',473),
  ('ExpressionB -> Bool','ExpressionB',1,'p_lang_expressionB_base','lang_yacc.py',479),
  ('ExpressionB -> ExpressionB AND ExpressionB','ExpressionB',3,'p_lang_expressionB_and','lang_yacc.py',518),
  ('ExpressionB -> ExpressionB OR ExpressionB','ExpressionB',3,'p_lang_expressionB_or','lang_yacc.py',525),
  ('ExpressionB -> NOT LPAREN ExpressionB RPAREN','ExpressionB',4,'p_lang_expressionB_not','lang_yacc.py',538),
  ('ExpressionB -> LPAREN ExpressionB RPAREN','ExpressionB',3,'p_lang_expressionB_paren','lang_yacc.py',543),
  ('ExpressionB -> ExpressionI LT ExpressionI','ExpressionB',3,'p_lang_expressionB_lt','lang_yacc.py',547),
  ('ExpressionB -> ExpressionI LE ExpressionI','ExpressionB',3,'p_lang_expressionB_le','lang_yacc.py',553),
  ('ExpressionB -> ExpressionI GT ExpressionI','ExpressionB',3,'p_lang_expressionB_gt','lang_yacc.py',559),
  ('ExpressionB -> ExpressionI GE ExpressionI','ExpressionB',3,'p_lang_expressionB_ge','lang_yacc.py',565),
  ('ExpressionB -> ExpressionI EQ ExpressionI','ExpressionB',3,'p_lang_expressionB_eq','lang_yacc.py',571),
  ('ExpressionB -> ExpressionI NEQ ExpressionI','ExpressionB',3,'p_lang_expressionB_neq','lang_yacc.py',577),
  ('Command -> IfThenElse','Command',1,'p_lang_command_ifthenelse','lang_yacc.py',584),
  ('Command -> IfThen','Command',1,'p_lang_command_ifthen','lang_yacc.py',588),
  ('IfThenElse -> If ExpressionB Then LBRACKET CommandBlock RBRACKET Else LBRACKET CommandBlock RBRACKET','IfThenElse',10,'p_lang_ifthenelse','lang_yacc.py',592),
  ('IfThen -> If ExpressionB Then LBRACKET CommandBlock RBRACKET','IfThen',6,'p_lang_ifthen','lang_yacc.py',603),
  ('Command -> WhileDo','Command',1,'p_lang_command_while','lang_yacc.py',611),
  ('WhileDo -> While ExpressionB LBRACKET CommandBlock RBRACKET','WhileDo',5,'p_lang_while','lang_yacc.py',615),
]
