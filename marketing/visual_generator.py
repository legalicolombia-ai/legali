import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

class NanoBananaClient:
    """
    Cliente oficial para integrar Nano Banana AI en el pipeline de LEGALI.
    """
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("NANOBANANA_API_KEY", "")
        self.endpoint = "https://api.nanobanana.ai/v1/generate"

    def generar_imagen(self, prompt_text, width=1080, height=1350):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": f"Cinematic dark corporate legal security, high contrast, professional photography: {prompt_text}",
            "width": width,
            "height": height
        }
        
        try:
            if self.api_key:
                response = requests.post(self.endpoint, json=payload, headers=headers, timeout=15)
                if response.status_code == 200:
                    data = response.json()
                    image_url = data.get("image_url") or data.get("url")
                    if image_url:
                        img_data = requests.get(image_url).content
                        return Image.open(BytesIO(img_data)).convert("RGB")
        except Exception as e:
            print(f"[Nano Banana AI] Conexión en curso o respaldo activo: {e}")
            
        # Fondo de respaldo corporativo LegalTech de alta gama si la API key está pendiente de configuración
        fallback_img = Image.new("RGB", (width, height), color=(12, 17, 29))
        return fallback_img


class VisualGenerator:
    """
    LEGALI MARKETING AI - CEREBRO COMERCIAL & NANO BANANA AI INTEGRATION
    """
    def __init__(self):
        self.output_dir = os.path.join(os.path.expanduser("~"), "Downloads", "legali_leads_carrusel")
        os.makedirs(self.output_dir, exist_ok=True)
        self.ai_client = NanoBananaClient()

    def _get_font(self, size, bold=False):
        font_paths = [
            "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
            "C:\\Windows\\Fonts\\segoeui.ttf",
            "C:\\Windows\\Fonts\\calibri.ttf",
        ]
        for path in font_paths:
            if os.path.exists(path):
                try:
                    return ImageFont.truetype(path, size)
                except:
                    continue
        return ImageFont.load_default()

    def generar_slide_individual(self, titulo, contenido, index, total, pilar="Venta"):
        width, height = 1080, 1350
        
        text_white = (255, 255, 255)
        text_muted = (225, 232, 240)
        accent_gold = (212, 175, 55)
        accent_cyan = (56, 189, 248)
        
        # 1. Generación de imagen de fondo mediante Nano Banana AI usando el título como prompt inteligente
        base_img = self.ai_client.generar_imagen(prompt_text=titulo, width=width, height=height)
        
        # 2. Aplicar capa oscura semitransparente para garantizar contraste absoluto con las letras
        base_img = base_img.resize((width, height), Image.Resampling.LANCZOS).convert("RGBA")
        overlay = Image.new("RGBA", (width, height), (10, 15, 30, 215))
        img = Image.alpha_composite(base_img, overlay).convert("RGB")
        
        draw = ImageDraw.Draw(img)
        
        # 3. Barra de progreso superior orientada a conversión
        filled_width = int(width * (index / total))
        draw.rectangle([0, 0, filled_width, 16], fill=accent_cyan)
        
        # 4. Marca LEGALI y Pilar Comercial visible
        font_header = self._get_font(32, bold=True)
        draw.text((80, 75), "@legali_co", fill=accent_gold, font=font_header)
        
        pilar_text = f"PILAR: {pilar.upper()}"
        font_pilar = self._get_font(22, bold=True)
        bbox_p = font_pilar.getbbox(pilar_text)
        draw.text((width - 80 - (bbox_p[2] - bbox_p[0]), 80), pilar_text, fill=accent_cyan, font=font_pilar)

        # 5. Contenedor central translúcido elegante
        draw.rounded_rectangle([70, 220, width - 70, height - 200], radius=20, fill=(15, 23, 42, 220), outline=(56, 189, 248, 100), width=2)

        # 6. Título de alto impacto visual
        margin_x = 110
        font_title = self._get_font(54, bold=True)
        y_cursor = 290
        for line in textwrap.wrap(titulo, width=24):
            draw.text((margin_x, y_cursor), line, fill=text_white, font=font_title)
            y_cursor += 75

        # Línea divisoria cian LegalTech
        y_cursor += 15
        draw.rectangle([margin_x, y_cursor, margin_x + 120, y_cursor + 5], fill=accent_cyan)
        y_cursor += 60

        # 7. Contenido / Cuerpo claro y legible
        font_body = self._get_font(38, bold=False)
        for line in textwrap.wrap(contenido, width=40):
             draw.text((margin_x, y_cursor), line, fill=text_muted, font=font_body)
             y_cursor += 54
            
        # 8. Llamado a la Acción (CTA) Comercial inferior
        font_footer = self._get_font(30, bold=True)
        if index == total:
            footer_text = "💬 ¡ESCRIBENOS AL DM PARA ASESORÍA!"
        else:
            footer_text = "DESLIZA PARA CONOCER MÁS ➔"
            
        bbox_f = font_footer.getbbox(footer_text)
        draw.text(((width - (bbox_f[2] - bbox_f[0])) / 2, height - 115), footer_text, fill=accent_gold, font=font_footer)
        
        filename = f"lead_slide_{index}.png"
        filepath = os.path.join(self.output_dir, filename)
        img.save(filepath, "PNG", quality=95)
        return filepath

    def generar_carrusel_completo(self, slides, pilar="Venta"):
        rutas = []
        total = len(slides)
        for i, slide in enumerate(slides, 1):
            ruta = self.generar_slide_individual(
                titulo=slide.get("titulo", ""),
                contenido=slide.get("contenido", ""),
                index=i,
                total=total,
                pilar=pilar
            )
            rutas.append(ruta)
        return rutas
