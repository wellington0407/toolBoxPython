class Carros():
    def __init__(self, nome):
        self.nome = nome


class Motor():
    def __init__(self, nome):
        self.nome = nome


class Fabricante():
    def __init__(self, nome):
        self.nome = nome


carro1 = Carros('Uno')
carro2 = Carros('Clio')
carro3 = Carros('Duster')
motor1 = Motor('1.0')
motor2 = Motor('2.0')
fabricante1 = Fabricante('Fiat')
fabricante2 = Fabricante('Renault')


carro1 = motor1
carro1 = fabricante1
carro2 = motor1
carro2 = fabricante2
carro3 = motor2
carro3 = fabricante2


print(carro1.nome)


