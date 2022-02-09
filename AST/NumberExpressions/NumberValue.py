import AST

class NumberValue(AST.NumberExpressionBase):
    def __init__(self, value : int):
        self.value = value
    def execute(self, variables) -> int:
        if AST.debug_enabled:
            print('NodeType=%r, Value=%r' % (type(self).__name__, self.value))
        return self.value
