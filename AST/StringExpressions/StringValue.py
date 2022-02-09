import AST

class StringValue(AST.StringExpressionBase):
    def __init__(self, value : str):
        self.value = value
    def execute(self, variables) -> str:
        if AST.debug_enabled:
            print('NodeType=%r, Value=%r' % (type(self).__name__, self.value))
        return self.value
