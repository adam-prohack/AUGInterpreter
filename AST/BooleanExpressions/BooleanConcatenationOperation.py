import AST

class BooleanConcatenationOperation(AST.BooleanExpressionBase):
    def __init__(self, left_expression : AST.BooleanExpressionBase, operator : str, right_expression : AST.BooleanExpressionBase):
        self.left_expression = left_expression
        self.operator = operator
        self.right_expression = right_expression
    def execute(self, variables) -> bool:
        left_value = self.left_expression.execute(variables)
        right_value = self.right_expression.execute(variables)
        value = 0

        if self.operator == "||":
            value = left_value or right_value
        elif self.operator == "&&":
            value = left_value and right_value

        if AST.debug_enabled:
            print('NodeType=%r, LeftExpressionValue=%r, RightExpressionValue=%r, Value=%r' % (type(self).__name__, left_value, right_value, value))
        return value
