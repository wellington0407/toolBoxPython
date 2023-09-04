from formar_json import ler_json
from ListaPessoas import ListaPessoas
from Pessoas import *

if __name__ == '__main__':

    lista_pessoas = ler_json()

    print(lista_pessoas)

    decoded_team = ListaPessoas(lista_pessoas) 
    print(type(decoded_team))
    
    