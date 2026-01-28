disjuntores_padrao = [6, 10, 16, 20, 25, 32, 40, 50, 63]


def sugerir_disjuntor(corrente_circuito, corrente_max_cabo):
    for dj in disjuntores_padrao:
        if dj >= corrente_circuito and dj <= corrente_max_cabo:
            return dj
    return "Nenhum disjuntor compatível com o cabo."
