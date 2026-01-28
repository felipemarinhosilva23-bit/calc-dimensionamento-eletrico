
import math

def calcular_potencia(corrente, tensao, tipo):
    if tipo == "mono":
        return tensao * corrente
    elif tipo == "bi":
        return tensao * corrente
    elif tipo == "tri":
        return math.sqrt(3) * tensao * corrente
    else:
        raise ValueError("Tipo de alimentação inválido.")