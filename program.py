import numpy as np
import random

privlastok = ['opozicno-oportunisticke','mocenske','progresivny','bratislavsky','liberalny','oportunista']

podmet = ['simecka', 'soros','caputova','korcok','lipsic','progresivci','slnieckari','deti hamburgerov','fasisti','72 pohlavi','propaganda',
          'liberalizmus','fasizmus','slovensko','europska unia','brusel','caputovej nadvlada','satanisti','hniezdo',
          'bratislavska kaviaren','markiza','dennik n','aktuality','medialne hyeny','kapitalisti','centrum','potkan',
          'istoty','13ty dochodok','oligarchovia','matovic','heger','naď','poradcovia caputovej','zidojaster','elity','chemtrails']

prisudok = ['rozkradli','kradnu','terorizovali','prizivuju','chcu pretlacit','oznacili za dezolata','opovrhuju clovekom menom',
            'chcu zmenit pohlavie','sterilizuju deti', 'budu skodit vlade','ini','dalsi','chcu zakazat']

predmet = ['deti','obcanov','potraty','lacnejsie potraviny','lacnejsie energie','dochodcov','spravne hodnoty','narodne hodnoty','statnu kasu','statny rozpocet']

extra = ['podla','podla obrazu','ako','napriklad','ale aj','a','pretoze']

extra_extra = ['mu ten rozok natlacim do krku','tak sa to robi do psej matere','chceme mier',
               'slovensko uz potrebuje pokoj','jelen jako do prdele strelen','prd do stromovky','z kolaca diera a z opice rit']


final_string = ''

# np.random.shuffle(words);
random.shuffle(podmet);
random.shuffle(privlastok);
random.shuffle(prisudok);
random.shuffle(predmet);
random.shuffle(extra);

sentence_count = 3
words_in_sentence_max = 12


for i in range(sentence_count):
    final_string = final_string + privlastok[random.randint(0, len(privlastok)-1)] + ' '
    final_string = final_string + podmet[random.randint(0, len(podmet)-1)] + ' '
    final_string = final_string + extra[random.randint(0, len(extra)-1)] + ' '
    final_string = final_string + podmet[random.randint(0, len(podmet)-1)] + ' '
    final_string = final_string + prisudok[random.randint(0, len(prisudok)-1)] + ' '
    # final_string = final_string + privlastok[random.randint(0, len(privlastok)-1)] + ' '
    final_string = final_string + predmet[random.randint(0, len(predmet)-1)]

    final_string = final_string + '...\n'

# final_string = final_string + extra_extra[(random.randint(0, len(extra_extra)-1))]

final_string = final_string.strip()

print()
print(final_string)
