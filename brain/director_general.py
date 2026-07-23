from brain.director_comercial import DirectorComercial


class DirectorGeneral:

    def __init__(self):

        self.director_comercial = DirectorComercial()

    def iniciar_dia(self):

        print()
        print("=" * 60)
        print("🏛️ DIRECTOR GENERAL")
        print("=" * 60)

        print("Iniciando Consejo Ejecutivo...\n")

        resultado = self.director_comercial.ejecutar()

        return resultado["estrategia"]