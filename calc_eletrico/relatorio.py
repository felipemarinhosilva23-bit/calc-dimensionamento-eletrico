from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


def gerar_relatorio(dados):
    nome_arquivo = "relatorio_dimensionamento.pdf"
    pdf = canvas.Canvas(nome_arquivo, pagesize=A4)

    largura, altura = A4
    y = altura - 40

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, y, "Relatório de Dimensionamento Elétrico")

    y -= 40
    pdf.setFont("Helvetica", 11)
    pdf.drawString(40, y, f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    y -= 30
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(40, y, "Dados do Circuito")

    y -= 20
    pdf.setFont("Helvetica", 11)

    for chave, valor in dados.items():
        pdf.drawString(40, y, f"{chave}: {valor}")
        y -= 18

        if y < 50:
            pdf.showPage()
            y = altura - 40

    y -= 20
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(
        40,
        y,
        "Observação: Relatório gerado automaticamente para fins educacionais."
    )

    pdf.save()
    return nome_arquivo