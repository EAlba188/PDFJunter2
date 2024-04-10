import PySimpleGUI as sg
from pdf_join import pdf_join

lista_archivos = []
ruta_carpeta = ""
texto_ingresado = ""


def agregar_archivo(ruta_archivo):
    if ruta_archivo.endswith(".pdf"):
        lista_archivos.append(ruta_archivo)
        actualizar_lista()


def borrar_lista():
    global lista_archivos
    lista_archivos = []
    actualizar_lista()


def actualizar_lista():
    window["lista"].update(values=lista_archivos)


def seleccionar_carpeta():
    global ruta_carpeta
    ruta_carpeta = sg.popup_get_folder(title="Seleccionar carpeta", message="Selecciona la carpeta para guardar")
    window["ruta_carpeta"].update(value=ruta_carpeta)


def obtener_texto(valor):
    global texto_ingresado
    texto_ingresado = valor


def enviar_datos():
    ruta_salida = ruta_carpeta + "/" + texto_ingresado + ".pdf"

    pdf_join(lista_archivos, ruta_salida)
    print(f"Lista de archivos: {lista_archivos}")
    print(f"Ruta de la carpeta: {ruta_carpeta}")
    print(f"Texto ingresado: {texto_ingresado}")
    sg.popup_ok("Terminado")


layout = [
    [sg.Button("Seleccionar archivo PDF", key="archivo")],
    [sg.Listbox(values=lista_archivos, key="lista", size=(40, 10)), sg.Button("Borrar lista", key="borrar")],
    [sg.Button("Seleccionar carpeta", key="carpeta")],
    [sg.Text("Ruta de la carpeta:"), sg.Text(ruta_carpeta, key="ruta_carpeta")],
    [sg.InputText(key="texto", change_submits=True, size=(40, 1)), sg.Button("Enviar datos", key="enviar")],
]

window = sg.Window("Programa PySimpleGUI", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "archivo":
        ruta_archivo = sg.popup_get_file(title="Seleccionar archivo PDF", message="Selecciona el PDF")
        if ruta_archivo:
            agregar_archivo(ruta_archivo)
    elif event == "borrar":
        borrar_lista()
    elif event == "carpeta":
        seleccionar_carpeta()
    elif event == "texto":
        obtener_texto(values["texto"])
    elif event == "enviar":
        enviar_datos()

window.close()
