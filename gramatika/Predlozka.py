from gramatika.Slovo import Slovo

class Predlozka(Slovo):
    def __init__(self, content, vzor):
        super().__init__(content)
        self._vzor = vzor

    def getVzor(self):
        return self._vzor

