import AST

class PrintStringFunction(AST.InstructionExpressionBase):
    def __init__(self, expression : AST.StringExpressionBase):
        self.expression = expression
    def run(self, variables):
        print(self.expression.execute(variables))