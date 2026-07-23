import json
import os
from datetime import datetime

class MemoryManager:
    def __init__(self, filepath="data/historial.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            self._guardar_datos([])

    def _cargar_datos(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _guardar_datos(self, datos):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

    def registrar_publicacion(self, enfoque, accion, copy_generado, rutas_imagenes):
        historial = self._cargar_datos()
        
        nuevo_registro = {
            "id": len(historial) + 1,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "enfoque_estratego": enfoque,
            "accion_clave": accion,
            "copy": copy_generado,
            "imagenes": rutas_imagenes
        }
        
        historial.append(nuevo_registro)
        self._guardar_datos(historial)
        print(f"🧠 [MEMORIA]: Publicación #{nuevo_registro['id']} guardada exitosamente en '{self.filepath}'")

    def obtener_temas_recientes(self, limite=5):
        historial = self._cargar_datos()
        if not historial:
            return "No hay publicaciones anteriores registradas."
        
        ultimos = historial[-limite:]
        resumenes = [f"- [{h['fecha']}] {h['accion_clave']}" for h in ultimos]
        return "\n".join(resumenes)
