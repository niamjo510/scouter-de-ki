import cv2
class CamaraHandler:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
    
    def get_frame(self):
        exito,frame= self.cap.read()
        return frame
    def liberar(self):
        self.cap.release()