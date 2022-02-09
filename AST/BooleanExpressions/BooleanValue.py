import AST

class BooleanValue(AST.BooleanExpressionBase):
    def __init__(self, value : bool):
        self.value = value
    def execute(self, variables) -> bool:
        if AST.debug_enabled:
            print('NodeType=%r, Value=%r' % (type(self).__name__, self.value))
        return self.value