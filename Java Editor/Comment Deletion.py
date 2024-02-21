from antlr4 import *
from gen.Java8Lexer import Java8Lexer
from gen.Java8Parser import Java8Parser


class Q4Listener(ParseTreeListener):
    def __init__(self):
        self.output = []
        self.is_in_comment = False
        self.current_context = []

    def enterEveryRule(self, ctx):
        self.current_context.append(type(ctx).__name__)

    def exitEveryRule(self, ctx):
        self.current_context.pop()

    def visitTerminal(self, node):
        text = node.getText()
        token_type = node.getSymbol().type if node.getSymbol() else None
        if token_type in [Java8Lexer.COMMENT, Java8Lexer.LINE_COMMENT]:
            self.is_in_comment = True
            if any(keyword in text for keyword in ['if(', 'switch', 'for(']):
                self.is_in_comment = False
                return
        if self.is_in_comment and (token_type == Token.EOF or text == '\n'):
            self.is_in_comment = False
            return
        if not self.is_in_comment:
            self.output.append(text)

    def getFilteredOutput(self):
        return ''.join(self.output)


file_address = input("Enter your java file address: ")
file_stream = FileStream(file_address)
lexer = Java8Lexer(file_stream)
token = CommonTokenStream(lexer)
parser = Java8Parser(token)
parse_tree = parser.compilationUnit()
walker = ParseTreeWalker()
my_listener = Q4Listener()
walker.walk(my_listener, parse_tree)
outfile = "edited_q4.java"
with open(outfile, 'w') as f:
    f.write(my_listener.getFilteredOutput())


