def get_element(lista, indice):

    if indice >= len(lista) or (int(indice) * -1 >= len(lista)):
        return None

    if len(lista) == 0:
        return None

    else:
        return lista[indice]



