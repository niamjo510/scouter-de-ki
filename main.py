import cv2
from src.ia_pose import PoseEngine
from src.analizador import BattlePoseAnalyzer
from src.efectos import EffectRenderer  # <-- IMPORTAMOS LA NUEVA CLASE
from src.nube import SupaBaseManager
# 1. Los Actores
try:
    captura = cv2.VideoCapture(0)
except:
    captura = None
    print("Error: No se detecta el visor de la cámara")
    exit()
mi_ia = PoseEngine()
mi_analizador = BattlePoseAnalyzer()
mi_efectos = EffectRenderer() # <-- CREAMOS EL OBJETO DE EFECTOS
contador_ki = 0
print("¡Radar del Dragón encendido! Presiona la tecla 'q' para salir.")

# 2. El Ciclo del Tiempo
while True:
    exito, frame = captura.read()
    if not exito:
        break

    # 3. La Acción
    datos_ia = mi_ia.procesar_frame(frame)
    
    # Creamos una variable que por defecto diga que NO estamos cargando ki
    esta_cargando = False 
    
    if datos_ia.pose_landmarks:
        # El analizador ahora nos devuelve True o False, y lo guardamos en la variable
        esta_cargando = mi_analizador.detectar_carga_ki(datos_ia.pose_landmarks)
        if esta_cargando:
            print("¡CARGANDO KI! ⚡")
            contador_ki +=1
    # --- AQUÍ APLICAMOS LOS EFECTOS VISUALES ---
    # Le mandamos el video, los datos (para que saque el recorte) y le decimos si hay que prender el aura
    frame = mi_efectos.aplicar_aura(frame, datos_ia, esta_cargando)
    # --------------------------------------------

    frame_dibujado = mi_ia.dibujar_puntos(frame, datos_ia)

    # 4. El Proyector
    cv2.imshow("Entrenamiento de Ki", frame_dibujado)

    # 5. El Botón de Escape
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

mi_gestor_nube=SupaBaseManager()
mi_gestor_nube.sincronizar_datos()
mi_gestor_nube.guardar_estadisticas(contador_ki)


captura.release()
cv2.destroyAllWindows()