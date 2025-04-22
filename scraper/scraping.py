import requests
import re
import os
from pypdf import PdfReader

def extraer_oposiciones(urls):
    resultados = []

    for url in urls:
        print(f"Procesando URL: {url}")
        
        boe = requests.get(url)
        pdf_filename = 'BOE-Prueba.pdf'

        with open(pdf_filename, 'wb') as f:
            f.write(boe.content)

        with open(pdf_filename, 'rb') as archivo:
            leer_pdf = PdfReader(archivo)
            contenido = ""
            for pagina in leer_pdf.pages:
                contenido += pagina.extract_text()

        oposiciones = [frase.strip() for frase in re.findall(r'[^.!?]*\boposiciones\b[^.!?]*[.!?]', contenido, re.IGNORECASE)]
        plaza = [frase.strip() for frase in re.findall(r'[^.!?]*\bplaza\b[^.!?]*[.!?]', contenido, re.IGNORECASE)]
        convocatoria = [frase.strip() for frase in re.findall(r'[^.!?]*\bconvocatoria\b[^.!?]*[.!?]', contenido, re.IGNORECASE)]

        resultados.append({
            "url": url,
            "oposiciones": oposiciones,
            "plaza": plaza,
            "convocatoria": convocatoria
        })

        os.remove(pdf_filename)

    return resultados
