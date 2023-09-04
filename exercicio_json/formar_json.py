import json

from Pessoas import Pessoas

CAMINHO_ARQUIVO = './exercicio_json/pessoas.json'

def save_data(Pessoas):
    data = {}
    for attr in Pessoas.__dict__:
        data[attr] = Pessoas.__dict__[attr]
    return data

def escrever_json(lista, abertura):
        
        with open(CAMINHO_ARQUIVO, abertura, encoding='utf8') as arquivo:    
            json.dump(lista,
                arquivo, indent=2,                    
                ensure_ascii=False)
            
def ler_json():
    with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
                dados = json.load(arquivo) 
                return dados