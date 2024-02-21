from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from Gen.Java8ParserListener import Java8ParserListener


class EjioguMetricsListener(Java8ParserListener):
    def __init__(self):
        self.maxDepth = 0
        self.currentDepth = 0
        self.rootChildren = 0
        self.monadicNodes = 0
        self.totalNodes = 0

    def enterEveryRule(self, ctx: ParserRuleContext):
        self.currentDepth += 1
        self.maxDepth = max(self.maxDepth, self.currentDepth)
        self.totalNodes += 1

        if self.currentDepth == 1:
            self.rootChildren = len(ctx.children)

        if ctx.getChildCount() == 1 and isinstance(ctx.getChild(0), TerminalNodeImpl):
            self.monadicNodes += 1

    def exitEveryRule(self, ctx: ParserRuleContext):
        self.currentDepth -= 1

    def get_structural_complexity(self):
        return self.maxDepth * self.rootChildren * self.monadicNodes

    def get_software_size(self):
        return self.totalNodes - 1
