import AST

class PrintNumberFunction(AST.InstructionExpressionBase):
    def __init__(self, expression : AST.NumberExpressionBase):
        self.expression = expression
    def run(self, variables):
        print(self.expression.execute(variables))