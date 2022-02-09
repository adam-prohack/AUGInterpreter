import AST

class StringConcatenateFunction(AST.StringExpressionBase):
    def __init__(self, first_string_expression : AST.StringExpressionBase, second_string_expression : AST.StringExpressionBase):
        self.first_string_expression = first_string_expression
        self.second_string_expression = second_string_expression
    def execute(self, variables) -> str:
        first_string = self.first_string_expression.execute(variables)
        second_string = self.second_string_expression.execute(variables)
        value = first_string + second_string

        if AST.debug_enabled:
            print('NodeType=%r, FirstString=%r, SecondString=%r, Value=%r' % (type(self).__name__, first_string, second_string, value))
        return value