import json
from pathlib import Path

from prompts import crear_prompt
from copywriter import generar_copy

BASE_DIR = Path(__file__).resolve().parent

TEMAS = BASE_DIR / "temas.json"
HISTORIAL = BASE_DIR / "historial.json"


def cargar_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


temas = cargar_json(TEMAS)
historial = cargar_json(HISTORIAL)

publicados = historial["publicados"]

tema = None

for servicio in temas:
    if servicio["id"] not in publicados:
        tema = servicio
        break

if tema is None:
    historial["publicados"] = []
    guardar_json(HISTORIAL, historial)
    tema = temas[0]

prompt = crear_prompt(tema)
copy = generar_copy(tema)

print("=" * 60)
print("🤖 LEGALI COMMUNITY IA")
print("=" * 60)

print(f"Servicio: {tema['titulo']}")
print(f"Precio: {tema['precio']}")
print(f"Descripción: {tema['descripcion']}")

print("\n" + "=" * 60)
print("PROMPT")
print("=" * 60)
print(prompt)

print("\n" + "=" * 60)
print("COPY PARA INSTAGRAM")
print("=" * 60)
print(copy)

historial["publicados"].append(tema["id"])
guardar_json(HISTORIAL, historial)

print("\n✅ Historial actualizado")