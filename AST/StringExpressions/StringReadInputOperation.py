import AST

class StringReadInputOperation(AST.StringExpressionBase):
    def __init__(self):
        pass
    def execute(self, variables) -> str:
        value = str(input("Enter str value: "))
        
        if AST.debug_enabled:
            print('NodeType=%r, Value=%r' % (type(self).__name__, value))
        return value
