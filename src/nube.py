import os 
from dotenv import load_dotenv
from supabase import create_client

class SupaBaseManager:
    def __init__(self):
        load_dotenv()
        url_proyecto=os.environ.get("SUPABASE_URL")
        url_proyectito=os.environ.get("SUPABASE_KEY")
        self.cliente=create_client(url_proyecto,url_proyectito)
    def guardar_estadisticas(self,total_frame_ki):
        try:
            self.cliente.table("sesion_entrenamiento").insert({"ki_cargado_frames": total_frame_ki}).execute()
        except:
            print("Conexion de Internet Fallida")
            with open("local_logs.csv","a")as archivo:
                archivo.write(f"{total_frame_ki}\n")
    def sincronizar_datos(self):
        try:
            with open("local_logs.csv","r")as archivo:
                datos_guardados= archivo.readlines()
                for datos in datos_guardados:
                    self.cliente.table("sesion_entrenamiento").insert({"ki_cargado_frames": int(datos)}).execute()
            with open("local_logs.csv", "w") as archivo_limpio:
                pass
        except:
            pass
