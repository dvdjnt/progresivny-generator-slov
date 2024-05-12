class VzorInterface:
    def __init__(self):
        _pady = ['N','G','D','A','L','I']
        self._pad_to_int = {pad: idx for idx, pad in enumerate(_pady)}
        # 1 ~ 6

    def getPadCode(self,pad):
        return self._pad_to_int.get(pad)