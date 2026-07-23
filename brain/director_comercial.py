"""
LEGALI BRAIN

Director Comercial IA

Responsabilidad:

- Analizar el negocio.
- Priorizar servicios.
- Solicitar la mejor estrategia comercial.

Nunca genera imágenes.
Nunca publica.

"""

from brain.decision_engine import DecisionEngine


class DirectorComercial:

    def __init__(self):

        self.engine = DecisionEngine()

    def analizar_negocio(self):

        print("📈 Analizando objetivos comerciales...")

        return {
            "objetivo": "Conseguir nuevos clientes",
            "prioridad": "Alta",
            "canal": "Instagram"
        }

    def solicitar_estrategia(self):

        print("🧠 Consultando Decision Engine...\n")

        estrategia = self.engine.ejecutar_reunion_consejo()

        return estrategia

    def ejecutar(self):

        negocio = self.analizar_negocio()

        estrategia = self.solicitar_estrategia()

        return {

            "negocio": negocio,

            "estrategia": estrategia

        }