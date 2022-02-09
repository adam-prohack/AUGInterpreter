import AST

class StringPositionFunction(AST.NumberExpressionBase):
    def __init__(self, string_expression : AST.StringExpressionBase, search_string_expression : AST.StringExpressionBase):
        self.string_expression = string_expression
        self.search_string_expression = search_string_expression
    def execute(self, variables) -> int:
        string = self.string_expression.execute(variables)
        search_string = self.search_string_expression.execute(variables)
        value = string.find(search_string)

        if AST.debug_enabled:
            print('NodeType=%r, String=%r, SearchString=%r, Value=%r' % (type(self).__name__, string, search_string, value))
        return value