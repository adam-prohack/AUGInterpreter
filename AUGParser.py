import sly
import pprint
import AST

class Lexer(sly.Lexer):
    tokens = {
        TRUE, FALSE, AND, OR, NOT, BEGIN, END, EXIT, IF, THEN, ELSE, UNTIL, DO, WHILE,
        ASSIGN, PLUS, MINUS, MULTIPLIER, DIVIDER, MODULO,
        LPAR, RPAR, COMMA, SEMICOLON, 
        SEQ_OP, SNEQ_OP, NEQ_OP, NNEQ_OP, NLE_OP, NGE_OP, NLT_OP, NGT_OP,
        READINT_FUNC, READSTR_FUNC, POSITION_FUNC, LENGTH_FUNC, CONCATENATE_FUNC, SUBSTRING_FUNC, PRINT_FUNC,
        NUM, STRING, IDENT,
    }
    ignore = ' \t'
    ignore_newline = r'\n+'
    
    # Keywords
    TRUE = r'true'
    FALSE = r'false'
    AND = r'and'
    OR = r'or'
    NOT = r'not'
    BEGIN = r'begin'
    END = r'end'
    EXIT = r'exit'
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'
    UNTIL = r'until'
    DO = r'do'
    WHILE = r'while'

    # Special symbols
    ASSIGN = r'\:\='
    PLUS = r'\+'
    MINUS = r'\-'
    MULTIPLIER = r'\*'
    DIVIDER = r'\/'
    MODULO = r'\%'
    LPAR = r'\('
    RPAR = r'\)'
    COMMA = r'\,'
    SEMICOLON = r'\;'

    # Boolean operators
    SEQ_OP = r'\=\='
    SNEQ_OP = r'\!\='
    NEQ_OP = r'\='
    NNEQ_OP = r'\<\>'
    NLE_OP = r'\<\='
    NGE_OP = r'\>\='
    NLT_OP = r'\<'
    NGT_OP = r'\>'

    # Functions
    READINT_FUNC = r'readint'
    READSTR_FUNC = r'readstr'
    POSITION_FUNC = r'position'
    LENGTH_FUNC = r'length'
    CONCATENATE_FUNC = r'concatenate'
    SUBSTRING_FUNC = r'substring'
    PRINT_FUNC = r'print'

    # Tokens
    NUM = r'\d+'
    STRING = r'\"[^"]*\"'
    IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

