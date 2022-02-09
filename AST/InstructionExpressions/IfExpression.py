import AST

class IfExpression(AST.InstructionExpressionBase):
    def __init__(self, condition : AST.BooleanExpressionBase, main_expression : AST.InstructionExpressionBase):
        self.condition = condition
        self.main_expression = main_expression
    def run(self, variables):
        if self.condition.execute(variables):
            self.main_expression.run(variables)