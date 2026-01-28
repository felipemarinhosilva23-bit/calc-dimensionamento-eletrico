from cabos import dimensionar_cabo
from disjuntores import sugerir_disjuntor
from curvas import curvas_por_uso
from alimentacao import calcular_potencia
from relatorio import gerar_relatorio

corrente = float(input("Corrente do circuito (A): "))
tensao = int(input("Tensão (127, 220 ou 380 V): "))

print("Tipo de alimentação:")
print("1 - Monofásico")
print("2 - Bifásico")
print("3 - Trifásico")

tipo_alimentacao = {
    "1": "mono",
    "2": "bi",
    "3": "tri"
}[input("Escolha: ")]

print("Tipo de carga:")
print("1 - Iluminação")
print("2 - Tomadas")
print("3 - Motor")

tipo_uso = {
    "1": "iluminacao",
    "2": "tomadas",
    "3": "motor"
}[input("Escolha: ")]

resultado = dimensionar_cabo(corrente)

if resultado:
    potencia = calcular_potencia(corrente, tensao, tipo_alimentacao)
    disjuntor = sugerir_disjuntor(corrente, resultado["corrente_max"])
    curva = curvas_por_uso[tipo_uso]

    print("\n RESULTADO FINAL")
    print(f"Cabo: {resultado['secao']} mm²")
    print(f"Potência: {potencia:.0f} W")
    if isinstance(disjuntor, int):
     print(f"Disjuntor: {disjuntor} A")
     disjuntor_relatorio = f"{disjuntor} A"
    else:
     print(f"Disjuntor: {disjuntor}")
     disjuntor_relatorio = disjuntor

    print(f"Curva do disjuntor: {curva}")
    print(f"Alimentação: {tipo_alimentacao.upper()}")

    dados_relatorio = {
    "Corrente (A)": corrente,
    "Tensão (V)": tensao,
    "Tipo de alimentação": tipo_alimentacao.upper(),
    "Cabo (mm²)": resultado["secao"],
    "Disjuntor": disjuntor_relatorio,
    "Curva do disjuntor": curva,
    "Potência calculada (W)": f"{potencia:.0f}"
    }

    gerar_relatorio(dados_relatorio)
    print("\n Relatório PDF gerado com sucesso!")

else:
    print("Não foi possível dimensionar o circuito.")

