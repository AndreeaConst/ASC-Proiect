import CircuitLogic, CONECTOR

class Poarta4Biti(CircuitLogic.CL):         # Inputs A,B,C,D. Output E.
    def __init__(self, nume):
        CircuitLogic.CL.__init__(self, nume)
        self.A = CONECTOR.Conector(self, 'A', activ = 1)
        self.B = CONECTOR.Conector(self, 'B', activ = 1)
        self.C = CONECTOR.Conector(self, 'C', activ = 1)
        self.D = CONECTOR.Conector(self, 'D', activ = 1)

        self.E = CONECTOR.Conector(self, 'E')


class And(Poarta4Biti):       # two input AND Gate
    def __init__(self, nume):
        Poarta4Biti.__init__(self, nume)

    def evaluate(self):
        self.E.set(self.A.valoare_bit and self.B.valoare_bit and self.C.valoare_bit and self.D.valoare_bit)