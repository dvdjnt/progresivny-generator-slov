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
                            obj = method(content=line[0])
                            self._slovesa.append(obj)

                        # words.append(obj)

                        if i == 100:
                            break
                        i+=1

        # print(len(podstatne))
        # print(len(pridavne))
        # print(len(slovesa))

        # for word in words:
        #     print(word.getContent())
        #     print(word.getRod())
        #     print(word.getVzor())
        #     print()

    def generateSentence(self):
        template = str(self.getSentenceTemplate())
        print(f'sentence template: {template}\n')
        sentence = ''

        for i in range(0, len(template)):
            index = int(template[i])
            word = self.getWord(index)
            sentence = sentence + word + ' '

        return sentence

    def getWord(self, data):
        wordtype = data

        if isinstance(data, int):
            wordtype = self._sd_enum[data] 
        elif not isinstance(data, str):
            raise ValueError("Unsupported data type")
        
        array = self._sd_arrays.get(wordtype)   # get array of words by type
        random_index = random.randint(0,len(array)-1)
        return array[random_index].getContent()
    
    def generatePodmetBlock(self):
        block = ''

        # get random podmet word
        random_index = random.randint(0,len(self._podstatne)-1) 
        podmet = self._podstatne[random_index]
        podmet_rod = podmet.getRod()

        # random number of privlastky
        random_privlastky_number = random.randint(2,3) # TODO 0,3

        for i in range(0, random_privlastky_number):
            random_pridavne_index = random.randint(0,len(self._pridavne)-1) 
            privlastok = self._pridavne[random_pridavne_index]
            privlastok_transformed = privlastok.transform(podmet_rod, 'sg','N')
            block = block + privlastok_transformed + ' '

        block = block + podmet.getContent()
        return block