from Gen.Java8ParserListener import Java8ParserListener
import math


class HalsteadMetricListener(Java8ParserListener):

    def __init__(self):
        self.operators = set()
        self.operands = set()
        self.total_operators = 0
        self.total_operands = 0

    def enterEveryRule(self, ctx):
        self.operators.add(ctx.getRuleIndex())
        self.total_operators += 1

    def visitTerminal(self, node):
        self.operands.add(node.symbol.text)
        self.total_operands += 1

    def get_vocabulary(self):
        return len(self.operators) + len(self.operands)

    def get_length(self):
        return self.total_operators + self.total_operands

    def get_volume(self):
        n = self.get_vocabulary()
        N = self.get_length()
        return N * math.log2(n) if n > 0 else 0

    def get_difficulty(self):
        n1 = len(self.operators)
        n2 = len(self.operands)
        N2 = self.total_operands
        return (n1 * N2) / (2 * n2) if n2 != 0 else float('inf')

    def get_effort(self):
        difficulty = self.get_difficulty()
        volume = self.get_volume()
        return difficulty * volume

    def get_time_to_program(self, S=18):
        effort = self.get_effort()
        return effort / S
