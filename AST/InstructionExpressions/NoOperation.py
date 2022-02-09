import AST

class NoOperation(AST.InstructionExpressionBase):
    def __init__(self):
        pass
    def run(self, variables):
        pass