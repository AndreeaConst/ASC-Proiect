class Wire:
    def __init__(self, default=True):
        self.state=default
        self.observers = []

    def drive(self, state, force=False):
        if state != self.state or force:
            self.state=state
            for observer in self.observers:
                if isinstance(observer, Wire):
                    observer.drive(state,force=force)
                elif isinstance(observer, Circuit):
                    observer.onchange()
                else:
                    observer()
    def conecteaza(self, observer):
        self.observers.append(observer)
        self.drive(self.state, force=True)


class Circuit:
    def __init__ (self, inputs, **kw):

        for input_nume in kw:
            if hasattr(self,input_nume):
                input = getattr(self, input_nume)
                output = kw(input_nume)
                output.conecteaza(input)
        for i in inputs:
            i.conecteaza(self)
        def onchange(self):
            return  NotImplemented

class LED(Wire):
    def __init__(self,label,a,**kw):
        self.label=label
        super().__init__(a,**kw)

    def drive(self,state,force=False):
        if state != self.state or force:
            if state:
                print("LED \" {}\" switched ON",format(self.label))
            else:
                print("LED \"{}\" switch OFF",format(self.label))

            super().drive(state, force)