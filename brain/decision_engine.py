import json
from pathlib import Path


class DecisionEngine:
    """
    Cerebro Comercial de LEGALI BRAIN

    Su única responsabilidad es decidir qué servicio
    debe promocionarse hoy.
    """

    def __init__(self):

        self.base_dir = Path(__file__).resolve().parent.parent

        self.servicios_path = self.base_dir / "data" / "servicios.json"
        self.objetivos_path = self.base_dir / "data" / "objetivos.json"
        self.historial_path = self.base_dir / "data" / "historial.json"

        self.servicios = self.cargar_servicios()
        self.objetivos = self.cargar_objetivos()
        self.historial = self.cargar_historial()

    # ----------------------------------------------------

    def cargar_servicios(self):

        with open(self.servicios_path, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    # ----------------------------------------------------

    def cargar_objetivos(self):

        with open(self.objetivos_path, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    # ----------------------------------------------------

    def cargar_historial(self):

        if not self.historial_path.exists():
            return []

        with open(self.historial_path, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    # ----------------------------------------------------

    def dias_sin_publicar(self, nombre_servicio):

        dias = 30

        historial = list(reversed(self.historial))

        for indice, publicacion in enumerate(historial):

            if publicacion.get("producto") == nombre_servicio:
                dias = indice + 1
                break

        return dias

    # ----------------------------------------------------

    def calcular_ioc(self, servicio):

        prioridad = servicio.get("prioridad", 50)

        rentabilidad = servicio.get("rentabilidad", 50)

        dias = self.dias_sin_publicar(servicio["nombre"])

        score = (

            prioridad * 0.40 +

            rentabilidad * 0.40 +

            min(dias, 30) * (20 / 30)

        )

        return round(score, 2)

    # ----------------------------------------------------

    def ranking_servicios(self):

        ranking = []

        for servicio in self.servicios:

            ranking.append({

                "servicio": servicio,

                "ioc": self.calcular_ioc(servicio)

            })

        ranking.sort(

            key=lambda x: x["ioc"],

            reverse=True

        )

        return ranking

    # ----------------------------------------------------

    def etapa_embudo(self):

        total = len(self.historial)

        if total < 2:
            return "Descubrimiento"

        ultimos = self.historial[-2:]

        conversiones = 0

        for p in ultimos:

            if p.get("tipo_contenido") == "conversion":
                conversiones += 1

        if conversiones == 0:

            return "Conversión"

        if total % 2 == 0:

            return "Educación"

        return "Descubrimiento"

    # ----------------------------------------------------

    def obtener_cta(self, etapa):

        return self.objetivos["cta"][etapa.lower()]

    # ----------------------------------------------------

    def ejecutar_reunion_consejo(self):

        ranking = self.ranking_servicios()

        ganador = ranking[0]

        servicio = ganador["servicio"]

        etapa = self.etapa_embudo()

        return {

            "producto": servicio["nombre"],

            "ioc_score": ganador["ioc"],

            "segmento": servicio["segmento"],

            "etapa": etapa,

            "cta_recomendado": self.obtener_cta(etapa),

            "ranking": ranking

        }