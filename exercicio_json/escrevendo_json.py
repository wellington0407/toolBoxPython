from formar_json import escrever_json, save_data
from Pessoas import *

if __name__ == '__main__':

    lista_pessoas = []

    ana = Pessoas('Ana', 'Maria', 26, 'F')
    print(ana)

    pedro = Pessoas('Pedro', 'Soares', 31, 'M')
    print(pedro)

    bia = Pessoas('Bia', 'Silva', 22, 'F')
    print(bia)

    lista_pessoas.append(save_data(ana))
    lista_pessoas.append(save_data(pedro))
    lista_pessoas.append(save_data(bia))

    escrever_json(lista_pessoas, 'w')

