from PyPDF2 import PdfMerger
import os
merger = PdfMerger()

pdfs='catalogos/'

# Recorre todos los archivos en la carpeta
for archivo in os.listdir(pdfs):
    if archivo.endswith('.pdf'):
        # Añade cada archivo PDF al merger
        merger.append(os.path.join(pdfs, archivo))

# Guarda el PDF combinado
output_file = 'catalogo.pdf'
merger.write(output_file)
merger.close()

print(f'Se ha creado {output_file} con éxito.')
