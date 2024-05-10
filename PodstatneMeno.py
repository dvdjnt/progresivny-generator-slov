from Slovo import Slovo
from Gramatika import VzorInterface, CisloInterface
import array

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
            'stroj':self.stroj,
            # kuli
            'zena':self.zena,
            'ulica':self.ulica,
            'dlan':self.dlan,
            'kost':self.kost,
            # gadzina
            # idea
            # 'mesto':self.mesto,
            # 'srdce':self.srdce,
            # 'vysvedcenie':self.vysvedcenie,
            # 'dievca':self.dievca

            # https://www.leitus.sk/podstatne-mena/
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

    def zena(self, cislo,pad):




        sklonovanie_arr = ['a','y','e','u','e','ou',
                       'y','i','am','y','ach','ami']
        
        # special case -> zien
        if pad == 'G' and cislo == 'pl':
            slovo = list(self.getContent()[:-1])    # for using insert function
            char = sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)] 
            slovo.insert(len(slovo)-2, char)
            return ''.join(slovo)
            return self.switchIndex(slovo, len(slovo)-3, len(slovo)-2) 

        return self.getContent()[:-1]+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]

    def ulica(self, cislo, pad):
        sklonovanie_arr = ['a','e','i','u','i','ou',
                'e','','iam','e','iach','ami']
        
        return self.getContent()[:-1]+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]

    def dlan(self, cislo, pad):
        sklonovanie_arr = ['','e','i','','i','ou',
                'e','i','iam','e','iach','ami']
        
        return self.getContent()+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]
    
    def kost(self, cislo, pad):
        sklonovanie_arr = ['','i','i','','i','ou',
                'i','i','iam','i','iach','ami']
        
        return self.getContent()+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]

    def switchIndex(self, string, indx1, indx2):
        char_list = list(string)
    
        # Swap the characters
        char_list[indx1], char_list[indx2] = char_list[indx2], char_list[indx1]
        
        # Convert list back to string
        return ''.join(char_list)


