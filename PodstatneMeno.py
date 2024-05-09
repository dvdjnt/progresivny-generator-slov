from Slovo import Slovo

class PodstatneMeno(Slovo):
    def __init__(self,content,rod,vzor,special=None, sklonovanie_array=None):
        super().__init__(self,content)
        self._rod = rod
        self._vzor = vzor

    def getRod(self):
        return self._rod
    
    def getVzor(self):
        return self._vzor
    
    # def changeRod
    # def changeCislo
    # def vysklonuj
