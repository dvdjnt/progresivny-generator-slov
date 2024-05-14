# from gramatika.Slovo import Slovo

class Sloveso():
    def __init__(self,content_m,content_p,content_b,content_n,typ,pad):
        # super().__init__(content)
        self._content_m=content_m
        self._content_p=content_p
        self._content_b=content_b
        self._content_n=content_n
        self._typ=typ
        self._pad=pad
        self._cas_dict = {
            'minuly':self.minuly,
            'pritomny':self.pritomny,
            'buduci':self.buduci,
            'neurcity':self.neurcity
        }
        self._cas_next = 'pritomny'
        self._rod_next = 'm'
        self._cislo_next = 'sg'

    def transform(self):
        method = self.getCasMethod(self._cas_next)
        return method(self._rod_next, self._cislo_next)

    def transformPrepare(self, cas, rod, cislo):
        self._cas_next = cas
        self._rod_next = rod
        self._cislo_next = cislo

    def transformRaw(self, cas, rod, cislo):
        # sklonovanie_arr = ['l',]
        method = self.getCasMethod(cas)
        return method(rod, cislo)

    def getCasMethod(self,cas):
        return self._cas_dict.get(cas)
    
    def getPad(self):
        return self._pad

    def getContent(self):
        return self._content_p
    
    def getTyp(self):
        # modal
        # plne
        # neplne
        return self._typ
    
    def fill_sklonovanie_array(self, array):
        self._sklonovanie_array = array
    
    def minuly(self, rod, cislo):
        # input vzdy v muzskom v minulom
        sklonovanie_arr = ['','a','o',
                           'i']
    
        index = 0
        slovo = self._content_m

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
        slovo = self._content_p[:-1]
        
        if cislo == 'sg':
            return self._content_p
        
        lastLetter = slovo[-1:]
        lastTwoLetters = slovo[-2:]

        if cislo == 'pl':
            if lastTwoLetters == 'ie':
                string = slovo
            elif lastLetter == 'a':
                string = slovo + 'ju'
            elif lastLetter == 'e':
                string = slovo + 'u'
            elif lastLetter == 'i':
                string = slovo + 'a'

        return string
    
    def buduci(self, rod, cislo):
        string = ''
        slovo = self._content_b

        lastLetter = slovo[-1:]

        if lastLetter != 't':
            return slovo

        if cislo == 'sg':
            string = 'bude '+ slovo
        elif cislo == 'pl':
            string = 'budu '+ slovo

        return string
    
    def neurcity(self, rod, cislo):
        return self._content_n