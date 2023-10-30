from antlr4 import *
from Gen.TypeCheckerLexer import TypeCheckerLexer
from Gen.TypeCheckerParser import TypeCheckerParser
from io import StringIO
from MyCode.TypeCheckerListener_V2 import TypeCheckListener


input_expression = input("Enter an expression: ")
lexer = TypeCheckerLexer(InputStream(input_expression))
token_stream = CommonTokenStream(lexer)
parser = TypeCheckerParser(token_stream)
parse_tree = parser.start()
listener = TypeCheckListener()
walker = ParseTreeWalker()
try:
    walker.walk(listener, parse_tree)
except Exception as e:
    print(e)
