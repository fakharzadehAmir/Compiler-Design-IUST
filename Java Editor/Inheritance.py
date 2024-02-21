from antlr4 import *
from gen.Java8Lexer import Java8Lexer
from gen.Java8Parser import Java8Parser


class Q2Listener(ParseTreeListener):
    def __init__(self):
        super().__init__()
        self.extended_class = {}
        self.current_class = ''

    def exitCompilationUnit(self, ctx: Java8Parser.CompilationUnitContext):
        for className, extended_classes in sorted(self.extended_class.items()):
            if len(extended_classes) != 0 :
                print(f"{className}: {extended_classes}")

    def enterNormalClassDeclaration(self, ctx: Java8Parser.NormalClassDeclarationContext):
        self.current_class = str(ctx.Identifier())
        if self.current_class not in self.extended_class:
            self.extended_class[self.current_class] = []

    def exitNormalClassDeclaration(self, ctx: Java8Parser.NormalClassDeclarationContext):
        self.current_class = ''

    def enterSuperclass(self, ctx: Java8Parser.SuperclassContext):
        superclass = ctx.getText()[7:]
        if superclass in self.extended_class:
            self.extended_class[superclass].append(self.current_class)
        else:
            self.extended_class[superclass] = [self.current_class]


file_address = input("Enter your java file address: ")
file_stream = FileStream(file_address)
lexer = Java8Lexer(file_stream)
token = CommonTokenStream(lexer)
parser = Java8Parser(token)
parse_tree = parser.compilationUnit()
walker = ParseTreeWalker()
my_listener = Q2Listener()
walker.walk(my_listener, parse_tree)

