import cv2
import numpy as np

class EffectRenderer:
    def aplicar_aura(self, frame, datos_ia, cargando_ki):
        # Si NO estamos cargando ki, o la IA no logró recortar la silueta, devolvemos el video normal
        if not cargando_ki or datos_ia.segmentation_mask is None:
            return frame
            
        # 1. Obtenemos el recorte del cuerpo (es una matriz de números decimales de 0 a 1)
        mascara = datos_ia.segmentation_mask
        
        # 2. La convertimos a una imagen en blanco y negro (0 a 255) que OpenCV pueda entender
        mascara_imagen = (mascara * 255).astype(np.uint8)
        
        # 3. Buscamos exactamente los bordes de esa mancha blanca (Canny es un buscador de bordes)
        bordes = cv2.Canny(mascara_imagen, 100, 200)
        
        # 4. El borde es muy delgado, así que lo "engrosamos" (dilate) para que parezca un aura
        kernel = np.ones((12, 12), np.uint8)
        aura_gruesa = cv2.dilate(bordes, kernel, iterations=1)
        
        # 5. Finalmente, donde el aura exista, pintamos el video de color Amarillo
        # Recuerda que en OpenCV los colores van al revés: BGR (Azul, Verde, Rojo). Amarillo es (0, 255, 255)
        frame[aura_gruesa > 0] = (0, 255, 255)
        
        return frame