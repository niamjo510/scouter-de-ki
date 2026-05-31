# 1. Visión General del Proyecto
Una aplicación de escritorio en Python que utiliza visión computacional en tiempo real para detectar la postura del usuario. Al reconocer la "pose de carga de Ki" (estilo Dragon Ball), el sistema renderiza un aura dinámica alrededor del usuario y registra el tiempo de entrenamiento en una base de datos en la nube para medir el "nivel de poder" acumulado.

# 2. Stack Tecnológico
Lenguaje: Python 3.x

Visión Computacional: * OpenCV (Procesamiento de video y renderizado).

MediaPipe (Estimación de pose y segmentación de silueta).

Backend y Base de Datos: Supabase (Auth, PostgreSQL, Storage).

Variables de Entorno: python-dotenv (Para proteger las credenciales de Supabase).

# 3. Arquitectura Orientada a Objetos (Core)
El proyecto se dividirá en los siguientes módulos/clases:

CameraHandler

Responsabilidad: Capturar el feed de la webcam y gestionar la resolución del video.

PoseDetector

Responsabilidad: Extraer los landmarks (puntos clave) del cuerpo y generar la máscara de segmentación (silueta) usando MediaPipe.

BattlePoseAnalyzer

Responsabilidad: Contener la lógica matemática. Calcular ángulos entre rodillas, codos y muñecas para determinar si el estado actual es CHARGING_KI o IDLE.

EffectRenderer

Responsabilidad: Aplicar los efectos visuales. Usar la máscara de segmentación para dibujar el resplandor (aura) detrás/alrededor del usuario.

SupabaseManager

Responsabilidad: Conexión con la API de Supabase. Manejar el login, descargar las texturas del aura y subir el tiempo total de entrenamiento al cerrar la app.

main.py (Controller)

Responsabilidad: El punto de entrada del programa. Orquesta el bucle de captura de video y hace que las clases se comuniquen entre sí.

# 4. Requerimientos de Supabase
Autenticación: Sistema simple de login por email/contraseña.

Storage (Buckets): * Un bucket llamado vfx_assets que contenga imágenes como aura_base.png o super_saiyan.png.

Database (Tabla training_logs):

id (UUID, Primary Key)

user_id (UUID, Foreign Key)

session_date (Timestamp)

ki_charged_seconds (Integer)

aura_level_reached (String)

# 5. Fases de Desarrollo (Roadmap)
[x] Fase 1: Configuración Base

Configurar entorno virtual (venv).

Instalar dependencias (opencv-python, mediapipe, supabase).

Crear la estructura de archivos en blanco según el diseño POO.

[x] Fase 2: Captura y Tracking (Local)

Programar CameraHandler para ver la cámara en una ventana.

Conectar PoseDetector para dibujar los puntos del esqueleto sobre el video.

[] Fase 3: El Algoritmo de "Carga de Ki"

En BattlePoseAnalyzer, definir la lógica matemática de la pose.

Imprimir en la consola "CARGANDO KI" cuando el usuario haga la pose correcta.

[ ] Fase 4: Efectos Visuales (VFX)

Extraer la silueta del usuario.

Programar EffectRenderer para colorear los bordes de la silueta de amarillo cuando esté cargando Ki.

[ ] Fase 5: Conexión a la Nube

Crear el proyecto en Supabase (Tablas y Buckets).

Programar SupabaseManager para autenticar al usuario al inicio y guardar sus estadísticas de sesión al presionar "Q" para salir.


# 6. Plan de Estudio Integrado (Herramientas de Aprendizaje)

* **Manejo de Errores (try/except):**
    * Implementar bloques `try/except` al inicializar la cámara para capturar fallos de hardware.
    * Proteger las peticiones de red hacia Supabase para evitar que la app se rompa si se pierde la conexión a internet.
* **Lectura y Escritura de Archivos (.txt / .csv):**
    * **Sistema de Caché Local:** Si la conexión a Supabase falla, la app escribirá los datos de la sesión de entrenamiento en un archivo `.csv` local (`local_logs.csv`).
    * Al iniciar la app, el sistema intentará leer ese archivo para sincronizar los datos pendientes con la nube.