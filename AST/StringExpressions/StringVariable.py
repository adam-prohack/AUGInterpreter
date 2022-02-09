import AST

class StringVariable(AST.StringExpressionBase):
    def __init__(self, variable_name : str):
        self.variable_name = variable_name
    def execute(self, variables) -> str:
        value = variables[self.variable_name]["value"]

        if AST.debug_enabled:
            print('NodeType=%r, VariableName=%r, Value=%r' % (type(self).__name__, self.variable_name, value))
        return value
