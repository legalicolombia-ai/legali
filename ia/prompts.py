import random


def crear_prompt(servicio):

    enfoque = random.choice(servicio.get("enfoques", ["Publicidad profesional"]))

    return f"""
Diseña una imagen publicitaria para Instagram.

EMPRESA:
LEGALI

SERVICIO:
{servicio["titulo"]}

PRECIO:
{servicio["precio"]}

DESCRIPCIÓN:
{servicio["descripcion"]}

ENFOQUE DEL DÍA:
{enfoque}

Características:

• Muy elegante
• Tecnología
• Fondo premium
• Diseño minimalista
• Azul oscuro
• Blanco
• Dorado
• Estilo Apple
• Formato 1080x1350
• Espacio para el logo
• Botón "Contratar Ahora"

Debe parecer una campaña publicitaria de una empresa tecnológica líder.
"""