from pypdf import PdfReader, PdfWriter


def dividir_pdf(arquivo_pdf, partes=3):
    leitor = PdfReader(arquivo_pdf)
    total_paginas = len(leitor.pages)
    print(f"Total de páginas: {total_paginas}")

    paginas_por_parte = total_paginas // partes
    resto = total_paginas % partes

    inicio = 0
    for i in range(partes):
        fim = inicio + paginas_por_parte
        if i == partes - 1:
            fim += resto

        escritor = PdfWriter()
        for num_pagina in range(inicio, fim):
            escritor.add_page(leitor.pages[num_pagina])

        nome_arquivo = f"parte_{i+1}.pdf"
        with open(nome_arquivo, "wb") as saida:
            escritor.write(saida)

        print(f"Gerado: {nome_arquivo} (páginas {inicio+1} até {fim})")
        inicio = fim


if __name__ == "__main__":
    dividir_pdf("seu-arquivo-grandão.pdf", partes=3)
