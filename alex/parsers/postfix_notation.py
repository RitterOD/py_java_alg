import ply.lex as lex
import re

def transform_to_postfix_notation(tkn_lst):
    pass

def build_token_lst(lexer, data):
    lexer.input(data)
    rv = []
    while True:
        tok = lexer.token()  # читаем следующий токен
        if not tok: break  # закончились печеньки
        rv.append(tok)
    return rv

# без этой штуки ничего не сынтерпретируется, потому что этот массив шарится между лексером и парсером и кроме того используется внутренне библиотекой
tokens = (
    'START', 'VAR', 'EQUAL', 'FUNC',
    'STRING', 'ECHO', 'COLON', 'COMA',
    'OPEN', 'CLOSE', 'NUM', 'PLUSMINUS', 'DIVMUL'
)

# определим регулярку для абстрактного идетификатора
ident = r'[a-z]\w*'

# для каждого токена из массива мы должны написать его определение вида t_ИМЯТОКЕНА = регулярка
t_START = r'\<\?'
t_VAR = r'\$'+ident # очень удобно, правда?
t_EQUAL = r'\='
t_FUNC = ident
t_STRING = r'"(\\.|[^"])*"'
t_ECHO = r'echo'
t_COLON = r';'
t_COMA = r','
t_OPEN = r'\('
t_CLOSE = r'\)'
t_NUM = r'\d+'
t_PLUSMINUS = r'\+|\-'
t_DIVMUL = r'/|\*'

# здесь мы игнорируем незначащие символы. Нам ведь все равно, написано $var=$value или $var   =  $value
t_ignore = ' \r\n\t\f'

# а здесь мы обрабатываем ошибки. Кстати заметьте формат названия функции
def t_error(t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.UNICODE | re.DOTALL)

data = '2+2'

lexer.input(data)


while True:
    tok = lexer.token() # читаем следующий токен
    if not tok: break      # закончились печеньки
    print (tok)