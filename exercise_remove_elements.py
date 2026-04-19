def remove_elements(lista):

    if len(lista) == 0:
        return lista

    elif len(lista) >= 6:
        del lista[0]
        del lista[3]
        del lista[3]

    elif len(lista) == 5:
        del lista[0]
        del lista[3]

    else:
        del lista[0]

    return lista


