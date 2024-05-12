import numpy as np
import random
import csv
from GeneratorViet import GeneratorViet
from gramatika.PodstatneMeno import PodstatneMeno

gen = GeneratorViet()
# word = gen.getWord(1)

# print(gen.getWord(1))

word = PodstatneMeno('chlpacik','m','chlap')

# print(word.transform('pl','D'))
# print(gen.getWord('podstatne'))
# sen = gen.generateSentence()
# print(sen)
# print(gen.generatePrisudokBlock())
# print(len(words))
# print(f"Processing string: {data}")

# string = ''
# string = string + gen.generatePodmetBlock()
# string = string + gen.generatePrisudokBlock()
# string = string + gen.generatePodmetBlock()
# print(string)
print(gen.generateSentence())