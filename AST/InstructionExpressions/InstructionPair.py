import AST

class InstructionPair(AST.InstructionExpressionBase):
    def __init__(self, first_instruction : AST.InstructionExpressionBase, second_instruction : AST.InstructionExpressionBase):
        self.first_instruction = first_instruction
        self.second_instruction = second_instruction
    def run(self, variables):
        self.first_instruction.run(variables)
        self.second_instruction.run(variables)