import math
class BattlePoseAnalyzer:
    def detectar_carga_ki(self, landmarks):
        mano_derecha_x= landmarks.landmark[16].x
        mano_derecha_y= landmarks.landmark[16].y
        mano_izquierda_x= landmarks.landmark[15].x
        mano_izquierda_y= landmarks.landmark[15].y
        
        distancia = math.hypot(mano_izquierda_x - mano_derecha_x, mano_izquierda_y - mano_derecha_y)
        
        if distancia < 0.15:
            return True
        else:
            return False