import cv2
import mediapipe as mp
# Entrando por la puerta trasera, ahora que sí existen los archivos:
from mediapipe.python.solutions import pose as mp_pose
from mediapipe.python.solutions import drawing_utils as mp_drawing

class PoseEngine:
    def __init__(self):
        # Usamos las herramientas directas
        self.pose = mp.solutions.pose.Pose(enable_segmentation=True)
        self.dibujo = mp.solutions.drawing_utils

    def procesar_frame(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultado = self.pose.process(frame_rgb)
        return resultado

    def dibujar_puntos(self, frame, resultado):
        if resultado.pose_landmarks:
            # Dibujamos usando las conexiones directas
            self.dibujo.draw_landmarks(
                frame, 
                resultado.pose_landmarks, 
                mp_pose.POSE_CONNECTIONS
            )
        return frame