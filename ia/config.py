from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY:
    print("✅ API KEY ENCONTRADA")
    print("Primeros caracteres:", OPENAI_API_KEY[:12] + "...")
else:
    print("❌ NO SE ENCONTRÓ LA API KEY")