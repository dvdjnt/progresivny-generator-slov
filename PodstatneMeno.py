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
    
    # def changeCislo(self, cislo):

        
    # def transform(self, cislo, pad)

    def chlap(self, cislo, pad):

        string = self.getContent()
        char = ''

        if cislo == 'sg':
            if pad == 'N':
                char = ''
            if pad == 'G':
                char = 'a'
            if pad == 'D':
                char = 'ovi'
            if pad == 'A':
                char = 'a'
            if pad == 'L':
                char = 'ovi'
            if pad == 'I':
                char = 'om'
        elif cislo == 'pl':
            if pad == 'N':
                char = 'i'
            if pad == 'G':
                char = 'ov'
            if pad == 'D':
                char = 'om'
            if pad == 'A':
                char = 'ov'
            if pad == 'L':
                char = 'och'
            if pad == 'I':
                char = 'mi'

        return string+char
    
    def hrdina(self, cislo, pad):

        string = self.getContent()[:-1]
        char = ''

        if cislo == 'sg':
            if pad == 'N':
                char = ''
            if pad == 'G':
                char = 'u'
            if pad == 'D':
                char = 'ovi'
            if pad == 'A':
                char = 'u'
            if pad == 'L':
                char = 'ovi'
            if pad == 'I':
                char = 'om'
        elif cislo == 'pl':
            if pad == 'N':
                char = 'ovia'
            if pad == 'G':
                char = 'ov'
            if pad == 'D':
                char = 'om'
            if pad == 'A':
                char = 'ov'
            if pad == 'L':
                char = 'och'
            if pad == 'I':
                char = 'ami'

        return string+char

    def dub(self, cislo, pad):

        string = self.getContent()
        char = ''

        if cislo == 'sg':
            if pad == 'N':
                char = ''
            if pad == 'G':
                char = 'a'
            if pad == 'D':
                char = 'u'
            if pad == 'A':
                char = ''
            if pad == 'L':
                char = 'e'
            if pad == 'I':
                char = 'om'
        elif cislo == 'pl':
            if pad == 'N':
                char = 'y'
            if pad == 'G':
                char = 'ov'
            if pad == 'D':
                char = 'om'
            if pad == 'A':
                char = 'y'
            if pad == 'L':
                char = 'och'
            if pad == 'I':
                char = 'mi'

        return string+char
    
    def stroj(self, cislo, pad):

        string = self.getContent()
        char = ''

        if cislo == 'sg':
            if pad == 'N':
                char = ''
            if pad == 'G':
                char = 'a'
            if pad == 'D':
                char = 'u'
            if pad == 'A':
                char = ''
            if pad == 'L':
                char = 'i'
            if pad == 'I':
                char = 'om'
        elif cislo == 'pl':
            if pad == 'N':
                char = 'e'
            if pad == 'G':
                char = 'ov'
            if pad == 'D':
                char = 'om'
            if pad == 'A':
                char = 'e'
            if pad == 'L':
                char = 'och'
            if pad == 'I':
                char = 'mi'

        return string+char

    # so inefficient!!






