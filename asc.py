
class Connector:
    # Connectors are inputs and outputs. Only outputs should connect
    # to inputs. Be careful NOT to have circular references
    # As an output is changed it propagates the change to its connected inputs
    #
    def __init__(self, owner, name, activates=0, monitor=0):
        self.value = None
        self.owner = owner
        self.name = name
        self.monitor = monitor
        self.connects = []
        self.activates = activates   # If true change kicks evaluate function

    def connect(self, inputs):
        if not isinstance(inputs, list):
            inputs = [inputs]
        for input in inputs:
            self.connects.append(input)

    def set(self, value):
        if self.value == value:
            return      # Ignore if no change
        self.value = value
        if self.activates:
            self.owner.evaluate()
        if self.monitor:
            print("Connector {0}-{1} set to {2}".format(self.owner.name,
                                                        self.name,
                                                        self.value))
        for con in self.connects:
            con.set(value)

class LC:
    # Logic Circuits have names and an evaluation function defined in child
    # classes. They will also contain a set of inputs and outputs.
    def __init__(self, name):
        self.name = name

    def evaluate(self):
        return


class Not(LC):         # Inverter. Input A. Output B.
    def __init__(self, name):
        LC.__init__(self, name)
        self.A = Connector(self, 'A', activates=1)
        self.B = Connector(self, 'B')

    def evaluate(self):
        self.B.set(not self.A.value)

class Gate3(LC):         # two input gates. Inputs A and B and C. Output D.
    def __init__(self, name):
        LC.__init__(self, name)
        self.A = Connector(self, 'A', activates=1)
        self.B = Connector(self, 'B', activates=1)
        self.C = Connector(self, 'C', activates=1)

        self.D = Connector(self, 'D')


class And(Gate3):       # two input AND Gate
    def __init__(self, name):
        Gate3.__init__(self, name)

    def evaluate(self):
        self.D.set(self.A.value and self.B.value and self.C.value)

def test3Bit(a):
    # a este vector care contine bitii din baza 2, in urma transformarii numarului citit de
    # la tastatura, din baza x in baza 2

    #poarta NOT are intrarea A si iesirea B
    #poarta AND  are intrarile A,B,C si iesirea D

    NOT1 = Not('NOT1')
    NOT1.B.monitor = 1

    NOT2 = Not('NOT2')
    NOT2.B.monitor = 1

    NOT3 = Not('NOT3')
    NOT3.B.monitor = 1

    AND1 = And('AND1')
    AND1.D.monitor = 1
    NOT1.B.connect(AND1.A)
    NOT2.B.connect(AND1.B)
    NOT3.B.connect(AND1.C)

    AND2 = And('AND2')
    AND2.D.monitor = 1
    NOT1.B.connect(AND2.A)
    NOT2.B.connect(AND2.B)
    AND2.C.set(a[2])

    AND3 = And('AND3')
    AND3.D.monitor = 1
    NOT1.B.connect(AND3.A)
    AND3.B.set(a[0])
    NOT3.B.connect(AND3.C)

    AND4 = And('AND4')
    AND4.D.monitor = 1
    NOT1.B.connect(AND4.A)
    AND4.B.set(a[1])
    AND4.B.set(a[2])

    AND5 = And('AND5')
    AND5.D.monitor = 1
    AND5.A.set(a[0])
    NOT2.B.connect(AND5.B)
    NOT3.B.connect(AND5.C)

    AND6 = And('AND6')
    AND6.D.monitor = 1
    AND6.A.set(a[0])
    NOT2.B.connect(AND6.B)
    AND6.C.set(a[2])

    AND7 = And('AND7')
    AND7.D.monitor = 1
    AND7.A.set(a[0])
    AND7.B.set(a[1])
    NOT3.B.connect(AND7.C)

    AND8 = And('AND8')
    AND8.D.monitor = 1
    AND8.A.set(a[0])
    AND8.B.set(a[1])
    AND8.C.set(a[2])

    NOT1.A.set(a[0])
    NOT2.A.set(a[1])
    NOT3.A.set(a[2])

    print(AND8.D.value)


def main():
    a = [0,0,0]
    a[0] = 1
    a[1] = 1
    a[2] = 1
    test3Bit(a)

main()