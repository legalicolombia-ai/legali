from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
import os
import base64

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generar_imagen(prompt, nombre_archivo):

    print("🎨 Generando imagen...")

    resultado = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1536"
    )

    imagen_base64 = resultado.data[0].b64_json

    carpeta = BASE_DIR.parent / "public" / "imagenes"
    carpeta.mkdir(parents=True, exist_ok=True)

    ruta = carpeta / nombre_archivo

    with open(ruta, "wb") as f:
        f.write(base64.b64decode(imagen_base64))

    print(f"✅ Imagen guardada en:\n{ruta}")

    return ruta