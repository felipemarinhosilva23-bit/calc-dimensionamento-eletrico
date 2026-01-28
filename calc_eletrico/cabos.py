from tabela_cabos import tabela_cabos

def dimensionar_cabo(corrente):
    for item in tabela_cabos:
        if corrente <= item["corrente_max"]:
            return item
    return None