from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .scraping import extraer_oposiciones

def mostrar_resultados(request):
    urls = [
        'https://www.boe.es/boe/dias/2025/03/28/pdfs/BOE-S-2025-75.pdf',
        'https://www.boe.es/boe/dias/2025/04/11/pdfs/BOE-S-2025-88.pdf'
    ]
    resultados = extraer_oposiciones(urls)
    return render(request, "scraper/resultados.html", {"resultados": resultados})
