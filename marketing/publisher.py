import os
import requests
import time
from data.cloud_storage import CloudStorageManager

class AIPublisher:
    def __init__(self):
        self.access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN", "")
        self.instagram_account_id = os.getenv("INSTAGRAM_ACCOUNT_ID", "")
        self.base_url = "https://graph.facebook.com/v19.0"
        self.cloud_manager = CloudStorageManager()

    def esta_configurado(self):
        """Verifica si tanto Meta API como Cloudinary están configurados."""
        meta_ok = bool(self.access_token and self.instagram_account_id)
        cloud_ok = self.cloud_manager.configurado
        return meta_ok and cloud_ok

    def subir_item_carrusel(self, image_url):
        """Paso 1 API Meta: Crear contenedor individual por imagen."""
        url = f"{self.base_url}/{self.instagram_account_id}/media"
        payload = {
            "image_url": image_url,
            "is_carousel_item": "true",
            "access_token": self.access_token
        }
        res = requests.post(url, data=payload)
        data = res.json()
        return data.get("id")

    def crear_contenedor_carrusel(self, item_ids, caption):
        """Paso 2 API Meta: Agrupar items en contenedor tipo CAROUSEL con el copy para @legali_co."""
        url = f"{self.base_url}/{self.instagram_account_id}/media"
        payload = {
            "media_type": "CAROUSEL",
            "children": ",".join(item_ids),
            "caption": caption,
            "access_token": self.access_token
        }
        res = requests.post(url, data=payload)
        data = res.json()
        return data.get("id")

    def publicar_contenedor(self, creation_id):
        """Paso 3 API Meta: Publicar el contenedor en el feed de @legali_co."""
        url = f"{self.base_url}/{self.instagram_account_id}/media_publish"
        payload = {
            "creation_id": creation_id,
            "access_token": self.access_token
        }
        res = requests.post(url, data=payload)
        data = res.json()
        return data.get("id")

    def ejecutar_publicacion_carrusel(self, rutas_imagenes_locales, caption):
        print("\n==================================================")
        print("📢 [PUBLICADOR IA]: Procesando salida para @legali_co...")
        print("==================================================")

        if not self.esta_configurado():
            print("ℹ️  [PUBLICADOR IA]: Modo Local / Preparación Activo.")
            print("📌 Para publicación automática directa en Instagram, configura las llaves en tu archivo .env.")
            print("📁 Los archivos locales quedaron guardados en 'reports/carruseles/'.")
            return None

        # 1. Subir imágenes a la nube
        urls_publicas = self.cloud_manager.subir_carrusel_completo(rutas_imagenes_locales)
        if len(urls_publicas) != len(rutas_imagenes_locales):
            print("⚠️ [PUBLICADOR IA]: No se pudieron alojar todas las imágenes en la nube. Operación cancelada.")
            return None

        # 2. Crear Items en la API de Meta
        print("🌐 [META API]: Enviando contenedores individuales a Instagram...")
        item_ids = []
        for url in urls_publicas:
            item_id = self.subir_item_carrusel(url)
            if item_id:
                item_ids.append(item_id)
            time.sleep(1) # Pausa breve respetando limites de frecuencia

        if len(item_ids) != len(urls_publicas):
            print("⚠️ Error al registrar contenedores en Meta API.")
            return None

        # 3. Crear contenedor general de carrusel
        print("📦 [META API]: Ensamblando carrusel multidiapositiva...")
        creation_id = self.crear_contenedor_carrusel(item_ids, caption)
        if not creation_id:
            return None

        # Pausa sugerida por Meta para procesamiento de medios
        time.sleep(5)

        # 4. Publicar
        post_id = self.publicar_contenedor(creation_id)
        if post_id:
            print(f"🚀 [PUBLICACIÓN EXITOSA]: Publicado en @legali_co. Post ID: {post_id}")
            return post_id
        return None
