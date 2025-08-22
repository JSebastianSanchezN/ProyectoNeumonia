# Proyecto Neumonía

## Índice 
- Descripción
- Instalación
- Herramientas utilizadas
- Acceso al proyecto
- Contribuidores
- Licencia

## Descripción
Este proyecto implementa un sistema de **clasificación automática de radiografías de tórax en formato DICOM**, utilizando redes neuronales convolucionales (CNN). El objetivo es clasificar las imágenes en tres categorías:

- Neumonía Bacteriana  
- Neumonía Viral  
- Sin Neumonía  

Además, se emplea la técnica **Grad-CAM** para generar mapas de calor que resaltan las regiones relevantes de la imagen que influyen en la predicción del modelo.

El desarrollo sigue el patrón de diseño **MVC (Modelo-Vista-Controlador)**, con un enfoque modular, cohesivo y desacoplado para facilitar su mantenimiento y escalabilidad.

<img width="815" height="589" alt="image" src="https://github.com/user-attachments/assets/878c6a4d-17ca-49e9-a7a5-0dd43278bfbd" />

---

## Instalación:

Clonar el repositorio:
https://github.com/JSebastianSanchezN/ProyectoNeumonia.git

---

## Ejecución

Ejecutar la interfaz gráfica (tkinter):

cd UAO-Neumonia

  pip install -r requirements.txt

  python detector_neumonia.py

---

## Flujo de Procesamiento

El sistema sigue una arquitectura modular basada en el patrón **MVC (Model-View-Controller)**, donde cada script cumple una función específica dentro del flujo de procesamiento de las imágenes médicas.  

### Scripts principales

- **detector_neumonia.py**  
  Contiene la interfaz gráfica desarrollada con **Tkinter**.  
  Los botones de la interfaz llaman métodos definidos en los demás módulos.  

- **read_img.py**  
  Lee imágenes en formato **DICOM**, las convierte a arreglo y las prepara para su visualización y preprocesamiento.  

- **preprocess_img.py**  
  Recibe el arreglo proveniente de `read_img.py` y aplica las siguientes transformaciones:  
  - Resize a 512x512  
  - Conversión a escala de grises  
  - Ecualización del histograma con **CLAHE**  
  - Normalización de la imagen en el rango [0,1]  
  - Conversión a batch (tensor)  

- **load_model.py**  
  Carga el modelo entrenado (`WilhemNet86.h5`) para la clasificación de imágenes.  

- **grad_cam.py**  
  Procesa la imagen y genera:  
  - Predicción de clase  
  - Probabilidad asociada  
  - Mapa de calor Grad-CAM resaltando regiones relevantes.  

- **integrator.py**  
  Módulo que integra todos los componentes anteriores y retorna solo la información necesaria para la interfaz gráfica:  
  - Clase predicha  
  - Probabilidad  
  - Imagen con mapa Grad-CAM

---
## Uso de la Interfaz Gráfica:

- Ingrese la cédula del paciente en la caja de texto
- Presione el botón 'Cargar Imagen', seleccione la imagen del explorador de archivos del computador (Imagenes de prueba en https://drive.google.com/drive/folders/1WOuL0wdVC6aojy8IfssHcqZ4Up14dy0g?usp=drive_link)
- Presione el botón 'Predecir' y espere unos segundos hasta que observe los resultados
- Presione el botón 'Guardar' para almacenar la información del paciente en un archivo excel con extensión .csv
- Presione el botón 'PDF' para descargar un archivo PDF con la información desplegada en la interfaz
- Presión el botón 'Borrar' si desea cargar una nueva imagen
---
## Resultados

Ejemplo de salida del sistema:

Imagen original (DICOM)

Imagen procesada

Predicción de clase y probabilidad

Mapa de calor generado por Grad-CAM

---

## Contribuidores:

* Johan Sebastian Sanchez Navas - https://github.com/JSebastianSanchezN
* Angel David Duarte Loaiza - https://github.com/AngelDDL
* Sharis Aranxa Barbosa Prado - https://github.com/SAranxa
* Santiago Cortes Murcia - https://github.com/SantiagoCorM
