import AST

class UntilExpression(AST.InstructionExpressionBase):
    def __init__(self, condition : AST.BooleanExpressionBase, instruction : AST.InstructionExpressionBase):
        self.condition = condition
        self.instruction = instruction
    def run(self, variables):
        if self.condition.execute(variables):
            self.instruction.run(variables)
            while self.condition.execute(variables):
                self.instruction.run(variables)