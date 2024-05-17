from gramatika.Slovo import Slovo

class Spojka(Slovo):
    def __init__(self, content, pad):
        super().__init__(content)
        self._pad = pad

    def getPad(self):
        return self._pad

    def transform(self):
        return self.getContent()
