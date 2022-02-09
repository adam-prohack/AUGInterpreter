import AST

class NumberReadInputOperation(AST.NumberExpressionBase):
    def __init__(self):
        pass
    def execute(self, variables) -> int:
        value = int(input("Enter int value: "))
        
        if AST.debug_enabled:
            print('NodeType=%r, Value=%r' % (type(self).__name__, value))
        return value
