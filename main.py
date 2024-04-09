import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
import string
import random


class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.archivo = None
        self.lista_archivos = []
        self.boton_cargar = tk.Button(master, text="Cargar Archivo", command=self.cargar_archivo)
        self.boton_cargar.pack()
        self.boton_carpeta = tk.Button(master, text="Seleccionar Carpeta", command=self.seleccionar_carpeta)
        self.boton_carpeta.pack()
        self.boton_ejecutar = tk.Button(master, text="Ejecutar Script", command=self.ejecutar_script)
        self.boton_ejecutar.pack()

    def cargar_archivo(self):
        self.archivo = filedialog.askopenfilename()
        self.lista_archivos.append(self.archivo)
        messagebox.showinfo("Archivo cargado", f"Archivo cargado: {self.archivo}")

    def seleccionar_carpeta(self):
        self.carpeta = filedialog.askdirectory()
        self.carpeta = self.carpeta + "/" + str(''.join(random.choice(string.ascii_letters) for _ in range(20))) + ".pdf"
        messagebox.showinfo("Carpeta seleccionada", f"Carpeta seleccionada: {self.carpeta}")

    def ejecutar_script(self):
        if self.archivo:

            pdf_writer = PyPDF2.PdfWriter()

            for pdf in self.lista_archivos:
                pdf_reader = PyPDF2.PdfReader(pdf)
                for pagina in range(len(pdf_reader.pages)):
                    pdf_writer.add_page(pdf_reader.pages[pagina])

            print(self.carpeta)
            with open(self.carpeta, 'wb') as out:
                pdf_writer.write(out)

            messagebox.showinfo("Script ejecutado", f"Script ejecutado para el archivo: {self.archivo}")
        else:
            messagebox.showwarning("No hay archivo", "Por favor, carga un archivo primero")


root = tk.Tk()
root.geometry("250x100")
app = Aplicacion(root)
root.mainloop()
