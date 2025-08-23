# Proyecto Neumonía  

## Índice  
- Descripción  
- Instalación  
- Ejecución  
- Flujo de Procesamiento  
- Uso de la Interfaz Gráfica  
- Resultados  
- Pruebas Unitarias  
- Estructura del Proyecto   
- Docker  
- Contribuidores  
- Licencia
- Observaciones

---

## Descripción  
Este proyecto implementa un sistema de **clasificación automática de radiografías de tórax en formato DICOM**, utilizando redes neuronales convolucionales (CNN).  

El objetivo es clasificar las imágenes en tres categorías:  
- Neumonía Bacteriana  
- Neumonía Viral  
- Sin Neumonía  

Se utiliza la técnica **Grad-CAM** para generar mapas de calor que resaltan las regiones relevantes de la imagen que influyen en la predicción del modelo.  

El desarrollo sigue el patrón de diseño **MVC (Modelo-Vista-Controlador)**, con un enfoque modular, cohesivo y desacoplado para facilitar su mantenimiento y escalabilidad.  

<img width="600" alt="interfaz" src="https://github.com/user-attachments/assets/878c6a4d-17ca-49e9-a7a5-0dd43278bfbd" />  

---

## Instalación  

1. Clonar el repositorio:  
   ```bash
   git clone https://github.com/JSebastianSanchezN/ProyectoNeumonia.git
   cd ProyectoNeumonia
2. Ejecutar
   ```bash
   uv run main.py 
3. Instalar dependencias:
   ```bash
   uv pip install -r requirements.txt

**Versión de Python:** `Python 3.11.9`  

⚠️ **Nota:** Las versiones posteriores a Python 3.11.9 presentaron problemas de compatibilidad con **Tkinter**, por lo que se recomienda utilizar esta versiónpara garantizar una ejecución estable.


---
## Ejecución

Para ejecutar el proyecto se tienen dos opciones
* Si la máquina cuenta con la herramienta Make se ejecuta el código:
     ```bash
     make cod
* De lo contrario, se ejecuta:
     ```bash
     uv run detector_neumonia.py

---
## Flujo de Procesamiento

El sistema sigue una arquitectura modular (MVC). Cada script cumple una función específica:
* `detector_neumonia.py` – Interfaz gráfica con Tkinter.
* `read_img.py` – Lee imágenes en formato DICOM y las convierte en arreglos.
* `preprocess_img.py` – Preprocesamiento (resize, escala de grises, CLAHE, normalización, batch tensor).
* `load_model.py` – Carga el modelo (WilhemNet86.h5).
* `grad_cam.py` – Genera predicción, probabilidad y mapa Grad-CAM.
* `integrator.py` – Integra todos los módulos y devuelve clase, probabilidad y mapa de calor.

---
## Uso de la Interfaz Gráfica

https://github.com/user-attachments/assets/4c7cf5ce-1efb-4ade-b27d-20178cdcda4c

**Paso a paso:**
1. Ingrese la cédula del paciente.
2. Presione Cargar Imagen y seleccione un archivo JPEG de la carpeta que se encuentra en el repositorio.
4. Presione Predecir para ver los resultados.
5. Presione Guardar para almacenar resultados en .csv.
6. Presione PDF para exportar un informe.
7. Presione Borrar para reiniciar el proceso.

---
## Resultados

Ejemplo de salida del sistema:

<img width="819" height="596" alt="image" src="https://github.com/user-attachments/assets/b9945b39-d45a-4021-a535-a7075bcec81d" />

Imagen original:

<img src="https://github.com/user-attachments/assets/907c41d4-d6da-4664-8f51-d562db98cdb9" alt="Imágen original" width="300"/>

Imagen procesada:

<img src="https://github.com/user-attachments/assets/8167ebde-6848-4220-b423-ab455e8f6224" alt="Imágen procesada" width="300"/>

Predicción de clase y probabilidad:

<img src="https://github.com/user-attachments/assets/4697ee50-f537-4a8c-a1a0-185bcf3707ab" width="300"/>


---
## Pruebas Unitarias

Se incluyen pruebas con pytest en la carpeta tests/.

Ejecutar con:
`pytest.py`

---
## Estructura del Proyecto

```plaintext
ProyectoNeumonia/
├── data/                   # Datos (pruebas o entrenamiento)
│   ├── raw/                # Datos sin procesar
│   ├── processed/          # Datos preprocesados
│   └── external/           # Datos externos
│
├── src/                    # Código fuente
│   ├── read_img.py
│   ├── preprocess_img.py
│   ├── load_model.py
│   ├── grad_cam.py
│   ├── integrator.py
│   └── detector_neumonia.py
│
├── tests/                  # Pruebas unitarias
│   ├── test_preprocess.py
│   └── test_integrator.py
│
├── reports/                # Reportes y figuras
├── docs/                   # Documentación adicional
│
├── requirements.txt        # Dependencias con versiones
├── .gitignore              # Ignorar modelo .h5 y datos pesados
├── LICENSE                 # Licencia
└── README.md               # Este archivo

```

---
## Docker

Completar...

---
## Contribuidores

Johan Sebastian Sanchez Navas – [GitHub](https://github.com/JSebastianSanchezN)

Angel David Duarte Loaiza – [GitHub](https://github.com/AngelDDL)

Sharis Aranxa Barbosa Prado – [GitHub](https://github.com/SAranxa)

Santiago Cortes Murcia – [GitHub](https://github.com/SantiagoCorM)

---
## Licencia
Este proyecto se distribuye bajo la licencia MIT.

Ver archivo [LICENSE](LICENSE) para más detalles.

