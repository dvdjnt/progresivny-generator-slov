import random
import csv
from gramatika import *

class GeneratorViet:
    def __init__(self):
        self._slovne_druhy_enum = {
            'podstatne':1,
            'pridavne':2,
            'zameno':3,
            'sloveso':4,
            'cislovka':5,
            'prislovka':6,
            'predlozka':7,
            'spojka':8,
            'castica':9,
            'citoslovcia':10
        }
        self._slovne_druhy_methods = {
            'podstatne':1,
            'pridavne':2,
            'zameno':3,
            'sloveso':4,
            'cislovka':5,
            'prislovka':6,
            'predlozka':7,
            'spojka':8,
            'castica':9,
            'citoslovcia':10
        }

        self._template_arr = [141]

    def getSentenceTemplate(self):
        random_index = random.randint(0,len(self._template_arr))
        return self._template_arr[random_index]
    
    def loadDB(self):
        
        words = []
        i = 1
        counter = 0

        with open ('db.csv', mode ='r', encoding='utf-8') as file:
            csvFile = csv.reader(file)

            for line in csvFile:
                    if line:  # Ensure the row isn't empty

                        first_line_char = line[0][0]

                        if first_line_char == '#':
                            counter+=1
                            continue
                        if first_line_char == '\n':
                            continue

                        obj = PridavneMeno(content=line[0], vzor=line[1])

                        words.append(obj)

                        if i == 10:
                            break
                        i+=1

        print(len(words))

