import os.path

from antlr4 import *
from gen.Java8Lexer import Java8Lexer
from gen.Java8Parser import Java8Parser


class Q3Listener(ParseTreeListener):

    def __init__(self, file_name):
        self.file_name = file_name
        self.current_class = None

    def enterClassDeclaration(self, ctx: Java8Parser.ClassDeclarationContext):
        if ctx.normalClassDeclaration():
            self.current_class = ctx.normalClassDeclaration().Identifier().getText()

    def exitClassDeclaration(self, ctx: Java8Parser.ClassDeclarationContext):
        self.current_class = None

    def enterMethodDeclaration(self, ctx: Java8Parser.MethodDeclarationContext):
        method_name = ctx.methodHeader().methodDeclarator().Identifier().getText()
        params_ctx = ctx.methodHeader().methodDeclarator().formalParameterList()
        params = self.formatParameters(params_ctx) if params_ctx else "None"
        return_type = ctx.methodHeader().result().getText()

        method_body = ctx.methodBody()
        if method_body and method_body.block():
            block_statements = method_body.block().blockStatements()

            if block_statements is None or len(block_statements.blockStatement()) == 0:
                print(
                    f'Empty method: {method_name}, Params: {f"[{params}]" if params != "None" else params}, Return Type: {return_type}, Class: {self.current_class}, File: {self.file_name}')
            elif self.isUnsupportedOperationException(block_statements):
                print(
                    f'UnsupportedOperationException method: {method_name}, Params: {f"[{params}]" if params != "None" else params}, Return Type: {return_type}, Class: {self.current_class}, File: {self.file_name}')
            else:
                print(
                    f'Normal method: {method_name}, Params: {f"[{params}]" if params != "None" else params}, Return Type: {return_type}, Class: {self.current_class}, File: {self.file_name}')

    def isUnsupportedOperationException(self, block_statements):
        if len(block_statements.blockStatement()) == 1:
            statement_ctx = block_statements.blockStatement(0).statement()
            if hasattr(statement_ctx, 'statementWithoutTrailingSubstatement'):
                stmt_without_trailing = statement_ctx.statementWithoutTrailingSubstatement()
                if hasattr(stmt_without_trailing, 'throwStatement'):
                    throw_stmt = stmt_without_trailing.throwStatement()
                    if throw_stmt and 'UnsupportedOperationException' in throw_stmt.expression().getText():
                        return True
        return False

    def formatParameters(self, params_ctx):
        if not params_ctx or not params_ctx.formalParameters():
            return "None"
        formatted_params = []
        for param in params_ctx.formalParameters().formalParameter():
            param_type = param.unannType().getText()
            param_name = param.variableDeclaratorId().Identifier().getText()
            formatted_params.append(f'{param_type} {param_name}')

        if params_ctx.lastFormalParameter():
            last_param = params_ctx.lastFormalParameter()
            if last_param.formalParameter():  # Check for regular parameter
                param_type = last_param.formalParameter().unannType().getText()
                param_name = last_param.formalParameter().variableDeclaratorId().Identifier().getText()
                formatted_params.append(f'{param_type} {param_name}')
            elif last_param.variableArityParameter():  # Check for varargs parameter
                param_type = last_param.variableArityParameter().unannType().getText()
                param_name = last_param.variableArityParameter().variableDeclaratorId().Identifier().getText()
                formatted_params.append(f'{param_type}... {param_name}')

        return ', '.join(formatted_params)


file_address = input("Enter your java file address: ")
file_stream = FileStream(file_address)
lexer = Java8Lexer(file_stream)
token = CommonTokenStream(lexer)
parser = Java8Parser(token)
parse_tree = parser.compilationUnit()
walker = ParseTreeWalker()
my_listener = Q3Listener(os.path.abspath(file_address))
walker.walk(my_listener, parse_tree)
