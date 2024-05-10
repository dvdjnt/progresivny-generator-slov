from Slovo import Slovo
from Gramatika import VzorInterface, CisloInterface

class PodstatneMeno(Slovo,VzorInterface,CisloInterface):
    def __init__(self,content,rod,vzor,special=None, sklonovanie_array=None):
        super().__init__(content)
        VzorInterface.__init__(self)
        CisloInterface.__init__(self)

        self._rod = rod
        self._vzor = vzor
        self._vzor_dictionary = {
            'chlap':self.chlap,
            'hrdina':self.hrdina,
            'dub':self.dub,
            'stroj':self.stroj
        }

    def getRod(self):
        return self._rod
    
    def getVzor(self):
        return self._vzor
    
    # def changeCislo(self, cislo):

        
    def transform(self, cislo, pad):
        method = self.getVzorMethod(self.getVzor())
        return method(cislo, pad)

    def getVzorMethod(self,vzor):
        return self._vzor_dictionary.get(vzor)

    def chlap(self, cislo, pad):
        sklonovanie_arr = ['','a','ovi','a','ovi','om',
                       'i','ov','om','ov','och','mi']

        return self.getContent()+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]
    
    def hrdina(self, cislo, pad):
        sklonovanie_arr = ['','u','ovi','u','ovi','om',
                           'ovia','ov','om','ov','och','ami']
        # slovo = self.getContent()[:-1]
        # index1 = self.getCisloCode(cislo)
        # index2 = self.getPadCode(pad)
        # char = sklonovanie_arr[index1+index2]
        # result = slovo+char
        # return result



        return self.getContent()[:-1]+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]

    def dub(self, cislo, pad):
        sklonovanie_arr = ['','a','u','','e','om',
                           'y','ov','om','y','och','mi']
        
        return self.getContent()+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]
    
    def stroj(self, cislo, pad):
        sklonovanie_arr = ['','a','u','','i','om',
                           'e','ov','om','e','och','mi']
        
        return self.getContent()+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]






