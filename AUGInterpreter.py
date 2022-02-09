import AUGParser
import AST

lexer = AUGParser.Lexer()
parser = AUGParser.Parser()

input_code = open("example_code.aug", "r").read()
if AST.debug_enabled:
    for tok in lexer.tokenize(input_code):
        print('type=%r, value=%r' % (tok.type, tok.value))

program = parser.parse(lexer.tokenize(input_code))
program.run({})