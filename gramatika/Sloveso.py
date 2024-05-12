from gramatika.Slovo import Slovo

class Sloveso(Slovo):
    def __init__(self,content):
        super().__init__(content)
        self._cas_dict = {
            'minuly':self.minuly,
            'pritomny':self.pritomny,
            'buduci':self.buduci
        }

    def transform(self, cas, rod, cislo):
        # sklonovanie_arr = ['l',]
        method = self.getCasMethod(cas)
        return method(rod, cislo)

    def getCasMethod(self,cas):
        return self._vzor_dict.get(cas)
    
    def minuly(self, rod, cislo):
        sklonovanie_arr = ['l','la','lo',
                           'li']
    
        index = 0
        slovo = self.getContent()[:-1]

        if rod == 'm':
            index += 1
        elif rod == 'z':
            index += 2
        elif rod == 's':
            index += 3

        if cislo == 'pl':
            index += 1

        return slovo + sklonovanie_arr[index]

    def pritomny(self, rod, cislo):
        string = ''
        slovo = self.getContent()[:-1]
        
        if cislo == 'sg':
            string = slovo
        elif cislo == 'pl':
            string = slovo + 'a'

        return string
    
    def buduci(self, rod, cislo):
        string = ''
        slovo = self.getContent()
        
        if cislo == 'sg':
            string = 'bude '+ slovo
        elif cislo == 'pl':
            string = 'budu '+ slovo

        return string