import AST

class StringSubstringFunction(AST.StringExpressionBase):
    def __init__(self, string_expression : AST.StringExpressionBase, start_expression : AST.NumberExpressionBase, length_expression : AST.NumberExpressionBase):
        self.string_expression = string_expression
        self.start_expression = start_expression
        self.end_expression = length_expression
    def execute(self, variables) -> str:
        string = self.string_expression.execute(variables)
        start = self.start_expression.execute(variables)
        end = self.end_expression.execute(variables)
        value = string[start:end]

        if AST.debug_enabled:
            print('NodeType=%r, String=%r, Start=%r, Length=%r, Value=%r' % (type(self).__name__, string, start, end, value))
        return value