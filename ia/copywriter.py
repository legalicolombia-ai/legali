import random

def generar_copy(servicio):

    frases = [
        "La seguridad no puede esperar.",
        "Protege lo que más valoras.",
        "La tecnología también salva vidas.",
        "Un segundo puede cambiarlo todo.",
        "La tranquilidad comienza con una buena decisión."
    ]

    llamados = [
        "📲 Escríbenos hoy.",
        "💬 Solicita una demostración.",
        "✅ Activa tu servicio ahora.",
        "🚀 Contrata hoy mismo.",
        "⚖️ Habla con un asesor Legali."
    ]

    hashtags = [
        "#Legali",
        "#Seguridad",
        "#Colombia",
        "#Proteccion",
        "#Tecnologia",
        "#Innovacion",
        "#Empresas",
        "#Familia",
        "#BotonDePanico",
        "#AsesoriaJuridica"
    ]

    copy = f"""
🚀 {servicio['titulo']}

{random.choice(frases)}

💰 Desde {servicio['precio']}

{servicio['descripcion']}

{random.choice(llamados)}

{' '.join(random.sample(hashtags,5))}
"""

    return copy