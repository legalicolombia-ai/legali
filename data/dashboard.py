import json
import os
from brain.decision_engine import DecisionEngine

class CommercialDashboard:
    def __init__(self, history_filepath="data/historial.json"):
        self.history_filepath = history_filepath
        self.engine = DecisionEngine(history_filepath=history_filepath)

    def _cargar_historial(self):
        if not os.path.exists(self.history_filepath):
            return []
        try:
            with open(self.history_filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def mostrar_panel_control(self):
        historial = self._cargar_historial()
        
        # Obtener selección actual y cálculo de IOCs
        estrategia = self.engine.ejecutar_reunion_consejo()
        
        print("\n==================================================================")
        print("          📊 LEGALI MARKETING AI - DASHBOARD COMERCIAL (IOC)      ")
        print("==================================================================")
        print(f" Total Publicaciones Registradas: {len(historial)}")
        print(f" Marca Oficial: @legali_co")
        print("------------------------------------------------------------------")
        print(" 🎯 PRÓXIMA ACCIÓN COMERCIAL RECOMENDADA:")
        print(f"   ► Producto Ganador: {estrategia['producto']}")
        print(f"   ► Etapa del Embudo: {estrategia['etapa']}")
        print(f"   ► Segmento Objetivo: {estrategia['segmento']}")
        print(f"   ► Call To Action (CTA): {estrategia['cta_recomendado']}")
        print("------------------------------------------------------------------")
        
        # Mostrar barra de progreso visual para el IOC de cada servicio
        print(" 📈 ÍNDICE DE OPORTUNIDAD COMERCIAL (IOC) POR SERVICIO:")
        for prod, datos in self.engine.productos.items():
            # Buscar días desde la última publicación
            dias = 25
            for i, p in enumerate(reversed(historial)):
                if p.get("producto") == prod or prod in p.get("accion", ""):
                    dias = i + 1
                    break
            
            score = self.engine.calcular_ioc(prod, dias)
            
            # Generar barra gráfica en terminal
            bar_length = 20
            filled_length = int(bar_length * score // 100)
            bar = "█" * filled_length + "░" * (bar_length - filled_length)
            
            marca_ganador = " ◄ [SELECCIONADO]" if prod == estrategia['producto'] else ""
            print(f"   • {prod:<26} |{bar}| {score:>5.1f}/100 {marca_ganador}")

        print("==================================================================\n")

if __name__ == "__main__":
    dashboard = CommercialDashboard()
    dashboard.mostrar_panel_control()
