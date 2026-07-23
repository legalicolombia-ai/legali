class ReelGenerator:
    def __init__(self):
        pass

    def generar_guion_reel(self, producto, segmento, etapa):
        """Genera la estructura de un video corto (Reel 9:16) optimizado para retención y conversión."""
        
        guiones_ejemplo = {
            "Asesoría Jurídica 24/7": {
                "gancho": f"¡Dueño de negocio! Si aún no tienes asesoría jurídica permanente, estás a una demanda de cerrar.",
                "problema": "Contratos mal redactados, despidos sin soporte legal o multas sorpresa que drenan el flujo de caja de tu empresa.",
                "solución": f"Con {producto} de Legali tienes respaldo profesional 24/7 para blindar tu patrimonio y tomar decisiones con total seguridad.",
                "cta": "Toca el link de la bio en @legali_co y agenda tu blindaje hoy mismo."
            },
            "Agente IA RRHH": {
                "gancho": f"Atención {segmento}: ¿Sigues gestionando contratos y permisos de personal de forma manual?",
                "problema": "Los errores humanos en recursos humanos generan sanciones laborales graves y pérdida de tiempo valioso.",
                "solución": f"Implementa el {producto}: automatiza la gestión de personal y cumple con toda la normatividad vigente al instante.",
                "cta": "Escribe 'RRHH' en los comentarios o toca el link de la bio en @legali_co."
            }
        }

        # Si el producto no está en el diccionario, usar una estructura general adaptada
        guion = guiones_ejemplo.get(producto, {
            "gancho": f"El error legal que le cuesta miles de dólares a las empresas en su crecimiento.",
            "problema": "La falta de prevención jurídica expone tu negocio a riesgos innecesarios.",
            "solución": f"Soluciona y previene cualquier contingencia con el respaldo estratégico de Legali.",
            "cta": "Toca el link de la bio en @legali_co para más información."
        })

        print("\n==================================================")
        print(f"🎬 [REEL IA] - GUION 9:16 CREADO ({producto})")
        print("==================================================")
        print(f"⏱️ 00:00 - 00:03 | GANCHO: {guion['gancho']}")
        print(f"⏱️ 00:03 - 00:15 | PROBLEMA: {guion['problema']}")
        print(f"⏱️ 00:15 - 00:30 | SOLUCIÓN: {guion['solución']}")
        print(f"⏱️ 00:30 - 00:45 | CTA: {guion['cta']}")
        print("==================================================\n")

        return guion

if __name__ == "__main__":
    gen = ReelGenerator()
    gen.generar_guion_reel("Asesoría Jurídica 24/7", "Dueños de Negocios", "Conversión")
