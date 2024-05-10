import numpy as np
import random
import csv
from PridavneMeno import PridavneMeno
from PodstatneMeno import PodstatneMeno

words = []
i = 1

meno = PodstatneMeno('Rodina','m','hrdina')
meno.transform('sg','A')
print(meno)



# with open ('db.csv', mode ='r', encoding='utf-8') as file:
#   csvFile = csv.reader(file)

#   for line in csvFile:
#         if line:  # Ensure the row isn't empty

#             first_line_char = line[0][0]

#             if first_line_char == '#':
#                 continue
#             if first_line_char == '\n':
#                 continue

#             # (content), string, vzor, special
#             # print(line[0])
#             # print(line[1])
#             # print(line[2])

#             obj = PridavneMeno(content=line[0], vzor=line[1])

#             words.append(obj)

#             if i == 10:
#                 break
#             i+=1

# print(len(words))

