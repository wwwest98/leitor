import PyPDF2
import sys


def verificar_pdf_iron_mountain(arquivo_pdf):
    try:
        with open(arquivo_pdf, 'rb') as arquivo:
            leitor_pdf = PyPDF2.PdfReader(arquivo)
            ultima_pagina = leitor_pdf.pages[-1]
            texto_pagina = ultima_pagina.extract_text()

            if "iron mountain" in texto_pagina.lower():
                return "ok"
            else:
                return "falhou"

    except FileNotFoundError:
        return "arquivo não encontrado"
    except PyPDF2.utils.PdfReadError:
        return "erro na leitura do PDF"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python verificar_pdf.py <caminho_do_arquivo.pdf>")
        sys.exit(1)

    arquivo_pdf = sys.argv[1]
    resultado = verificar_pdf_iron_mountain(arquivo_pdf)
    print(resultado)
