import random
import csv
# from gramatika.PodstatneMeno import PodstatneMeno
# from gramatika.PridavneMeno import PridavneMeno
# from gramatika.Sloveso import Sloveso
# from gramatika import * 
from gramatika.PodstatneMeno import PodstatneMeno
from gramatika.PridavneMeno import PridavneMeno
from gramatika.Sloveso import Sloveso

class GeneratorViet:
    def __init__(self):
        self._sd_enum = [ 
            'null',
            'podstatne',    # 1
            'pridavne',     # 2
            'zameno',       # 3
            'sloveso',      # 4
            'cislovka',     # 5
            'prislovka',
            'predlozka',
            'spojka',
            'castica',
            'citoslovcia']
        
        self._sd_methods = {
            'podstatne':PodstatneMeno,
            'pridavne':PridavneMeno,
            'zameno':3,
            'sloveso':Sloveso,
            'cislovka':5,
            'prislovka':6,
            'predlozka':7,
            'spojka':8,
            'castica':9,
            'citoslovcia':10
        }

        self.loadDB()
        
        self._sd_arrays = {
            'podstatne':self._podstatne,
            'pridavne':self._pridavne,
            'zameno':3,
            'sloveso':self._slovesa,
            'sloveso_modal':self._slovesa_modal,
            'cislovka':5,
            'prislovka':6,
            'predlozka':7,
            'spojka':8,
            'castica':9,
            'citoslovcia':10
        }

        self._template_arr = [141, 21421, 2141] # word blocks based on _sd_enum
        
    def getSentenceTemplate(self):
        random_index = random.randint(0,len(self._template_arr)-1)
        return self._template_arr[random_index]
    
    def loadDB(self):
        
        words = []
        self._podstatne = []
        self._pridavne = []
        self._slovesa = []
        self._slovesa_modal = []

        i = 1
        enum_counter = 0 # used for correct class creation according to _sd_enum

        with open ('db.csv', mode ='r', encoding='utf-8') as file:
            csvFile = csv.reader(file)

            for line in csvFile:
                    if line:  # Ensure the row isn't empty

                        first_line_char = line[0][0]

                        if first_line_char == '#':
                            enum_counter+=1  # skips line
                            continue
                        if first_line_char == '\n':
                            continue

                        # access string from array through index 
                        sd_string = self._sd_enum[enum_counter]

                        # access method (slovny druh constructor) through dictionary
                        method = self._sd_methods.get(sd_string)

                        # call method - create new object 
                        if (sd_string == 'podstatne'):
                            obj = method(content=line[0], rod=line[1], vzor=line[2])
                            self._podstatne.append(obj)
                        
                        if (sd_string == 'pridavne'):
                            obj = method(content=line[0], vzor=line[1])
                            self._pridavne.append(obj)

                        if (sd_string == 'sloveso'):
                            obj = method(content_m=line[0],content_p=line[1],content_b=line[2],content_n=line[3], 
                                         typ=line[4],pad=line[5])
                            
                            if obj.getTyp() == 'plne':
                                self._slovesa.append(obj)
                            elif obj.getTyp() == 'modal':
                                self._slovesa_modal.append(obj)

                        # words.append(obj)

                        if i == 100:
                            break
                        i+=1

    def generateSentence(self, sentence_amount):


        template = str(self.getSentenceTemplate())
        print(f'sentence template: {template}')
        print(f'sentence amount: {sentence_amount}\n')
        sentence = ''
        # TODO add template


        for i in range(0, sentence_amount):
            podmet = self.getPodmet()
            prisudok = self.getPlnovyznamnovyPrisudok()

            podmetBlock = self.generatePodmetBlock(podmet)
            prisudokBlock = self.generatePrisudokBlock(prisudok, podmet)
            predmetBlock = self.generatePredmetBlock(prisudok.getPad())
            sentence = sentence + podmetBlock + prisudokBlock + predmetBlock + '...'

        return sentence

    def getRandomWord(self, data):
        wordtype = data

        if isinstance(data, int):
            wordtype = self._sd_enum[data] 
        elif not isinstance(data, str):
            raise ValueError("Unsupported data type")
        
        array = self._sd_arrays.get(wordtype)   # get array of words by type
        random_index = random.randint(0,len(array)-1)
        return array[random_index]
    
    def generatePodmetBlock(self, podmet):
        privlastky_amount = random.randint(0,3)

        privlastky = self.getWords(privlastky_amount, 'pridavne', podmet.getRod(), 'sg', 'N')

        return privlastky + podmet.getContent() + ' '

    def generatePrisudokBlock(self, sloveso, podmet):
        block = ''

        prisudky_amount = 1
        if self.chance(0.3):
            prisudky_amount+= 1

        # TODO random cas
        # TODO dont repeat words

        cas = 'pritomny'
        rod = podmet.getRod()
        cislo = 'sg'

        for i in range(0, prisudky_amount):

            cas = 'pritomny'

            # modal chance
            if self.chance(0.7):
                prisudok = self.getModalBlock(cas, rod, cislo, sloveso)
                prisudok = self.negativeChance(prisudok)
                cas = 'neurcity'
                block = block + prisudok

            sloveso_trans = sloveso.transform(cas, rod, cislo)
            sloveso_trans = self.negativeChance(sloveso_trans)
            block = block + sloveso_trans + ' '

            if prisudky_amount > 1  and i == 0 and self.chance(0.7): # chance for spojka with multiple words
                char = ''
                if self.chance(0.7):
                    char = 'a '
                else:
                    char = 'ale '
            
                block = block + char

                # block = block.replace(' ',' a ',1)
                # TODO viacero slov, vyriesit a, ked sloveso ma medzery, pridat 's'

        return block
    
    def getModalBlock(self, cas, rod, cislo, sloveso):
        return self.getRandomWord('sloveso_modal').transform(cas, rod, cislo) + ' ' #+ sloveso.transform('neurcity',rod,cislo) + ' '

    def negativeChance(self, string):
        if self.chance(0.2):
            string = 'ne'+string
        return string

    def generatePredmetBlock(self, predmet_pad):
        block = ''

        predmet = self.getRandomWord('podstatne')
        predmet_trans = predmet.transform('sg',predmet_pad)
        
        privlastky_amount = random.randint(0,3)

        privlastky = self.getWords(privlastky_amount, 'pridavne', predmet.getRod(), 'sg', predmet_pad) 

        return block + privlastky + predmet_trans + ' '

    def getPodmet(self):
        return self.getRandomWord('podstatne')
    
    def getPlnovyznamnovyPrisudok(self):
        randomSloveso = self.getRandomWord('sloveso')
        # print(randomSloveso.getTyp())

        while randomSloveso.getTyp == 'plne':
            # print(randomSloveso.getTyp())
            randomSloveso = self.getRandomWord('sloveso')

        return randomSloveso

    def getWords(self, word_amount, wordtype, rod, cislo, pad):
        if isinstance(wordtype, int):
            wordtype = self._sd_enum[wordtype] 
        elif not isinstance(wordtype, str):
            raise ValueError("Unsupported data type")
    
        block = ''

        for i in range(0, word_amount):
            privlastok = self.getRandomWord(wordtype)

            # if block contains.....

            privlastok_trans = privlastok.transform(rod, cislo, pad)
            block = block + privlastok_trans + ' '

        return block

    def chance(self, threshold):
        return random.random() < threshold