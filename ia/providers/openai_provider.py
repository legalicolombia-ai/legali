from pathlib import Path
import os
import base64

from dotenv import load_dotenv
from openai import OpenAI

from .base_provider import BaseProvider

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


class OpenAIProvider(BaseProvider):

    def __init__(self):
        super().__init__("OpenAI")

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generar_imagen(self, prompt):

        respuesta = self.client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1536"
        )

        imagen = respuesta.data[0].b64_json

        carpeta = BASE_DIR.parent / "public" / "imagenes"
        carpeta.mkdir(parents=True, exist_ok=True)

        ruta = carpeta / "imagen_openai.png"

        with open(ruta, "wb") as f:
            f.write(base64.b64decode(imagen))

        return ruta

    def generar_texto(self, prompt):

        respuesta = self.client.responses.create(
            model="gpt-5",
            input=prompt
        )

        return respuesta.output_text