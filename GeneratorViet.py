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
                            obj = method(content_m=line[0],content_p=line[1],content_b=line[2],pad=line[3])
                            self._slovesa.append(obj)

                        # words.append(obj)

                        if i == 100:
                            break
                        i+=1


    def generateSentence(self):
        template = str(self.getSentenceTemplate())
        print(f'sentence template: {template}\n')
        sentence = ''

        podmet = self.generatePodmet()
        prisudok = self.generatePrisudok()

        podmetBlock = self.generatePodmetBlock(podmet)
        prisudokBlock = self.generatePrisudokBlock(prisudok, podmet)
        predmetBlock = self.generatePredmetBlock(prisudok.getPad())

        return podmetBlock + prisudokBlock + predmetBlock

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
        block = ''

        podmet_rod = podmet.getRod()

        # random number of privlastky
        random_privlastky_number = random.randint(0,3)

        for i in range(0, random_privlastky_number):
            privlastok = self.getRandomWord('pridavne')
            privlastok_trans = privlastok.transform(podmet_rod, 'sg','N')
            block = block + privlastok_trans + ' '

        block = block + podmet.getContent() + ' '
        return block
    
    def generatePrisudokBlock(self, sloveso, podmet):
        block = ''
        
        # sloveso_vzor = podmet.getVzor() # TODO add pad for next block

        random_number = random.randint(1,2) # number of words 

        for i in range(0, random_number):
            sloveso_trans = sloveso.transform('pritomny',podmet.getRod(), 'sg')
            block = block + sloveso_trans + ' '

            if random_number > 1 and self.chance(0.6) and i == 0: # 40% chance for spojka with multiple words
                block = block + 'a '
                # block = block.replace(' ',' a ',1)
                # TODO viacero slov, vyriesit a, ked sloveso ma medzery...

        return block

    def generatePredmetBlock(self, predmet_pad):
        block = ''

        predmet = self.getRandomWord('podstatne')
        print(predmet.getContent())
        print(predmet.getVzor())
        print(predmet_pad)

        # random number of privlastky
        random_privlastky_number = random.randint(0,3)

        for i in range(0, random_privlastky_number):
            privlastok = self.getRandomWord('pridavne')
            privlastok_trans = privlastok.transform(predmet.getRod(), 'sg',predmet_pad)
            block = block + privlastok_trans + ' '

        predmet_trans = predmet.transform('sg',predmet_pad)
        block = block + predmet_trans + ' '

        return block

    def generatePodmet(self):
        return self.getRandomWord('podstatne')
    
    def generatePrisudok(self):
        return self.getRandomWord('sloveso')

    def chance(self, threshold):
        return random.random() < threshold