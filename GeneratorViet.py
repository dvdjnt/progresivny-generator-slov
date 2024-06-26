import copy
import random
import csv
from gramatika.PodstatneMeno import PodstatneMeno
from gramatika.PridavneMeno import PridavneMeno
from gramatika.Spojka import Spojka
from gramatika.Sloveso import Sloveso
from gramatika.Prislovka import Prislovka

from collections import deque


class GeneratorViet:
    def __init__(self):
        self._podstatne_vlastne = []
        self._podstatne_zivotne = []
        self._podstatne_nezivotne = []
        self._pridavne = []
        self._slovesa = []
        self._slovesa_modal = []
        self._prislovky = []
        self._predlozky = []
        self._spojky = []

        self._debug = False

        if self._debug:
            self._neChance = 0.2
            self._modalChance = 0.3

            self._podmetyWeight = [0.1, 0.9]
            self._prisudkyWeight = [0.1, 0.9]
            self._predmetyWeight = [0.3, 0.5, 0.2]

            self._privlastkyWeight = [0.1, 0.1, 0.8]
            self._prislovkyWeight = [0.1, 0.9]
        else:
            self._neChance = 0.2
            self._modalChance = 0.3

            self._podmetyWeight = [0.5, 0.5]
            self._prisudkyWeight = [0.5, 0.5]
            self._predmetyWeight = [0.3, 0.5, 0.2]

            self._privlastkyWeight = [0.3, 0.5, 0.2]
            self._prislovkyWeight = [0.6, 0.4]
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
            'prislovka':Prislovka,
            'predlozka':7,
            'spojka':Spojka,
            'castica':9,
            'citoslovcia':10
        }

        self.loadDB()

        self._sd_arrays = {
            'podstatne_vlastne':self._podstatne_vlastne,
            'podstatne_zivotne':self._podstatne_zivotne,
            'podstatne_nezivotne':self._podstatne_nezivotne,
            'pridavne':self._pridavne,
            'zameno':3,
            'sloveso':self._slovesa,
            'sloveso_modal':self._slovesa_modal,
            'cislovka':5,
            'prislovka':self._prislovky,
            'predlozka':self._predlozky,
            'spojka':self._spojky,
            'castica':9,
            'citoslovcia':10
        }

        self._template_arr = [141, 21421, 2141] # word blocks based on _sd_enum



    def getSentenceTemplate(self):
        random_index = random.randint(0,len(self._template_arr)-1)
        return self._template_arr[random_index]

    def loadDB(self):

        words = []


        i = 1
        enum_counter = 0 # used for correct class creation according to _sd_enum

        # TODO do buducna - nenaplnat array, iba si vziat pointer na line na file - lepsia memory
        # TODO viacero padov pri slovesach

        if self._debug:
            file = 'db_test.csv'
        else:
            file = 'db.csv'

        with open (file, mode ='r', encoding='utf-8') as file:
            csvFile = csv.reader(file)

            for line in csvFile:
                    if line:  # Ensure the row isn't empty

                        first_line_char = line[0][0]

                        if first_line_char == '#':
                            enum_counter += 1  # skips line
                            continue
                        if first_line_char == '\n':
                            continue

                        # access string from array through index
                        sd_string = self._sd_enum[enum_counter]

                        # access method (slovny druh constructor) through dictionary
                        method = self._sd_methods.get(sd_string)

                        # call method - create new object
                        if sd_string == 'podstatne':

                            if len(line) > 3:
                                obj = method(content=line[0], rod=line[1], vzor=line[2], typ=line[3])

                                if obj.getTyp() == 'zivotne':
                                    self._podstatne_zivotne.append(obj)
                                elif obj.getTyp() == 'nezivotne':
                                    self._podstatne_nezivotne.append(obj)
                            else:
                                obj = method(content=line[0], rod=line[1], vzor=line[2], typ='vlastne')
                                self._podstatne_vlastne.append(obj)

                        elif sd_string == 'pridavne':
                            obj = method(content=line[0], vzor=line[1])
                            self._pridavne.append(obj)

                        elif sd_string == 'sloveso':
                            obj = method(content_m=line[0],content_p=line[1],content_b=line[2],content_n=line[3], typ=line[4],pad=line[5])

                            if obj.getTyp() == 'plne':
                                self._slovesa.append(obj)
                            elif obj.getTyp() == 'modal':
                                self._slovesa_modal.append(obj)

                        elif sd_string == 'spojka':
                            obj = method(content=line[0], pad=line[1])
                            self._spojky.append(obj)

                        elif sd_string == 'prislovka':
                            obj = method(content=line[0])
                            self._prislovky.append(obj)

                        # TODO optimize appending


    def generateSentences(self, sentence_amount):
        """
        Generates given amount of randomly generated sentences as string. Creates blocks within sentence and
        then compiles (sklonovanie) the sentences

        :param sentence_amount: amount of sentences to be given
        :return: paragraph with sentences as string
        """

        template = str(self.getSentenceTemplate())

        if self._debug:
            print(f'sentence template: {template}')
            print(f'sentence amount: {sentence_amount}\n')

        paragraph = ''
        # TODO add template
        # TODO s, ale, a (podmetBlock)
        # TODO add template blocks (podmetBlock = z templatu = 'poradcovia caputovej', 'europska unia)
        # TODO nepriamy privlastok


        for i in range(0, sentence_amount):
            # amount of words
            podmet_amount = random.choices([1, 2], weights=self._podmetyWeight, k=1)[0]
            prisudok_amount = random.choices([1, 2], weights=self._prisudkyWeight, k=1)[0]
            predmet_amount = random.choices([1, 2, 3], weights=self._predmetyWeight, k=1)[0]

            if self._debug:
                print(f"podmety: {podmet_amount}, prisudky: {prisudok_amount}, predmety: {predmet_amount}")


            podmety = self.getWords(podmet_amount, wordtype_arr=['podstatne_vlastne', 'podstatne_zivotne'])
            prisudky = self.getPlnovyznamovePrisudky(prisudok_amount)
            predmety = self.getWords(predmet_amount, wordtype_arr=['podstatne_vlastne', 'podstatne_zivotne'])


            podmetBlock = self.generatePBlock(podmety)
            podmetBlock = self.fillInSpojky(podmetBlock) # TODO sklonovanie 's'
            podmetBlock = self.fillInPrivlastky(podmetBlock, self._privlastkyWeight)

            prisudokBlock = self.generatePrisudokBlock(prisudky, podmety)
            prisudokBlock = self.fillInPrislovky(prisudokBlock, self._prislovkyWeight)

            predmetBlock = self.generatePBlock(predmety, prisudky)

            # TODO privlastky self.fillInPrivlastky()

            blocks = podmetBlock + prisudokBlock + predmetBlock # TODO based on given template

            blocks_dll = self.convertToLinkedList(blocks)
            blocks_dll = self.fillInSpojky(blocks_dll)
            blocks_arr = self.convertToArray(blocks_dll)

            sentence = self.compileSentence(blocks_arr)

            if self._debug:
                print(sentence + '\n')

            paragraph = paragraph + sentence + '.\n'

        print()
        return paragraph

    def compileSentence(self, blocks):

        sentence = ''

        for wordObj in blocks:
            if self._debug:
                if isinstance(wordObj, PodstatneMeno):
                    print(f"word: {wordObj.getContent()}, rod: {wordObj.getRod()}, cislo: {wordObj.getCislo()}, pad: {wordObj.getPadNext()}, vzor: {wordObj.getVzor()}")
                elif isinstance(wordObj, PridavneMeno):
                    print(f"word: {wordObj.getContent()}, rod: {wordObj.getRodNext()}, cislo: {wordObj.getCisloNext()}, pad: {wordObj.getPadNext()}, vzor: {wordObj.getVzor()}")
                elif isinstance(wordObj, Sloveso):
                    print(f"word: {wordObj.getContent()}, rod: {wordObj.getRodNext()}, cislo: {wordObj.getCisloNext()}, cas: {wordObj.getCasNext()}, pad: {wordObj.getPad()}")

            wordString = wordObj.transform()

            sentence = sentence + wordString + ' '

        return sentence[:-1] # without whitespace at the end

    def generatePBlock(self, podmety, prisudky=None):
        """
        Gerenerates privlastky before each podmet from podmety.
        Used for podmet and predmet generation.
        :param podmety: list of podmet objects to generate privlastky for
        :param prisudky: list of prisudky objects for predmet transformation
        :return: list of objects - (privlastky + podmety)*
        """

        # TODO nastavit podmety, rody....


        block = []

        if prisudky is not None:
            pad = prisudky[-1].getPad() # predmet
        else:
            pad = 'N'   # podmet

        # podmety
        podmety_amount = len(podmety)

        for j in range(0,podmety_amount):
            rod = podmety[j].getRod()
            cislo = 'sg'
            pad_final = pad
            podmety[j].transformPrepare(cislo, pad)
            # vzor = podmety[j].getVzor()
            #
            # privlastky_amount = random.choices([1, 2, 3], weights=[0.0, 0.0, 1.0], k=1)[0]
            #
            # # privlastky
            # privlastky = self.getPmena(privlastky_amount, 'pridavne')
            # # TODO sklonovanie dub - N
            # # TODO sklonovanie nesklonnych
            #
            # if vzor == 'nesklonne' or (pad_final == 'A' and (vzor == 'liberalizmus' or vzor == 'dub' or vzor == 'stroj')) :
            #     pad_final = 'N'
            #
            # for i in range(0, privlastky_amount):
            #     privlastky[i].transformPrepare(rod, cislo, pad_final)
            #     block.append(privlastky[i])

            block.append(podmety[j])

        return block

    def generatePrisudokBlock(self, prisudky, podmety):
        # TODO random cas
        # TODO add prislovky
        words = []

        prisudky_amount = len(prisudky)

        cas = 'pritomny'

        if len(podmety) == 1:
            rod = podmety[0].getRod()
            cislo = 'sg'
        else:
            rod = podmety[-1].getRod()
            cislo = 'pl'

        for i in range(0, prisudky_amount):
            cas = 'pritomny'

            # TODO sloveso-menny prisudok = prisudok + podstatne meno (bude zlodej, meni cloveka)
            # TODO add negativeChance

            # modal chance
            if self.chance(self._modalChance):
                modal_sloveso = self.getRandomWord('sloveso_modal') # TODO getWord lebo sa opakuju
                modal_sloveso.transformPrepare(cas, rod, cislo)
                # modal_sloveso = self.negativeChance(modal_sloveso)
                cas = 'neurcity'
                words.append(modal_sloveso)

            # sklonovanie plnovyznamoveho slovesa
            prisudky[i].transformPrepare(cas, rod, cislo)
            # prisudok_trans = self.negativeChance(prisudok_trans)

            words.append(prisudky[i])   # to avoid [[<Sloveso>]]

        return words

    def convertToLinkedList(self, arr):
        llist = deque()

        for element in arr:
            llist.append(element)

        return llist

    def convertToArray(self, list):
        arr = []
        for node in list:
            arr.append(node)

        return arr

    def fillInPrivlastky(self, words, weight):
        """
        Iterates over given words array, and generates a number of PridavneMeno objects
        for each PodstatneMeno. Generated objects are places in front of existing objects
        in the returned array.
        :param weight: chance vector for generating privlastky
        :param words: array of objects, ignores all but PodstatneMeno
        :return: array with added PridavneMeno objects placed in front of existing PodstatneMeno objects
        """

        return_arr = []

        for i in range(0, len(words)):
            if not isinstance(words[i], PodstatneMeno):
                return_arr.append(words[i])
                continue

            privlastky_block = []

            # get RCPV
            rod = words[i].getRod()
            cislo = 'sg'
            pad = words[i].getPadNext()
            vzor = words[i].getVzor()

            if vzor == 'nesklonne' or (
                    pad == 'A' and (vzor == 'liberalizmus' or vzor == 'dub' or vzor == 'stroj')):
                pad = 'N'

            # privlastky
            privlastky_amount = random.choices([1, 2, 3], weights=weight, k=1)[0] # non-zero
            privlastky = self.getWords(privlastky_amount, 'pridavne')

            for j in range(0, privlastky_amount):
                privlastky[j].transformPrepare(rod, cislo, pad)
                # privlastky_block.append(privlastky[j])
                return_arr.append(privlastky[j])

            return_arr.append(words[i])

        return return_arr

    def fillInPrislovky(self, words, weight):
        return_arr = []
        last_index = len(words)-1 # because for loop i-1 because looking for next element crash
        # print(words)

        i = 0
        for i in range(0, len(words)-1):
            if isinstance(words[i], Sloveso) and isinstance(words[i+1], Sloveso):
                prislovky_amount = random.choices([1, 2], weights=weight, k=1)[0]
                prislovky = self.getWords(prislovky_amount, 'prislovka')

                for j in range(0, prislovky_amount):
                    # prislovky[j].transformPrepare()
                    return_arr.append(prislovky[j])

            return_arr.append(words[i])

        return_arr.append(words[last_index])

        return return_arr

    def fillInSpojky(self, blocks_list):
        """
        Inserts a Spojka object between two PodstatneMeno objects
        or between PodstatneMeno and PridavneMeno objects in given list.

        :param blocks_list: linked list of objects
        :return:
        """
        indices = []

        for i in range(0, len(blocks_list) - 1):
            podm1 = isinstance(blocks_list[i], PodstatneMeno) and isinstance(blocks_list[i + 1], PodstatneMeno)
            podm2 = isinstance(blocks_list[i], PodstatneMeno) and isinstance(blocks_list[i + 1], PridavneMeno)
            if podm1 or podm2:
                indices.append(i)

        total = 0

        for index in indices:
            spojka = self.getRandomWord('spojka')
            blocks_list[index + 1 + total].transformPrepare(None, spojka.getPad())
            # blocks_list[index + 1 + total].
            blocks_list.insert(index + 1 + total, spojka)

            # indices shift because of inserting
            total += 1

        return blocks_list

    def getRandomWord(self, data):
        """

        :param data: string or string array representation of types of words to generate
        in case of array, randomly choose type
        :return: a single word object
        """
        if not isinstance(data, str) and not isinstance(data, list):
            raise ValueError("Unsupported data type in getRandomWord")

        if isinstance(data, str):
            wordtype = data
        else:
            wordtype = random.choice(data) # randomly choose one type

        array = self._sd_arrays.get(wordtype)  # get array of words of type
        random_index = random.randint(0, len(array) - 1)

        obj = array[random_index]

        obj_copy = copy.deepcopy(obj)

        return obj_copy

    def getWords(self, word_amount, wordtype_arr):
        """
        Returns amount of podstatne or pridavne mena from given wordtype array,
        array is not processed, but passed to getRandomWord function.
        Returned words are unique from each other (no duplicates).
        :param word_amount: amount of words to generate
        :param wordtype_arr of int, str
        :return array of words (Slovo object)
        """

        if not isinstance(wordtype_arr, (str, list)):
            raise ValueError("Unsupported data type in getRandomWord")

        words = []

        seen = set()  # Set to keep track of the contents we've already added

        while len(words) < word_amount:
            word = self.getRandomWord(wordtype_arr)
            content = word.getContent()
            if content not in seen:
                seen.add(content)
                words.append(word)

        return words    # list of words

    def getPlnovyznamovePrisudky(self, amount):
        # TODO optimize with getWords
        slovesa = []

        for i in range(0, amount):
            randomSloveso = self.getRandomWord('sloveso')

            while not randomSloveso.getTyp == 'plne' and randomSloveso in slovesa:
                randomSloveso = self.getRandomWord('sloveso')

            slovesa.append(randomSloveso)

        return slovesa  # list of words

    def negativeChance(self, string):
        if self.chance(self._neChance):
            string = 'ne'+string
        return string

    def chance(self, threshold):
        return random.random() < threshold

