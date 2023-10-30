from antlr4 import *
from Gen.ArithmeticLexer import ArithmeticLexer
from Gen.ArithmeticParser import ArithmeticParser
from Code.CalculatorListener_v2 import CalculatorListener
from io import StringIO

input_expression = input("Enter an arithmetic expression: ")
lexer = ArithmeticLexer(InputStream(input_expression))
token_stream = CommonTokenStream(lexer)
parser = ArithmeticParser(token_stream)
parse_tree = parser.start()
listener = CalculatorListener()
walker = ParseTreeWalker()
walker.walk(listener, parse_tree)
result = listener.result
print("Result:", result)