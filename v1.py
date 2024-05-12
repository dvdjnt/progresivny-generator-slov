import numpy as np
import random
import csv

privlastok = ['opozicno-oportunisticke','mocenske','progresivny','bratislavsky','liberalny','oportunista','dalsi','farizejski']

podmet = ['simecka', 'soros','caputova','korcok','lipsic','progresivci','slnieckari','fasisti','72 pohlavi','propaganda',
          'liberalizmus','fasizmus','europska unia','brusel','caputovej nadvlada','satanisti','hniezdo',
          'bratislavska kaviaren','markiza','dennik n','aktuality','medialne hyeny','kapitalisti','centrum','potkan','oligarchovia',
          'matovic','heger','naď','poradcovia caputovej','zidojaster','elity','mimovladky','farizej','matovicova vlada','sulik','SASka','OLANO','PSko']

prisudok_slovesny = ['farizejsky','bezhlavo','fasisticky','bez problemov']

prisudok = ['rozkradli','kradnu','terorizovali','prizivuju','chcu pretlacit','oznacili za dezolata','opovrhuju clovekom menom',
            'chcu zmenit','sterilizuju', 'budu skodit','chcu zakazat','zavadza','znicili']

predmet = ['deti','potraty','lacnejsie potraviny','lacnejsie energie','dochodcov','spravne hodnoty','narodne hodnoty',
           'statnu kasu','statny rozpocet','slovensko','istoty', '13ty dochodok','pohlaviu','vlade','kulturu','vlastencov']

extra = ['podla','podla obrazu','ako','napriklad','ale aj','a']

extra_extra = ['mu ten rozok natlacim do krku','tak sa to robi do psej matere','chceme mier',
               'slovensko uz potrebuje pokoj','jelen jako do prdele strelen','prd do stromovky','z kolaca diera a z opice rit',
               'slovenska a ziadna ina']




# np.random.shuffle(words);
random.shuffle(podmet);
random.shuffle(privlastok);
random.shuffle(prisudok);
random.shuffle(predmet);
random.shuffle(extra);
random.shuffle(prisudok_slovesny)

sentence_count = 10
words_in_sentence_max = 12


final_string = ''
version = 1

if version == 2:
    for i in range(sentence_count):
        final_string = final_string + privlastok[random.randint(0, len(privlastok)-1)] + ' '
        final_string = final_string + podmet[random.randint(0, len(podmet)-1)] + ' '
        final_string = final_string + extra[random.randint(0, len(extra)-1)] + ' '
        final_string = final_string + privlastok[random.randint(0, len(privlastok)-1)] + ' '
        final_string = final_string + podmet[random.randint(0, len(podmet)-1)] + ' '
        final_string = final_string + prisudok_slovesny[random.randint(0, len(prisudok_slovesny)-1)] + ' '
        final_string = final_string + prisudok[random.randint(0, len(prisudok)-1)] + ' '
        # final_string = final_string + privlastok[random.randint(0, len(privlastok)-1)] + ' '
        final_string = final_string + predmet[random.randint(0, len(predmet)-1)]

        final_string = final_string + '...\n'

# final_string = final_string + extra_extra[(random.randint(0, len(extra_extra)-1))]

if version == 1:
    words = privlastok + podmet + extra + privlastok + podmet + prisudok + prisudok_slovesny
    # words = list(itertools.chain(podmet,prisudok, predmet, privlastok, extra))
    for i in range(words_in_sentence_max*sentence_count):
        final_string = final_string + words[random.randint(0, len(words)-1)]
        final_string = final_string + ' '

# final_string = final_string.strip()

if version == 3:
    print(random.randint(0, len(privlastok)-1))
    print(random.randint(0, len(privlastok)-1))
    print(random.randint(0, len(privlastok)-1))
    print(random.randint(0, len(privlastok)-1))
    print(random.randint(0, len(privlastok)-1))
    print(random.randint(0, len(privlastok)-1))
    print(random.randint(0, len(podmet)-1))
    print(random.randint(0, len(podmet)-1))
    print(random.randint(0, len(podmet)-1))
    print(random.randint(0, len(extra)-1))
    print(random.randint(0, len(prisudok)-1))
    print(random.randint(0, len(prisudok_slovesny)-1))

if version == 4:
    words = privlastok + podmet + extra + prisudok + prisudok_slovesny
    # print(words)
    print('\n'.join(words))
    # print(' '.join(words))

print()
print(final_string)

