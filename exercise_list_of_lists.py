def list_of_lists(lista_de_listas):

    if len(lista_de_listas[0]) >= 3:
        del (lista_de_listas[0][2:])




    if len(lista_de_listas[1]) >= 4:
        lista_de_listas[1] = lista_de_listas[1][1:4]

    elif len(lista_de_listas[1]) <= 3 and len(lista_de_listas[2]) > 1:
        del (lista_de_listas[1][0])

    elif (lista_de_listas[2]) == []:
        lista_de_listas[1] = []


    if len(lista_de_listas[2]) >= 3:
        lista_de_listas[2] = lista_de_listas[2][-2:]


    return lista_de_listas

print(list_of_lists([[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]))





