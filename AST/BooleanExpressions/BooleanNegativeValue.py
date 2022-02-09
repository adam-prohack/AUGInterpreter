import AST

class BooleanNegativeValue(AST.BooleanExpressionBase):
    def __init__(self, expression : AST.BooleanExpressionBase):
        self.expression = expression
    def execute(self, variables) -> bool:
        value = not self.expression.execute(variables)

        if AST.debug_enabled:
            print('NodeType=%r, Value=%r' % (type(self).__name__, value))
        return value