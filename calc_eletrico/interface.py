import tkinter as tk
from tkinter import messagebox

from cabos import dimensionar_cabo
from disjuntores import sugerir_disjuntor
from curvas import curvas_por_uso
from alimentacao import calcular_potencia
from relatorio import gerar_relatorio


# ----- CORES -----
COR_FUNDO = "#0d1b2a"
COR_TEXTO = "#e0e1dd"
COR_DESTAQUE = "#fca311"
COR_CAIXA = "#1b263b"


def calcular():
    try:
        corrente = float(entry_corrente.get())
        tensao = int(entry_tensao.get())
        tipo_alimentacao = alimentacao_var.get()
        tipo_uso = uso_var.get()

        resultado = dimensionar_cabo(corrente)

        if not resultado:
            messagebox.showerror("Erro", "Não foi possível dimensionar o cabo.")
            return

        potencia = calcular_potencia(corrente, tensao, tipo_alimentacao)
        disjuntor = sugerir_disjuntor(corrente, resultado["corrente_max"])
        curva = curvas_por_uso[tipo_uso]

        if isinstance(disjuntor, int):
            disjuntor_txt = f"{disjuntor} A"
        else:
            disjuntor_txt = disjuntor

        dados = {
            "Corrente (A)": corrente,
            "Tensão (V)": tensao,
            "Tipo de alimentação": tipo_alimentacao.upper(),
            "Cabo (mm²)": resultado["secao"],
            "Disjuntor": disjuntor_txt,
            "Curva do disjuntor": curva,
            "Potência calculada (W)": f"{potencia:.0f}"
        }

        gerar_relatorio(dados)

        resultado_label.config(
            text=(
                f"Cabo: {resultado['secao']} mm²\n"
                f"Disjuntor: {disjuntor_txt}\n"
                f"Curva: {curva}\n"
                f"Potência: {potencia:.0f} W\n\n"
                "PDF gerado com sucesso!"
            )
        )

    except Exception as e:
        messagebox.showerror("Erro", str(e))


# ----- JANELA -----
janela = tk.Tk()
janela.title("Calculadora de Dimensionamento Elétrico")
janela.geometry("480x520")
janela.configure(bg=COR_FUNDO)

# ----- TÍTULO -----
tk.Label(
    janela,
    text="Dimensionamento Elétrico",
    bg=COR_FUNDO,
    fg=COR_DESTAQUE,
    font=("Segoe UI", 16, "bold")
).pack(pady=10)

# ----- FRAME DE ENTRADA -----
frame = tk.Frame(janela, bg=COR_CAIXA)
frame.pack(padx=20, pady=10, fill="x")

def label(texto):
    return tk.Label(frame, text=texto, bg=COR_CAIXA, fg=COR_TEXTO, anchor="w")

label("Corrente (A)").pack(fill="x", padx=10, pady=(10, 0))
entry_corrente = tk.Entry(frame)
entry_corrente.pack(fill="x", padx=10)

label("Tensão (127 / 220 / 380 V)").pack(fill="x", padx=10, pady=(10, 0))
entry_tensao = tk.Entry(frame)
entry_tensao.pack(fill="x", padx=10)

label("Tipo de alimentação").pack(fill="x", padx=10, pady=(10, 0))
alimentacao_var = tk.StringVar(value="mono")
tk.OptionMenu(frame, alimentacao_var, "mono", "bi", "tri").pack(fill="x", padx=10)

label("Tipo de carga").pack(fill="x", padx=10, pady=(10, 0))
uso_var = tk.StringVar(value="iluminacao")
tk.OptionMenu(frame, uso_var, "iluminacao", "tomadas", "motor").pack(fill="x", padx=10, pady=(0, 10))

# ----- BOTÃO -----
tk.Button(
    janela,
    text="Calcular e Gerar PDF",
    bg=COR_DESTAQUE,
    fg="black",
    font=("Segoe UI", 11, "bold"),
    command=calcular
).pack(pady=15)

# ----- RESULTADO -----
resultado_label = tk.Label(
    janela,
    text="",
    bg=COR_FUNDO,
    fg=COR_TEXTO,
    font=("Segoe UI", 10),
    justify="left"
)
resultado_label.pack(pady=10)

janela.mainloop()
