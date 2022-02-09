import AST

class ExitInstruction(AST.InstructionExpressionBase):
    def __init__(self):
        pass
    def run(self, variables):
        exit()