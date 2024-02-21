from antlr4 import *
from Gen.Java8Lexer import Java8Lexer
from Gen.Java8ParserListener import Java8ParserListener


class ReadabilityMetricListener(Java8ParserListener):

    def __init__(self):
        self.lines_of_code = 0

    def visitTerminal(self, node):
        if node.symbol is None or node.symbol.type == -1:
            return
        line = node.symbol.line
        self.lines_of_code = max(self.lines_of_code, line)

    def get_lines_of_code(self):
        return self.lines_of_code

    def calculate_document_pages(self):
        L = self.get_lines_of_code() / 10
        return 49 * (L ** 1.01)
