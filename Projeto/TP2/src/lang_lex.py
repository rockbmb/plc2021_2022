import ply.lex as lex

t_PLUS       = r'\+'
t_MINUS      = r'\-'
t_TIMES      = r'\*'
t_DIVIDE     = r'\/'
t_MOD        = r'\%'
t_ASSIGN     = r'\<\-'
t_Decl       = r'\='
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_LBRACKET   = r'\{'
t_RBRACKET   = r'\}'
t_COMMA      = r'\,'
t_LSQBRACKET = r'\['
t_RSQBRACKET = r'\]'

t_GT         = r'\>'
t_GE         = r'\>\='
t_LT         = r'\<'
t_LE         = r'\<\='
t_EQ         = r'\=\='
t_NEQ        = r'\!\='

t_AND        = r'\&\&'
t_OR         = r'\|\|'
t_NOT        = r'\~'

reserved = {
    'DeclBegin' : 'DeclBegin',
    'DeclEnd' : 'DeclEnd',
    'int' : 'IntDecl',
    'bool' : 'BoolDecl',
    'string' : 'StringDecl',
    'read' : 'ReadString',
    'write' : 'WriteString',
    'if' : 'If',
    'then' : 'Then',
    'else' : 'Else',
    'while' : "While",
    "error" : 'Err'
}

def t_Bool(t):
    r'True|False'
    import distutils.util
    t.value = bool(distutils.util.strtobool(t.value))
    return t

def t_String(t):
    r'\"[^\"]*\"'
    return t

def t_Name(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    # Necessário para captar palavras reservadas.
    t.type = reserved.get(t.value, 'Name')
    return t

def t_Integer(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_comment(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

t_ignore = ' \r\n\t'

def t_error(t):
    print('Illegal character: ' + t.value[0])
    return

tokens = list(reserved.values()) + [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'ASSIGN',
    'Decl',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'LSQBRACKET',
    'RSQBRACKET',

    "GT",
    "GE",
    "LT",
    "LE",
    "EQ",
    "NEQ",
    'AND',
    'OR',
    'NOT',

    'Name',
    'Integer',
    'String',
    'Bool'
]

lexer = lex.lex()