class Parser(sly.Parser):
    debugfile = 'debug.out'
    debug_enabled = False
    tokens = Lexer.tokens
    precedence = (
        ('left', PLUS, MINUS),
        ('left', MULTIPLIER, DIVIDER, MODULO),
        ('right', UMINUS),
        ('left', IF),
        ('left', AND, OR),
        ('left', NUM),
        ('left', STRING)
    )

    variables = {}

    # program jako taki
    @_('instr')
    def program(self, p):
        return p.instr

    # wyrażenie numeryczne, którego wartością jest liczba
    @_('num_expr PLUS t_num_expr')
    def num_expr(self, p): 
        return AST.NumberSimpleOperation(p.num_expr, "+", p.t_num_expr)
    @_('num_expr MINUS t_num_expr')
    def num_expr(self, p): 
        return AST.NumberSimpleOperation(p.num_expr, "-", p.t_num_expr)
    @_('t_num_expr')
    def num_expr(self, p): 
        return p.t_num_expr

    @_('t_num_expr MULTIPLIER f_num_expr')
    def t_num_expr(self, p):
        return AST.NumberSimpleOperation(p.t_num_expr, "*", p.f_num_expr)
    @_('t_num_expr DIVIDER f_num_expr')
    def t_num_expr(self, p):
        return AST.NumberSimpleOperation(p.t_num_expr, "/", p.f_num_expr)
    @_('t_num_expr MODULO f_num_expr')
    def t_num_expr(self, p):
        return AST.NumberSimpleOperation(p.t_num_expr, "%", p.f_num_expr)
    @_('f_num_expr')
    def t_num_expr(self, p):
        return p.f_num_expr
    
    @_('NUM')
    def f_num_expr(self, p):
        return AST.NumberValue(int(p.NUM))
    @_('IDENT')
    def f_num_expr(self, p):
        return AST.NumberVariable(p.IDENT)
    @_('READINT_FUNC')
    def f_num_expr(self, p):
        return AST.NumberReadInputOperation()
    @_('MINUS num_expr %prec UMINUS')
    def f_num_expr(self, p):
        return AST.NumberNegativeValue(p.num_expr)
    @_('LPAR num_expr RPAR')
    def f_num_expr(self, p):
        return p.num_expr
    @_('LENGTH_FUNC LPAR str_expr RPAR')
    def f_num_expr(self, p):
        return AST.StringLengthFunction(p.str_expr)
    @_('POSITION_FUNC LPAR str_expr COMMA str_expr RPAR')
    def f_num_expr(self, p):
        return AST.StringPositionFunction(p.str_expr0, p.str_expr1)
 
    # wyrażenie, którego wartością jest łańcuch
    @_('STRING')
    def str_expr(self, p):
        return AST.StringValue(str(p.STRING)[1:-1])
    @_('IDENT')
    def str_expr(self, p):
        return AST.StringVariable(p.IDENT)
    @_('READSTR_FUNC')
    def str_expr(self, p):
        return AST.StringReadInputOperation()
    @_('CONCATENATE_FUNC LPAR str_expr COMMA str_expr RPAR')
    def str_expr(self, p):
        return AST.StringConcatenateFunction(p.str_expr0, p.str_expr1)
    @_('SUBSTRING_FUNC LPAR str_expr COMMA num_expr COMMA num_expr RPAR')
    def str_expr(self, p):
        return AST.StringSubstringFunction(p.str_expr, p.num_expr0, p.num_expr1)

    # relacje logiczne    
    @_('bool_expr OR t_bool_expr')
    def bool_expr(self, p):
        return AST.BooleanConcatenationOperation(p.bool_expr, "||", p.t_bool_expr)
    @_('t_bool_expr')
    def bool_expr(self, p):
        return p.t_bool_expr

    @_('t_bool_expr AND f_bool_expr')
    def t_bool_expr(self, p):
        return AST.BooleanConcatenationOperation(p.t_bool_expr, "&&", p.f_bool_expr)
    @_('f_bool_expr')
    def t_bool_expr(self, p):
        return p.f_bool_expr

    @_('TRUE')
    def f_bool_expr(self, p):
        return AST.BooleanValue(True)
    @_('FALSE')
    def f_bool_expr(self, p):
        return AST.BooleanValue(False)
    @_('LPAR bool_expr RPAR')
    def f_bool_expr(self, p):
        return p.bool_expr
    @_('NOT bool_expr')
    def f_bool_expr(self, p):
        return AST.BooleanNegativeValue(p.bool_expr)
    @_('num_expr NEQ_OP num_expr')
    def f_bool_expr(self, p):
        return AST.BooleanNumberComparsionOperation(p.num_expr0, "=", p.num_expr1)
    @_('num_expr NNEQ_OP num_expr')
    def f_bool_expr(self, p):
        return AST.BooleanNumberComparsionOperation(p.num_expr0, "<>", p.num_expr1)
    @_('num_expr NLT_OP num_expr')
    def f_bool_expr(self, p):
        return AST.BooleanNumberComparsionOperation(p.num_expr0, "<", p.num_expr1)
    @_('num_expr NLE_OP num_expr')
    def f_bool_expr(self, p):
        return AST.BooleanNumberComparsionOperation(p.num_expr0, "<=", p.num_expr1)
    @_('num_expr NGT_OP num_expr')
    def f_bool_expr(self, p):
        return AST.BooleanNumberComparsionOperation(p.num_expr0, ">", p.num_expr1)
    @_('num_expr NGE_OP num_expr')
    def f_bool_expr(self, p):
        return AST.BooleanNumberComparsionOperation(p.num_expr0, ">=", p.num_expr1)
    
    @_('str_expr SNEQ_OP str_expr')
    def f_bool_expr(self, p):
        return AST.BooleanStringComparsionOperation(p.str_expr0, "!=", p.str_expr1)
    @_('str_expr SEQ_OP str_expr')
    def f_bool_expr(self, p):
        return AST.BooleanStringComparsionOperation(p.str_expr0, "==", p.str_expr1)

    # podstawowe konstrukcje
    @_('assign_stat')
    def simple_instr(self, p):
        return p.assign_stat
    @_('if_stat')
    def simple_instr(self, p):
        return p.if_stat
    @_('while_stat')
    def simple_instr(self, p):
        return p.while_stat
    @_('until_stat')
    def simple_instr(self, p):
        return p.until_stat
    @_('BEGIN instr END')
    def simple_instr(self, p):
        return p.instr
    @_('output_stat')
    def simple_instr(self, p):
        return p.output_stat
    @_('EXIT')
    def simple_instr(self, p):
        return AST.ExitInstruction()

    # ciąg instrukcji
    @_('instr SEMICOLON simple_instr')
    def instr(self, p):
        return AST.InstructionPair(p.instr, p.simple_instr)
    @_('')
    def instr(self, p):
        return AST.NoOperation()
    
    # przypisanie
    @_('IDENT ASSIGN num_expr')
    def assign_stat(self, p):
        return AST.AssignNumberInstruction(p.IDENT, p.num_expr)
    @_('IDENT ASSIGN str_expr')
    def assign_stat(self, p):
        return AST.AssignStringInstruction(p.IDENT, p.str_expr)

    # konstrukcja warunkowa
    @_('IF bool_expr THEN simple_instr')
    def if_stat(self, p):
        return AST.IfExpression(p.bool_expr, p.simple_instr)
    @_('IF bool_expr THEN simple_instr ELSE simple_instr')
    def if_stat(self, p):
        return AST.IfElseExpression(p.bool_expr, p.simple_instr0, p.simple_instr1)

    # petla "while"
    @_('WHILE bool_expr DO simple_instr')
    def while_stat(self, p):
        return AST.WhileExpression(p.bool_expr, p.simple_instr)

    # petla "until"
    @_('DO simple_instr UNTIL bool_expr')
    def until_stat(self, p):
        return AST.UntilExpression(p.bool_expr, p.simple_instr)

    # wypisanie informacji na ekran
    @_('PRINT_FUNC LPAR num_expr RPAR')
    def output_stat(self, p):
        return AST.PrintNumberFunction(p.num_expr)
    @_('PRINT_FUNC LPAR str_expr RPAR')
    def output_stat(self, p):
        return AST.PrintNumberFunction(p.str_expr)