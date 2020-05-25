class Conector:

    def __init__(self, owner, nume, activ = 0, vezi_output = 0):
        self.valoare_bit = None
        self.owner = owner
        self.nume = nume
        self.vezi_output = vezi_output
        self.vector_conectori = []
        self.activ = activ

    def conecteaza(self, inputs):
        if not isinstance(inputs, list):
            inputs = [inputs]
        for input in inputs:
            self.vector_conectori.append(input)

    def set(self, valoare_bit):
        if self.valoare_bit == valoare_bit:
            return
        self.valoare_bit = valoare_bit
        if self.activ:
            self.owner.evaluate()
        if self.vezi_output:
            print("Conector {0}-{1} setat la {2}".format(self.owner.nume,
                                                        self.nume,
                                                        self.valoare_bit))
        for con in self.vector_conectori:
            con.set(valoare_bit)
