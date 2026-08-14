"""
LEGALI BRAIN

Director Comercial IA
"""

from brain.commercial_intelligence import CommercialIntelligence


class DirectorComercial:

    def __init__(self):

        self.inteligencia = CommercialIntelligence()

    def analizar_negocio(self):

        print("📈 Analizando objetivos comerciales...")

        return {
            "objetivo": "Conseguir nuevos clientes",
            "prioridad": "Alta",
            "canal": "Instagram"
        }

    def solicitar_estrategia(self):

        print("🧠 Consultando Commercial Intelligence...\n")

        return self.inteligencia.generar_plan()

    def ejecutar(self):

        negocio = self.analizar_negocio()

        estrategia = self.solicitar_estrategia()

        return {

            "negocio": negocio,

            "estrategia": estrategia

        }