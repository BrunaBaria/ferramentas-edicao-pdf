import fitz  # PyMuPDF

def juntar_pdfs(pdf1, pdf2, pdf_saida):
    # Abrir os PDFs
    doc1 = fitz.open(pdf1)
    doc2 = fitz.open(pdf2)

    # Criar um novo documento PDF
    pdf_final = fitz.open()

    # Adicionar páginas do primeiro PDF
    for page in doc1:
        pdf_final.insert_pdf(doc1, from_page=page.number, to_page=page.number)

    # Adicionar páginas do segundo PDF
    for page in doc2:
        pdf_final.insert_pdf(doc2, from_page=page.number, to_page=page.number)

    # Salvar o PDF final
    pdf_final.save(pdf_saida)
    pdf_final.close()
    doc1.close()
    doc2.close()
    print(f"✅ PDFs combinados e salvos como: {pdf_saida}")

# Exemplo de uso
juntar_pdfs("pdf-1.pdf", "pdf-2.pdf", "pdf_combinado.pdf")