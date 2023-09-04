from Pessoas import *


class ListaPessoas(Pessoas): 
    def __init__(self, pessoas: dict[Pessoas]): 
        self.pessoas = pessoas 