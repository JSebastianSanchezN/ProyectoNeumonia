#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aplicación gráfica en Tkinter para la detección rápida de neumonía.
Permite cargar imágenes médicas (DICOM/JPG/PNG), aplicar un modelo
predictivo, visualizar resultados con heatmap, guardar historial en CSV
y exportar reportes en PDF.
"""

# ========================
# Importaciones estándar
# ========================
import csv
import getpass
import time
import os

# ========================
# Importaciones de terceros
# ========================
from tkinter import *
from tkinter import ttk, font, filedialog, Entry
from tkinter.messagebox import askokcancel, showinfo, WARNING
from PIL import ImageTk, Image
import pyautogui
import tkcap
import img2pdf
import numpy as np

# ========================
# Importaciones locales
# ========================
from ..model import read_img
from ..controller import integrator


class App:
    """Clase principal de la aplicación de detección de neumonía."""

    def __init__(self):
        """Inicializa la interfaz gráfica de la aplicación."""
        self.root = Tk()
        self.root.title("Herramienta para la detección rápida de neumonía")

        # Fuente en negrita
        fonti = font.Font(weight='bold')

        # Configuración del grid
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.rowconfigure(2, weight=1)

        # Etiquetas
        self.lab1 = ttk.Label(self.root, text="Imagen Radiográfica",
                              font=fonti)
        self.lab2 = ttk.Label(self.root, text="Imagen con Heatmap",
                              font=fonti)
        self.lab3 = ttk.Label(self.root, text="Resultado:", font=fonti)
        self.lab4 = ttk.Label(self.root, text="Cédula Paciente:", font=fonti)
        self.lab5 = ttk.Label(
            self.root,
            text=("SOFTWARE PARA EL APOYO AL DIAGNÓSTICO MÉDICO DE "
                  "NEUMONÍA"),
            font=fonti
        )
        self.lab6 = ttk.Label(self.root, text="Probabilidad:", font=fonti)

        # Variables de entrada (ID y resultado)
        self.ID = StringVar()
        self.result = StringVar()

        # Caja de entrada para ID
        self.text1 = ttk.Entry(self.root, textvariable=self.ID, width=20)
        self.ID_content = self.text1.get()

        # Cajas de texto para imágenes y resultados
        self.text_img1 = Text(self.root, width=40, height=20)
        self.text_img2 = Text(self.root, width=40, height=20)
        self.text2 = Text(self.root, width=15, height=2)
        self.text3 = Text(self.root, width=15, height=2)

        # Botones
        self.button1 = ttk.Button(
            self.root, text="Predecir", state='disabled',
            command=self.run_model
        )
        self.button2 = ttk.Button(
            self.root, text="Cargar Imagen", command=self.load_img_file
        )
        self.button3 = ttk.Button(
            self.root, text="Borrar", command=self.delete
        )
        self.button4 = ttk.Button(
            self.root, text="PDF", command=self.create_pdf
        )
        self.button6 = ttk.Button(
            self.root, text="Guardar", command=self.save_results_csv
        )

        # Posicionamiento de widgets
        self.lab5.grid(row=0, column=0, columnspan=4, pady=10)
        
        self.lab1.grid(row=1, column=0, columnspan=2, sticky='s')
        self.text_img1.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.lab2.grid(row=1, column=2, columnspan=2, sticky='s')
        self.text_img2.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.lab4.grid(row=3, column=0, columnspan=2, pady=5)
        self.text1.grid(row=4, column=0, columnspan=2, pady=5)

        self.lab3.grid(row=3, column=2, sticky='e', pady=5)
        self.text2.grid(row=3, column=3, sticky='w', pady=5)

        self.lab6.grid(row=4, column=2, sticky='e', pady=5)
        self.text3.grid(row=4, column=3, sticky='w', pady=5)

        self.button2.grid(row=5, column=0, pady=10)
        self.button1.grid(row=5, column=1, pady=10)
        self.button6.grid(row=5, column=2, pady=10)
        self.button4.grid(row=5, column=3, pady=10)
        self.button3.grid(row=6, column=0, columnspan=4, pady=10)

        # Poner foco en ID del paciente
        self.text1.focus_set()

        # Variables internas
        self.array = None  # Imagen cargada
        self.reportID = 0  # ID para reportes PDF

        # Ejecutar loop principal
        self.root.mainloop()

    def load_img_file(self):
        """Carga una imagen (DICOM o JPG/PNG) y la muestra en la interfaz."""
        filepath = filedialog.askopenfilename(
            initialdir="data",
            title="Select image",
            filetypes=(
                ('DICOM', '*.dcm'),
                ('JPEG', '*.jpeg'),
                ('jpg files', '*.jpg'),
                ('png files', '*.png')
            )
        )
        if filepath:
            file_extension = filepath.lower().split('.')[-1]
            if file_extension == 'dcm':
                self.array, img2show = read_img.read_dicom_file(filepath)
            elif file_extension in ['jpeg', 'jpg', 'png']:
                self.array, img2show = read_img.read_jpg_file(filepath)
            else:
                showinfo(title="Error",
                         message="Tipo de archivo no soportado.")
                return

            self.img1 = img2show.resize((250, 250),
                                        Image.Resampling.LANCZOS)
            self.img1 = ImageTk.PhotoImage(self.img1)
            self.text_img1.image_create(END, image=self.img1)
            self.button1['state'] = 'enabled'

    def run_model(self):
        """Ejecuta el modelo predictivo y muestra resultados y heatmap."""
        self.label, self.proba, self.heatmap = integrator.predict(self.array)
        self.img2 = Image.fromarray(self.heatmap)
        self.img2 = self.img2.resize((250, 250),
                                     Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(self.img2)
        print('OK')
        self.text_img2.image_create(END, image=self.img2)
        self.text2.insert(END, self.label)
        self.text3.insert(END, '{:.2f}'.format(self.proba) + '%')

    def save_results_csv(self):
        """Guarda los resultados de la predicción en un archivo CSV."""
        with open('reports/historial.csv', 'a') as csvfile:
            w = csv.writer(csvfile, delimiter='-')
            w.writerow([
                self.text1.get(),
                self.label,
                '{:.2f}'.format(self.proba) + '%'
            ])
            showinfo(title='Guardar',
                     message='Los datos se guardaron con éxito.')

    def create_pdf(self):
        """Genera un archivo PDF con captura de la interfaz."""
        cap = tkcap.CAP(self.root)
        ID = 'Reporte' + str(self.reportID) + '.jpg'
        img_path = os.path.join('reports', ID)
        img = cap.capture(img_path)
        img = Image.open(img_path)
        img = img.convert('RGB')
        pdf_filename = r'Reporte' + str(self.reportID) + '.pdf'
        pdf_path = os.path.join('reports', pdf_filename)
        img.save(pdf_path)
        self.reportID += 1
        showinfo(title='PDF', message='El PDF fue generado con éxito.')

    def delete(self):
        """Limpia todos los datos de la interfaz."""
        answer = askokcancel(
            title='Confirmación',
            message='Se borrarán todos los datos.',
            icon=WARNING
        )
        if answer:
            self.text1.delete(0, 'end')
            self.text2.delete(1.0, 'end')
            self.text3.delete(1.0, 'end')
            self.text_img1.delete(self.img1, 'end')
            self.text_img2.delete(self.img2, 'end')
            showinfo(title='Borrar',
                     message='Los datos se borraron con éxito')


def main():
    """Función principal para ejecutar la aplicación."""
    my_app = App()
    return 0


if __name__ == '__main__':
    main()
