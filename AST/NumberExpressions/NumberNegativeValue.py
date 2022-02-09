import AST

class NumberNegativeValue(AST.NumberExpressionBase):
    def __init__(self, number_expression : AST.NumberExpressionBase):
        self.number_expression = number_expression
    def execute(self, variables) -> int:
        value = 0 - self.number_expression.execute(variables)

        if AST.debug_enabled:
            print('NodeType=%r, Value=%r' % (type(self).__name__, value))
        return value
