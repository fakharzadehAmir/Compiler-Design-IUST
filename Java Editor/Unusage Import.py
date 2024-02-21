from antlr4 import *
from gen.Java8Lexer import Java8Lexer
from gen.Java8Parser import Java8Parser


class Q1Listener(ParseTreeListener):
    def __init__(self):
        self.imported_classes = set()
        self.used_classes = set()
        self.is_in_declaration = False

    def enterUnannClassType_lfno_unannClassOrInterfaceType(self, ctx:Java8Parser.UnannClassType_lfno_unannClassOrInterfaceTypeContext):
        class_name = ctx.getText()
        if self.is_in_declaration:
            self.used_classes.add(class_name)

    def enterImportDeclaration(self, ctx: Java8Parser.ImportDeclarationContext):
        imported_class = ctx.getText().split('.')[-1].strip(';')
        self.imported_classes.add(imported_class)

    def enterLocalVariableDeclaration(self, ctx: Java8Parser.LocalVariableDeclarationContext):
        self.is_in_declaration = True

    def exitLocalVariableDeclaration(self, ctx: Java8Parser.LocalVariableDeclarationContext):
        self.is_in_declaration = False

    def getUnusedImports(self):
        return self.imported_classes - self.used_classes


file_address = input("Enter your java file address: ")
file_stream = FileStream(file_address)
lexer = Java8Lexer(file_stream)
token = CommonTokenStream(lexer)
parser = Java8Parser(token)
parse_tree = parser.compilationUnit()
walker = ParseTreeWalker()
my_listener = Q1Listener()
walker.walk(my_listener, parse_tree)
print("used classes: ", my_listener.used_classes)
print("unused classes: ", my_listener.getUnusedImports())

