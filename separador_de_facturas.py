import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog
import re
import pytesseract
from pdf2image import convert_from_path


contador_de_errores = 0

def obtener_numero_factura(pdf_path, num_pagina):
    global contador_de_errores
    # Convierte la página de PDF en una imagen utilizando PyMuPDF
    imagenes = convert_from_path(pdf_path, first_page=num_pagina+1, last_page=num_pagina+1)
    if imagenes:
        # Utilizar pytesseract para extraer texto de la imagen
        texto_extraido = pytesseract.image_to_string(imagenes[0])
        patron = r'FACTURA N.+:\s*(\d+)'
        # Buscar coincidencias en el texto
        coincidencias = re.search(patron, texto_extraido)
        # Si hay coincidencias, devolver el número encontrado
        if coincidencias:
            numero_factura = coincidencias.group(1)
            return numero_factura
        else:
            print(texto_extraido)
            contador_de_errores += 1
            return f"error_sin_numero_de_factura({contador_de_errores})"


def separar_pdf(pdf_path, carpeta_salida):
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        for num_pagina in range(pdf_reader.numPages):
            pagina = pdf_reader.getPage(num_pagina)
            numero_factura = obtener_numero_factura(pdf_path, num_pagina)

            pdf_nuevo = PyPDF2.PdfFileWriter()
            pdf_nuevo.addPage(pagina)

            nombre_archivo = f"{numero_factura}.pdf"
            ruta_salida = os.path.join(carpeta_salida, nombre_archivo)

            with open(ruta_salida, 'wb') as pdf_salida:
                pdf_nuevo.write(pdf_salida)

def seleccionar_pdf():
    ruta_pdf = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
    entry_pdf.delete(0, tk.END)
    entry_pdf.insert(0, ruta_pdf)

def seleccionar_carpeta():
    carpeta_salida = filedialog.askdirectory()
    entry_carpeta.delete(0, tk.END)
    entry_carpeta.insert(0, carpeta_salida)

def separar_pdf_gui():
    global entry_pdf
    pdf_path = entry_pdf.get()
    carpeta_salida = entry_carpeta.get()

    if not pdf_path or not carpeta_salida:
        tk.messagebox.showwarning("Error", "Por favor, selecciona un archivo PDF y una carpeta de salida.")
        return

    separar_pdf(pdf_path, carpeta_salida)
    tk.messagebox.showinfo("Éxito", "El PDF se ha separado exitosamente.")

# Crear la interfaz gráfica
app = tk.Tk()

app.title("Separador de PDFs")

# Etiqueta y entrada para el PDF
tk.Label(app, text="Selecciona un archivo PDF:").pack()
entry_pdf = tk.Entry(app, width=50)
entry_pdf.pack()
tk.Button(app, text="Buscar", command=seleccionar_pdf).pack()

# Etiqueta y entrada para la carpeta de salida
tk.Label(app, text="Selecciona una carpeta de salida:").pack()
entry_carpeta = tk.Entry(app, width=50)
entry_carpeta.pack()
tk.Button(app, text="Buscar", command=seleccionar_carpeta).pack()

# Botón para separar el PDF
tk.Button(app, text="Separar PDF", command=separar_pdf_gui).pack()

app.mainloop()

