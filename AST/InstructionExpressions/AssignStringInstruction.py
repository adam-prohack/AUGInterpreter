import AST

class AssignStringInstruction(AST.InstructionExpressionBase):
    def __init__(self, variable_name : str, expression : AST.StringExpressionBase):
        self.variable_name = variable_name
        self.expression = expression
    def run(self, variables):
        if self.variable_name in variables.keys() and variables[self.variable_name]['type'] != 'string':
            print('Variable with "%r" could not change type to number' % self.variable_name)
            exit()
        variables[self.variable_name] = { 'type': 'string', 'value': self.expression.execute(variables) }