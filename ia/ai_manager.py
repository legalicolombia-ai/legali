class AIManager:
    def __init__(self, model_name="default"):
        self.model_name = model_name

    def generar_respuesta(self, prompt: str) -> str:
        return f"[AI Response] Procesado prompt: '{prompt}'"