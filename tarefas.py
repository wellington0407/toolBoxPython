import os

lista_fazer = []
lista_desfazer = []

os.system('clear')

while True:
    
    def comandar():
        print('\nComandos: listar, desfazer, refazer')
        comando = input('Digite uma tarefa ou comando: ')
        return comando
        print('\n')

    def escolher(comando):
        if comando == 'listar':
            return lista
        elif comando == 'desfazer':
            return desfaz
        elif comando == 'refazer':
            return refaz
        elif comando == 'limpar':
            return limpeza
        else:
            return inclui

    def lista(comando):
        print('\nTAREFAS: ')
        for itens in lista_fazer:
            print(f'{itens}')

    def desfaz(comando):
        lista_desfazer.append(lista_fazer.pop())
        lista(comando)

    def refaz(comando):
        lista_fazer.append(lista_desfazer.pop())
        lista(comando)

    def inclui(comando):
        lista_fazer.append(comando)
        lista(comando)

    def limpeza(comando):
        os.system('cls')

    comando = comandar()
    result = escolher(comando)
    result(comando)