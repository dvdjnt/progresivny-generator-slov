from gramatika.Slovo import Slovo
from gramatika.VzorInterface import VzorInterface
from gramatika.CisloInterface import CisloInterface

class PodstatneMeno(Slovo, VzorInterface,CisloInterface):
    def __init__(self,content,rod,vzor,special=None, sklonovanie_array=None):
        super().__init__(content)
        VzorInterface.__init__(self)
        CisloInterface.__init__(self)
        # add cislo 
        self._rod = rod
        self._vzor = vzor
        self._cislo = 'sg'  # TODO pomnozne
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
            'nesklonne':self.nesklonne,
            'otcov':self.otcov

            # https://www.leitus.sk/podstatne-mena/
        }
        self._cislo_next = self._cislo
        self._pad_next = ''

    def getRod(self):
        return self._rod
    
    def getVzor(self):
        return self._vzor

    def getCislo(self):
        return self._cislo

    def getVzorMethod(self,vzor):
        return self._vzor_dict.get(vzor)

    def getPadNext(self):
        return self._pad_next

    def getCisloNext(self):
        return self._cislo_next

    def transform(self):
        method = self.getVzorMethod(self.getVzor())
        return method(self._cislo_next, self._pad_next)

    def transformPrepare(self, cislo, pad):
        self._cislo_next = cislo
        self._pad_next = pad

    def transformRaw(self, cislo, pad):
        method = self.getVzorMethod(self.getVzor())
        return method(cislo, pad)





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
        lastLetter = self.getContent()[-1:]

        debug = False
        if debug:
            print(f"word: {self.getContent()}, last letter: {lastLetter}")

        sklonovanie_arr = [lastLetter, 'a','u','o','e','om',
        'a','i','am','a','ach','ami']
        
        # special case -> miest
        if pad == 'G' and cislo == 'pl':
            slovo = self.getContent()[:-1]
            char = sklonovanie_arr[self.getCisloCode(cislo)+self.getPadCode(pad)] 

            return self.insertLetterAtIndex(slovo, char, len(slovo)-3)
        # TODO index sa moze hybat (fasizmus, centrum)

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
        return self.getContent()

    def otcov(self, cislo, pad):
        # TODO nezivotne
        sklonovanie_arr_m = ['','ho','mu','ho','om','ym',
                            'i','ych','ym','ych','ych','ymi']
        
        sklonovanie_arr_z = ['a','ej','ej','u','ej','ou',
                            'e','ych','ym','e','ych','ymi']
        
        sklonovanie_arr_s = ['o','ho','mu','o','om','ym',
                            'e','ych','ym','e','ych','ymi']
        
        rod_array_dict = {
            'm':sklonovanie_arr_m,
            'z':sklonovanie_arr_z,
            's':sklonovanie_arr_s
        }

        arr = rod_array_dict.get(self.getRod())
        return self.getContent()+arr[self.getCisloCode(cislo)+self.getPadCode(pad)]
    
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
