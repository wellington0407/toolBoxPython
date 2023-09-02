from Pessoas import *

if __name__ == '__main__':

    ana = Pessoas('Ana', 'Maria', 26, 'F')
    print(ana)

    pedro = Pessoas('Pedro', 'Soares', 31, 'M')
    print(pedro)

    bia = Pessoas('Bia', 'Silva', 22, 'F')
    print(bia)

    bia.escrever_json('w')
    pedro.escrever_json('a')
    ana.escrever_json('a')
