import PyPDF2


def pdf_join(lista_archivos, ruta_salida):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in lista_archivos:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for pagina in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[pagina])

    print(ruta_salida)
    with open(ruta_salida, 'wb') as out:
        pdf_writer.write(out)
