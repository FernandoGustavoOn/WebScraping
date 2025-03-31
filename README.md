# WebScraping

Este repositório contém o código e os arquivos gerados durante a execução do **Teste de Web Scraping**, solicitado no teste de nivelamento técnico. O objetivo deste projeto é realizar o download dos anexos I e II do site da ANS e compactar os arquivos em um único arquivo `.zip`.

---

## Descrição do Projeto

O projeto executa as seguintes etapas:
1. Acessa o site oficial da ANS.
   - [Link para o site](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
2. Baixa os PDFs dos anexos I e II.
3. Compacta os dois arquivos PDF em um único arquivo `.zip`.

---

## Estrutura dos Arquivos

- **`scraping.py`:** Código Python que realiza todas as etapas descritas acima.
- **`anexos/`:** Pasta onde os PDFs baixados são armazenados.
  - `Anexo_I.pdf`: Primeiro anexo baixado do site.
  - `Anexo_II.pdf`: Segundo anexo baixado do site.
- **`compactado.zip`:** Arquivo `.zip` contendo os dois PDFs compactados.
- **`README.md`:** Documentação do projeto.

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:
- **Python 3.7 ou superior**
- Bibliotecas necessárias:
  - `requests` para realizar o download dos arquivos.
  - `zipfile` para criar o arquivo `.zip` (já incluído no Python).

Para instalar as dependências, execute:
```bash
pip install requests
