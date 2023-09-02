import json


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

    def escrever_json(self, abertura):
        caminho_arquivo = './exercicio_json/pessoas.json'
        with open(caminho_arquivo, abertura, encoding='utf8') as arquivo:    
            json.dump(self.__dict__,
                arquivo, indent=2,                    
                ensure_ascii=False)
            
    