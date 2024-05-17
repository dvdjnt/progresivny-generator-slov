from gramatika.Slovo import Slovo

class Prislovka(Slovo):
    def __init__(self,content):
        super().__init__(content=content)

    def transform(self):
        return self.getContent()
