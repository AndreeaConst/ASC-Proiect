import CircuitLogic, CONECTOR

class Not(CircuitLogic.CL):         # Input A. Output B.
    def __init__(self, nume):
        CircuitLogic.CL.__init__(self, nume)
        self.A = CONECTOR.Conector(self, 'A', activ = 1)
        self.B = CONECTOR.Conector(self, 'B')

    def evaluate(self):
        self.B.set(not self.A.valoare_bit)