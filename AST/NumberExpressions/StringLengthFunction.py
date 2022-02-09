import AST

class StringLengthFunction(AST.NumberExpressionBase):
    def __init__(self, string_expression : AST.StringExpressionBase):
        self.string_expression = string_expression
    def execute(self, variables) -> int:
        string = self.string_expression.execute(variables)
        value = len(string)

        if AST.debug_enabled:
            print('NodeType=%r, String=%r, Value=%r' % (type(self).__name__, string, value))
        return value
