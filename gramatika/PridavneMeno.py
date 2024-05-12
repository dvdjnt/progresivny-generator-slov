from gramatika.Slovo import Slovo
from gramatika.VzorInterface import VzorInterface
from gramatika.CisloInterface import CisloInterface

class PridavneMeno(Slovo,VzorInterface, CisloInterface):
    def __init__(self,content,vzor,special=None, sklonovanie_array=None):
        super().__init__(content)
        VzorInterface.__init__(self)
        CisloInterface.__init__(self)

        self._vzor = vzor
        self._vzor_dictionary = {
            'pekny':self.pekny,
            'cudzi':self.cudzi,
            'otcov':self.otcov,
            'nesklonne':self.nesklonne

            # https://www.leitus.sk/pridavne-mena/
        }
    
    def getVzor(self):
        return self._vzor

    def transform(self, rod, cislo, pad):
        slovo = self.getContent()

        method = self.getVzorMethod(self.getVzor())
        return method(rod, cislo, pad)
            
    def getVzorMethod(self, vzor):
        return self._vzor_dictionary.get(vzor)
    
    def pekny(self, rod, cislo, pad):
        # TODO nezivotne    
        sklonovanie_arr_m = ['y','eho','emu','eho','om','ym',
                            'i','ych','ych','ych','ych','ymi']
        
        sklonovanie_arr_z = ['a','ej','ej','u','ej','ou',
                            'e','ych','ym','e','ych','ymi']
        
        sklonovanie_arr_s = ['e','eho','emu','e','om','ym',
                            'e','ych','ym','e','ych','ymi']
        
        rod_array_dict = {
            'm':sklonovanie_arr_m,
            'z':sklonovanie_arr_z,
            's':sklonovanie_arr_s
        }

        arr = rod_array_dict.get(rod)
        return self.getContent()[:-1]+arr[self.getCisloCode(cislo)+self.getPadCode(pad)]
    
    def cudzi(self, rod, cislo, pad):
        # TODO nezivotne
        sklonovanie_arr_m = ['i','ieho','iemu','ieho','om','im',
                            'i','ich','im','ich','ich','imi']
        
        sklonovanie_arr_z = ['ia','ej','ej','iu','ej','ou',
                            'ie','ich','im','ie','ich','imi']
        
        sklonovanie_arr_s = ['ie','ieho','iemu','ie','om','im',
                            'ie','ich','im','ie','ich','imi']
        
        rod_array_dict = {
            'm':sklonovanie_arr_m,
            'z':sklonovanie_arr_z,
            's':sklonovanie_arr_s
        }

        arr = rod_array_dict.get(rod)
        return self.getContent()[:-1]+arr[self.getCisloCode(cislo)+self.getPadCode(pad)]
    
    def otcov(self, rod, cislo, pad):
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

        arr = rod_array_dict.get(rod)
        return self.getContent()+arr[self.getCisloCode(cislo)+self.getPadCode(pad)]


    def nesklonne(self, rod, cislo, pad):
        return self.getContent()
