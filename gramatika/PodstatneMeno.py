from gramatika.Slovo import Slovo
from gramatika.VzorInterface import VzorInterface
from gramatika.CisloInterface import CisloInterface

class PodstatneMeno(Slovo, VzorInterface,CisloInterface):
    def __init__(self,content,rod,vzor,special=None, sklonovanie_array=None):
        super().__init__(content)
        VzorInterface.__init__(self)
        CisloInterface.__init__(self)

        self._rod = rod
        self._vzor = vzor
        self._vzor_dict = {
            'chlap':self.chlap,
            'hrdina':self.hrdina,
            'dub':self.dub,
            'stroj':self.stroj,
            # kuli
            'zena':self.zena,
            'ulica':self.ulica,
            'dlan':self.dlan,
            'kost':self.kost,
            # gazdina
            # idea
            'mesto':self.mesto,
            'srdce':self.srdce,
            'vysvedcenie':self.vysvedcenie,
            'dievca':self.dievca,
            'nesklonne':self.nesklonne

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
        return self._vzor_dict.get(vzor)

    def chlap(self, cislo, pad):
        sklonovanie_arr = ['','a','ovi','a','ovi','om',
                       'i','ov','om','ov','och','mi']

        return self.getContent()+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]
    
    def hrdina(self, cislo, pad):
        sklonovanie_arr = ['','u','ovi','u','ovi','om',
                           'ovia','ov','om','ov','och','ami']
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
            slovo = self.getContent()[:-1]
            char = sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)] 

            return self.insertLetterAtIndex(slovo, char, len(slovo)-2)
            # TODO opravit hyen

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

    def mesto(self, cislo, pad):
        sklonovanie_arr = ['o','a','u','o','e','om',
        'a','i','am','a','ach','ami']
        
        # special case -> miest
        if pad == 'G' and cislo == 'pl':
            slovo = self.getContent()[:-1]
            char = sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)] 

            return self.insertLetterAtIndex(slovo, char, len(slovo)-3)
        # TODO index sa moze hybat

        return self.getContent()[:-1]+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]

    def srdce(self, cislo, pad):
        sklonovanie_arr = ['e','a','u','e','i','om',
                'ia','','iam','ia','iach','ami']
        
        return self.getContent()[:-1]+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]
    
    def vysvedcenie(self, cislo, pad):
        sklonovanie_arr = ['e','a','u','e','','m',
                'a','','am','a','ach','ami']
        
        return self.getContent()[:-1]+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]

    def dievca(self, cislo, pad):
        sklonovanie_arr = ['','ta','tu','','ti','tom',
                'a','t','tam','a','ach','ami']
        
        return self.getContent()+sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)]
    
    def nesklonne(self, cislo, pad):
        print("SERZANT, BOL SOM TRAFENY AAAARRRGGHHHH")
        return self.getContent()

    def switchIndex(self, string, indx1, indx2):
        char_list = list(string)
    
        # Swap the characters
        char_list[indx1], char_list[indx2] = char_list[indx2], char_list[indx1]
        
        # Convert list back to string
        return ''.join(char_list)

    def insertLetterAtIndex(self, string, letter, index):
        string = list(string)
        string.insert(index, letter)
        return ''.join(string)
