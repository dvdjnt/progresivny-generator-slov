class Slovo:
    def __init__(self,content,rod,vzor,special=None, sklonovanie_array=None):
        self._content = content
        self._rod = rod
        self._vzor = vzor
        self._special = special

    def fill_sklonovanie_array(self, array):
        self._sklonovanie_array = array

    def getRod(self):
        return self._rod