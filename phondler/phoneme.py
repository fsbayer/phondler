class Phoneme:
    def __init__(self, ptype: str):
        self.ptype = ptype


class Cons(Phoneme):
    def __init__(self, voice: int, ctype: str):
        super().__init__("Cons")
        self.voice = voice
        self.ctype = ctype


class PulmCons(Cons):
    def __init__(self, voice: int, pcmanner: int, pcplace: int):
        super().__init__(voice, "PulmCons")
        self.pcmanner = pcmanner
        self.pcplace = pcplace


class NonPulmCons(Cons):
    def __init__(self, voice: int, npctype: str):
        super().__init__(voice, "NonPulmCons")
        self.npctype = npctype


class Ejective(NonPulmCons):
    def __init__(self, voice: int, ejmanner: int, ejplace: int):
        super().__init__(voice, "Ejective")
        self.ejmanner = ejmanner
        self.ejplace = ejplace


class Click(NonPulmCons):
    def __init__(self, voice: int, clmanner: int, clplace: int):
        super().__init__(voice, "Click")
        self.clmanner = clmanner
        self.clplace = clplace


class Implosive(NonPulmCons):
    def __init__(self, voice: int, implace: int):
        super().__init__(voice, "Implosive")
        self.implace = implace


class Multi(Cons):
    def __init__(self, voice: int, catype: str):
        super().__init__(voice, "Multi")
        self.catype = catype
        self.sequence = []

    def append(self, cons: Cons):
        self.sequence.append(cons)