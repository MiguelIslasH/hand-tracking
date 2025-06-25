# Tracker de Manos - Proyecto de Seguimiento con MediaPipe

## Descripción

Este proyecto implementa un sistema de seguimiento de manos en tiempo real utilizando OpenCV y MediaPipe. El programa detecta las manos del usuario a través de la cámara web y dibuja líneas desde la punta del pulgar hasta las puntas de los otros dedos, creando un efecto visual similar a un láser.

## Características

- **Detección de manos en tiempo real**: Utiliza MediaPipe para detectar hasta 2 manos simultáneamente
- **Seguimiento de dedos**: Identifica y rastrea los 5 dedos de cada mano
- **Efecto visual**: Dibuja líneas desde el pulgar hasta los otros dedos
- **Interfaz visual**: Muestra el video en tiempo real con las líneas superpuestas
- **Control de salida**: Presiona 'ESC' para cerrar la aplicación

## Requisitos del Sistema

- Python 3.7 o superior
- Cámara web funcional
- Windows 10/11 (probado en Windows 10.0.26100)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/MiguelIslasH/hand-tracking.git
cd hand-tracking
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

**En Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**En Windows (Command Prompt):**
```cmd
.\venv\Scripts\activate.bat
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

O instalar manualmente:
```bash
pip install opencv-python mediapipe
```

## Ejecución

### Método 1: Ejecutar directamente

```bash
python index.py
```

### Método 2: Con el entorno virtual activado

```bash
# Asegúrate de que el entorno virtual esté activado
python index.py
```

## Configuración

### Ajustar la cámara

Si tu cámara no se detecta correctamente, puedes modificar la línea 8 en `index.py`:

```python
cap = cv2.VideoCapture(2)  # Cambia el número (0, 1, 2, etc.)
```

- `0`: Cámara principal
- `1`: Cámara secundaria
- `2`: Cámara externa (si está disponible)

### Parámetros de detección

Puedes ajustar la sensibilidad de detección modificando estos valores en `index.py`:

```python
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,              # Número máximo de manos a detectar
    min_detection_confidence=0.7,  # Confianza mínima para detectar (0.0-1.0)
    min_tracking_confidence=0.7    # Confianza mínima para rastrear (0.0-1.0)
)
```

## Uso

1. **Ejecuta el programa**: `python index.py`
2. **Posiciona tus manos**: Coloca tus manos frente a la cámara
3. **Observa el efecto**: Verás líneas rojas desde tu pulgar hasta los otros dedos
4. **Salir**: Presiona la tecla `ESC` para cerrar la aplicación

## Estructura del Proyecto

```
tracker/
├── index.py          # Archivo principal del programa
├── requirements.txt  # Dependencias del proyecto
├── .gitignore       # Archivos a ignorar en Git
├── README.md        # Este archivo
└── venv/            # Entorno virtual (no incluido en Git)
```

## Dependencias Principales

- **OpenCV (opencv-python)**: Procesamiento de imágenes y video
- **MediaPipe**: Detección y seguimiento de manos
- **NumPy**: Operaciones numéricas (incluido con OpenCV)

## Solución de Problemas

### La cámara no se abre
- Verifica que tu cámara web esté conectada y funcionando
- Cambia el índice de la cámara en `cv2.VideoCapture()`
- Asegúrate de que no haya otros programas usando la cámara

### Detección lenta o inexacta
- Ajusta los valores de `min_detection_confidence` y `min_tracking_confidence`
- Mejora la iluminación del entorno
- Mantén las manos a una distancia adecuada de la cámara

### Errores de importación
- Asegúrate de que el entorno virtual esté activado
- Reinstala las dependencias: `pip install -r requirements.txt`

## Personalización

### Cambiar el color de las líneas
Modifica la línea 28 en `index.py`:
```python
cv2.line(image, thumb_tip, finger_tip, (0, 0, 255), 2)  # (B, G, R)
```

### Cambiar el grosor de las líneas
Modifica el último parámetro en `cv2.line()`:
```python
cv2.line(image, thumb_tip, finger_tip, (0, 0, 255), 5)  # Grosor = 5
```

## Contribuciones

Si deseas contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

## Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

## Notas Importantes

### ¿Por qué ignorar el entorno virtual?

El directorio `venv/` está incluido en el archivo `.gitignore` porque:

- **Tamaño**: Los entornos virtuales pueden ser muy grandes (cientos de MB)
- **Específico del sistema**: Cada desarrollador debe crear su propio entorno
- **Dependencias**: Las versiones exactas pueden variar entre sistemas operativos
- **Buenas prácticas**: Es estándar en proyectos Python ignorar entornos virtuales

En su lugar, usamos `requirements.txt` para especificar las dependencias exactas que necesita el proyecto.

---

**Nota**: Este proyecto es educativo y está diseñado para demostrar las capacidades de MediaPipe y OpenCV en el seguimiento de manos en tiempo real.

---
