class Pessoas:
    def __init__(
            self, 
            nome, 
            sobrenome, 
            idade, 
            sexo) -> None:
        
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        return f'Nome: {self.nome}, Idade: {self.idade}'        
    