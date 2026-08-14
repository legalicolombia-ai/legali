from brain.director_general import DirectorGeneral
import sys
import os
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ai.manager import AIManager
from ai.reel_generator import ReelGenerator
from brain.commercial_intelligence import CommercialIntelligence
from marketing.visual_generator import VisualGenerator
from marketing.publisher import AIPublisher
from data.memory_manager import MemoryManager
from data.analyst import AIAnalyst

def main():
    print("==================================================")
    print("      🏛️  LEGALI MARKETING AI - SISTEMA INTEGRADO ")
    print("==================================================\n")
    
    # 1. ANALISTA IA: Métricas y sugerencias
    analista = AIAnalyst()
    reporte_analista = analista.analizar_rendimiento_reciente()
    print(f"📊 [ANALISTA IA]: {reporte_analista['diagnostico']}")
    print(f"💡 [RECOMENDACIÓN]: {reporte_analista['recomendacion_consejo']}\n")

    # 2. DIRECTOR COMERCIAL: IOC y embudo
    director = DirectorGeneral()
    estrategia = director.iniciar_dia()
    
    prod = estrategia['producto']
    etapa = estrategia['etapa']
    segmento = estrategia['segmento']
    cta = estrategia['cta_recomendado']

    # 3. SELECCIÓN DE FORMATO (Carrusel Gráfico o Reel 9:16)
    formato_elegido = random.choice(["carrusel", "reel"])
    print(f"🎯 [ESTRATEGIA DE CONTENIDO]: Formato seleccionado para este ciclo -> {formato_elegido.upper()}\n")

    memoria = MemoryManager()

    if formato_elegido == "reel":
        # Generar Guion para Reel
        reel_gen = ReelGenerator()
        guion = reel_gen.generar_guion_reel(prod, segmento, etapa)
        
        # Registrar en Memoria
        memoria.registrar_publicacion(
            enfoque=etapa,
            accion=f"Reel 9:16 - {prod} (IOC: {estrategia['ioc_score']})",
            copy_generado=guion['gancho'] + "\n\n" + guion['solución'] + "\n\n" + guion['cta'],
            rutas_imagenes=[]
        )
        print("✅ [ÉXITO TOTAL]: Guion de Reel 9:16 generado y registrado para @legali_co.")

    else:
        # Generar Copywriter IA
        ai = AIManager()
        resultado_copy = ai.generar_copy_carrusel(
            producto=prod,
            etapa=etapa,
            segmento=segmento,
            cta=cta
        )

        # Generador Visual (Diseñador IA)
        slides = [
            {
                "titulo": f"¿Tu empresa está protegida con {prod}?",
                "contenido": f"Solución especialmente pensada para {segmento}. Evita contingencias este año."
            },
            {
                "titulo": "1. Diagnóstico Preventivo",
                "contenido": "Auditamos contratos y procesos para blindar tu operación frente a sanciones o demandas."
            },
            {
                "titulo": "2. Respuesta y Soporte IA",
                "contenido": "Tecnología jurídica en tiempo real para resolver dudas y gestionar reclamos al instante."
            },
            {
                "titulo": "3. Tranquilidad Operativa",
                "contenido": "Convierte el cumplimiento legal en una ventaja competitiva para escalar tu negocio sin riesgos."
            },
            {
                "titulo": "Blindaje Inmediato LEGALI",
                "contenido": cta
            }
        ]

        print("🎨 [DISEÑADOR IA]: Generando diapositivas en Descargas para @legali_co...")
        
        # Redirigir la salida directamente a C:\Users\HP\Downloads\legali_carrusel
        output_dir = os.path.join(os.path.expanduser("~"), "Downloads", "legali_carrusel")
        os.makedirs(output_dir, exist_ok=True)
        
        visual = VisualGenerator()
        visual.output_dir = output_dir  # Forzar el directorio de destino
        rutas_imagenes = visual.generar_carrusel_completo(slides)
        
        # Registrar en Memoria
        memoria.registrar_publicacion(
            enfoque=etapa,
            accion=f"Carrusel - {prod} (IOC: {estrategia['ioc_score']})",
            copy_generado=resultado_copy,
            rutas_imagenes=rutas_imagenes
        )

        # Publicador IA (Nube / Meta)
        publicador = AIPublisher()
        publicador.ejecutar_publicacion_carrusel(rutas_imagenes, resultado_copy)

        print(f"\n✅ [ÉXITO TOTAL]: Carrusel guardado en {output_dir} y procesado para @legali_co.")

if __name__ == "__main__":
    main()
