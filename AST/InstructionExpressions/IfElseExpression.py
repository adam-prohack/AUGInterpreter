import AST

class IfElseExpression(AST.InstructionExpressionBase):
    def __init__(self, condition : AST.BooleanExpressionBase, main_expression : AST.InstructionExpressionBase):
        self.condition = condition
        self.main_expression = main_expression
    def __init__(self, condition : AST.BooleanExpressionBase, main_expression : AST.InstructionExpressionBase, else_expression : AST.InstructionExpressionBase):
        self.condition = condition
        self.main_expression = main_expression
        self.else_expression = else_expression
    def run(self, variables):
        if self.condition.execute(variables):
            self.main_expression.run(variables)
        else:
            self.else_expression.run(variables)