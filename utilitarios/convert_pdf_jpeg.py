import fitz  # PyMuPDF
from PIL import Image
import os

def get_unique_filename(output_folder, base_name, extension):
    """
    Gera um nome de arquivo único no diretório especificado, adicionando um sufixo incremental se necessário.
    """
    counter = 1
    unique_name = f"{base_name}{extension}"
    while os.path.exists(os.path.join(output_folder, unique_name)):
        unique_name = f"{base_name}_{counter}{extension}"
        counter += 1
    return unique_name

def pdf_to_jpeg(pdf_path, output_folder):
    # Abrir o arquivo PDF
    pdf_document = fitz.open(pdf_path)

    for page_num in range(len(pdf_document)):
        # Obter a página atual
        page = pdf_document[page_num]
        
        # Renderizar a página como uma imagem (dpi = 150 para boa qualidade)
        pix = page.get_pixmap(dpi=150)
        
        # Converter o Pixmap para uma imagem PIL
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Gerar um nome único para o arquivo
        base_name = f"page_{page_num + 1}"
        unique_name = get_unique_filename(output_folder, base_name, ".jpeg")
        output_path = os.path.join(output_folder, unique_name)
        
        # Salvar a imagem como JPEG
        image.save(output_path, "JPEG")
        print(f"Página {page_num + 1} salva como {output_path}")

    # Fechar o documento PDF
    pdf_document.close()

# Exemplo de uso
pdf_path = r'C:\Users\seu-user\seu-diretorio\seu-doc.pdf'  # Caminho do PDF
output_folder = "conversor"  # Pasta para salvar as imagens

# Certifique-se de que a pasta de saída existe
os.makedirs(output_folder, exist_ok=True)

pdf_to_jpeg(pdf_path, output_folder)
