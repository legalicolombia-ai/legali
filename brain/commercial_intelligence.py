from brain.decision_engine import DecisionEngine


class CommercialIntelligence:

    def __init__(self):

        self.engine = DecisionEngine()

    def generar_plan(self):

        return self.engine.ejecutar_reunion_consejo()