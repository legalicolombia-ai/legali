import os
import openai
from PIL import Image, ImageDraw, ImageFont

class AIDesigner:
    def __init__(self, output_dir="reports/carruseles", assets_dir="assets"):
        self.output_dir = output_dir
        self.assets_dir = assets_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generar_prompt_visual(self, concepto_slide):
        """Usa GPT para traducir la idea de la slide en un prompt de imagen profesional."""
        prompt_system = (
            "Eres un Director de Arte y Diseñador Visual Senior especializado en marcas LegalTech. "
            "Crea un prompt detallado en inglés para DALL-E 3 que describa un fondo o ilustración abstracta, "
            "minimalista, elegante y corporativa. Colores clave: Navy Blue, Dark Slate, Cyan Accent. "
            "Sin texto en la imagen generada, estilo 3D render o vector minimalista."
        )
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt_system},
                {"role": "user", "content": f"Concepto de la diapositiva: {concepto_slide}"}
            ]
        )
        return response.choices[0].message.content

    def generar_imagen_dalle(self, prompt):
        """Genera una imagen conceptual usando DALL-E 3."""
        print(f"🎨 [DISEÑADOR IA]: Generando ilustración DALL-E 3 para prompt: {prompt[:60]}...")
        try:
            result = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )
            image_url = result.data[0].url
            # Aquí podrías descargar la imagen usando requests y usarla como fondo o asset
            return image_url
        except Exception as e:
            print(f"⚠️ [DISEÑADOR IA]: Error al invocar DALL-E 3 ({e}). Usando motor gráfico de respaldo.")
            return None
