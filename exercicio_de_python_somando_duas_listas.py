"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_c = []
contador = 0

contador = len(lista_a) if len(lista_a) < len(lista_b) else len(lista_b)

for i in range(contador):

    lista_c.append(lista_a[i] + lista_b[i])

print(lista_c)

lista_c = [x + y for x, y in zip(lista_a, lista_b)]

print(lista_c)