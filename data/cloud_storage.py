import os
import requests
import json

class CloudStorageManager:
    def __init__(self):
        # API Key gratuita de ImgBB (o configurable en .env)
        self.api_key = os.getenv("IMGBB_API_KEY", "")
        self.configurado = bool(self.api_key)

    def subir_imagen_carrusel(self, ruta_local_imagen):
        """Sube una imagen local a ImgBB y devuelve una URL pública HTTPS accesible por Meta."""
        if not self.configurado:
            print("⚠️ [CLOUD STORAGE]: API Key de ImgBB no configurada.")
            return None

        try:
            with open(ruta_local_imagen, "rb") as file:
                url = "https://api.imgbb.com/1/upload"
                payload = {
                    "key": self.api_key
                }
                files = {
                    "image": file
                }
                res = requests.post(url, data=payload, files=files)
                data = res.json()
                
                if data.get("success"):
                    secure_url = data["data"]["url"]
                    print(f"☁️ [CLOUD STORAGE]: Imagen alojada en nube -> {secure_url}")
                    return secure_url
                else:
                    print(f"❌ [CLOUD STORAGE]: Error al subir a ImgBB: {data}")
                    return None
        except Exception as e:
            print(f"❌ [CLOUD STORAGE]: Excepción al subir imagen: {e}")
            return None

    def subir_carrusel_completo(self, rutas_locales):
        """Sube todas las diapositivas del carrusel y retorna la lista de URLs públicas."""
        print("\n☁️ [CLOUD STORAGE]: Subiendo diapositivas a la nube...")
        urls_publicas = []
        for ruta in rutas_locales:
            url = self.subir_imagen_carrusel(ruta)
            if url:
                urls_publicas.append(url)
        return urls_publicas
