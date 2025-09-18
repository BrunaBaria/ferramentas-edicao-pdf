import os
import comtypes.client

def convert_docx_to_pdf(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False
    
    for file in os.listdir(input_folder):
        if file.endswith(".docx") and not file.startswith("~$"):
            docx_path = os.path.join(input_folder, file)
            pdf_path = os.path.join(output_folder, file.replace(".docx", ".pdf"))
            
            doc = word.Documents.Open(docx_path)
            doc.SaveAs(pdf_path, FileFormat=17)  # 17 é o formato PDF no Word
            doc.Close()
            print(f"Convertido: {file} -> {pdf_path}")
    
    word.Quit()

if __name__ == "__main__":
    input_folder = os.getcwd()  # Diretório atual
    output_folder = os.path.join(input_folder, "exports")
    convert_docx_to_pdf(input_folder, output_folder)
