import AST

class AssignNumberInstruction(AST.InstructionExpressionBase):
    def __init__(self, variable_name : str, expression : AST.NumberExpressionBase):
        self.variable_name = variable_name
        self.expression = expression
    def run(self, variables):
        if self.variable_name in variables.keys() and variables[self.variable_name]['type'] != 'number':
            print('Variable with "%r" could not change type to string' % self.variable_name)
            exit()

        variables[self.variable_name] = { 'type': 'number', 'value': self.expression.execute(variables) }