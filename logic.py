from circuit import Circuit, Wire

class NOT(Circuit):
    def __init__(self, wire = None, *a, **kw):
        self.a = Wire()
        if wire:
            wire.conecteaza(self.a)
        self.out = Wire()
        self.a.conecteaza(self)
        super().__init__(inputs = [], *a, **kw)

    def onchange(self):
        a = self.a.state
        self.out.drive(not a)

class AND(Circuit):
    def __init__(self, *a, **kw):
        self.a = Wire()
        self.b = Wire()
        self.out = Wire()
        super().__init__(inputs = [self.a, self.b], *a, **kw)

    def onchange(self):
        a = self.a.state
        b = self.b.state
        self.out.drive(a & b)