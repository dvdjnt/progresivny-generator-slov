class Gramatika_pridavne_meno:
    def __init__(self) -> None:
        pass
    
    def changeRod(slovo,rod):

        if rod == 'm':
            string = slovo[:-1] + 'y'
            return string
        
        elif rod == 'z':
            string = slovo[:-1] + 'a'
            return string
        
        elif rod == 's':
            string = slovo[:-1] + 'o'
            return string
            