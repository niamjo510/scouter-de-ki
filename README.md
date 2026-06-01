# 🐉 Scouter de Ki con IA (Pose Estimation)

¡Bienvenido a la Sala del Espíritu y el Tiempo! Este es un proyecto Full-Stack de Visión por Computadora que utiliza Inteligencia Artificial para detectar tu esqueleto en tiempo real, identificar si estás haciendo una pose de batalla (Carga de Ki), aplicarte un aura de energía y enviar tu puntuación a la nube.

## ✨ Características Principales

* **Detección de Pose con IA:** Utiliza `MediaPipe` para identificar las articulaciones del cuerpo humano a través de la cámara web.
* **Cálculo Matemático en Tiempo Real:** Analiza la distancia entre las muñecas y los hombros para determinar si el usuario ha entrado en la "Pose de Batalla".
* **Efectos Visuales (VFX):** Extrae la silueta del usuario utilizando máscaras de imagen y dibuja un aura brillante generada matemáticamente con `NumPy` y `OpenCV`.
* **Conexión a la Nube:** Integración con la API de `Supabase` para almacenar el "Nivel de Ki" (frames acumulados) en una base de datos PostgreSQL.
* **Sistema de Tolerancia a Fallos (Modo Offline):** Si la conexión a internet falla, el programa guarda los registros en una caché local (`local_logs.csv`) y los sincroniza automáticamente con la nube en la siguiente ejecución.

## 🛠️ Tecnologías Utilizadas

* **Python 3.11** - Lenguaje base.
* **OpenCV (`cv2`)** - Captura de video y procesamiento de imágenes.
* **MediaPipe** - Modelo de Machine Learning para estimación de pose.
* **NumPy** - Cálculos matriciales para el renderizado del aura.
* **Supabase** - Backend as a Service (BaaS) y base de datos.
* **Python-dotenv** - Gestión segura de variables de entorno.

## 🚀 Guía de Instalación
Sigue estos pasos para entrenar en tu propia máquina:
**1. Clonar el repositorio**
```bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd TU_REPOSITORIO
