import wget
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import shutil  # para compactar os pdfs

# Constantes
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}
PAGINA_GOV = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def acessar_site(url, headers):
    """Acessa o site e retorna os links de PDFs filtrados."""
    resposta = requests.get(url, headers=headers)
    estrutura_site = BeautifulSoup(resposta.text, "html.parser")  # Lê o HTML
    pdf_links = [(link.get_text(strip=True), link.get("href")) # faz o scraping dos pdfs
                 for link in estrutura_site.find_all("a", class_="internal-link") 
                 if link.get("href").endswith(".pdf")] # somente se tiver o final.pdf
    print("___NOME DOS PDF's___")
    print(pdf_links)
    print("____________________")
    # Filtrar apenas os PDFs Anexo I e Anexo II
    pdf_filtrados = [(nome, url) for nome, url in pdf_links if "Anexo I" in nome or "Anexo II" in nome]
    return pdf_filtrados

def baixar_pdfs(pdf_filtrados, output_dir="pdfs/"):
    """Faz o download dos PDFs filtrados."""
    for nome, url in pdf_filtrados:
        print(f"Baixando: {nome} - {url}")
        wget.download(url, out=output_dir)
        print(f"\nDownload concluído do {nome}!\n")

def compactar_pdfs(output_zip="PDFs_compactados", source_dir="pdfs"):
    """Compacta os PDFs em um arquivo ZIP."""
    shutil.make_archive(output_zip, "zip", source_dir)
    print("\nArquivos compactados com sucesso!")

# Fluxo principal
if __name__ == "__main__":
    pdf_filtrados = acessar_site(PAGINA_GOV, HEADERS)
    baixar_pdfs(pdf_filtrados)
    compactar_pdfs()