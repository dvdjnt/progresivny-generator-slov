class CisloInterface:
    def __init__(self):
        self._cislo_to_int = {
            'sg':0,
            'pl':6
        }

    def getCisloCode(self, cislo):
        return self._cislo_to_int.get(cislo)