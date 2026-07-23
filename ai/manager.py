import json

class AIManager:
    def __init__(self):
        pass

    def generar_copy_carrusel(self, producto, etapa, segmento, cta):
        """Simula la generación de copy estructurado alineado al embudo y la audiencia."""
        
        hooks = {
            "Descubrimiento": f"🚨 ¿Cometiendo este error en tu empresa sin saberlo? ({segmento})",
            "Educación / Autoridad": f"💡 Cómo blindar legalmente tu operación con {producto}",
            "Conversión": f"🛡️ Protege tu Pyme hoy mismo con {producto}"
        }
        
        hook = hooks.get(etapa, f"Atención {segmento}")

        copy_resultado = f"""{hook}

El 80% de los problemas jurídicos en empresas surgen por no tener protocolos claros de prevención o tecnología de respuesta rápida.

En Legali transformamos la protección legal de tu negocio:
✅ Respuestas en tiempo real.
✅ Cumplimiento normativo automatizado.
✅ Tranquilidad para dueños y equipos de trabajo.

---
{cta}
#Legali #LegalTech #PymesColombia #ProteccionEmpresarial #AgenteIA
"""
        return copy_resultado
