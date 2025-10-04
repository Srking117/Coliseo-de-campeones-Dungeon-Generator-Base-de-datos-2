from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED, DOUBLE
from rich.columns import Columns
from .mapa import Mapa
from .explorador import Explorador

class Visualizador:
    def __init__(self):
        self.console = Console()
    
    def mostrar_mapa_completo(self, mapa: Mapa, explorador: Explorador):
        """Muestra el mapa completo con diseño mejorado"""
        # Crear tabla principal
        grid = Table(
            show_header=False, 
            show_lines=True, 
            box=DOUBLE,
            padding=(0, 1),
            title="COLISEO DE CAMPEONES - MAPA COMPLETO",
            title_style="bold gold1",
            border_style="bright_white"
        )
        
        # Crear columnas con encabezados de coordenadas X
        for x in range(mapa.ancho):
            grid.add_column(f"{x}", width=4, justify="center")
        
        # Llenar grid con coordenadas Y
        for y in range(mapa.alto):
            row_cells = []
            for x in range(mapa.ancho):
                habitacion = mapa.obtener_habitacion_por_coordenadas(x, y)
                
                if habitacion:
                    # Determinar símbolo y color según el contenido
                    if (x, y) == explorador.posicion_actual:
                        simbolo = "X"
                        color = "bold red"
                    elif habitacion.inicial:
                        simbolo = "I"
                        color = "bold green"
                    elif habitacion.contenido:
                        if habitacion.contenido.tipo == "jefe":
                            simbolo = "J"
                            color = "bold yellow"
                        elif habitacion.contenido.tipo == "monstruo":
                            simbolo = "M"
                            color = "bold magenta"
                        elif habitacion.contenido.tipo == "tesoro":
                            simbolo = "T"
                            color = "bold cyan"
                        elif habitacion.contenido.tipo == "evento":
                            simbolo = "E"
                            color = "bold blue"
                        else:
                            simbolo = "·"
                            color = "white"
                    else:
                        simbolo = "·"
                        color = "white" if habitacion.visitada else "dim white"
                    
                    # Crear celda
                    cell_text = Text(simbolo, style=color)
                    cell_text.append(f"\n({x},{y})", style="dim")
                    row_cells.append(cell_text)
                else:
                    row_cells.append(Text(" ", style="black"))
            
            # CORREGIDO: Eliminar el style problemático
            grid.add_row(*row_cells)
        
        # Panel con leyenda
        leyenda = Table(show_header=True, box=ROUNDED, title="LEYENDA")
        leyenda.add_column("Símbolo", style="bold")
        leyenda.add_column("Significado", style="white")
        
        leyenda_data = [
            ("X", "Tu posición actual"),
            ("I", "Entrada del Coliseo"),
            ("J", "Jefe Final"),
            ("M", "Monstruo"),
            ("T", "Tesoro"),
            ("E", "Evento Especial"),
            ("·", "Habitación normal"),
            ("?", "No explorado")
        ]
        
        for simbolo, significado in leyenda_data:
            leyenda.add_row(simbolo, significado)
        
        # Mostrar en columnas
        contenido = Columns([grid, leyenda], expand=True)
        self.console.print(Panel(contenido, border_style="gold1"))
    
    def mostrar_habitacion_actual(self, explorador: Explorador):
        """Muestra descripción detallada de la habitación actual"""
        habitacion = explorador.mapa.obtener_habitacion_por_coordenadas(*explorador.posicion_actual)
        
        if not habitacion:
            return
        
        # Crear panel principal de habitación
        contenido_habitacion = []
        
        # Coordenadas y estado
        estado_table = Table(show_header=False, box=ROUNDED)
        estado_table.add_column("", style="cyan", width=15)
        estado_table.add_column("", style="white")
        
        estado_table.add_row("Posición", f"[{habitacion.x}, {habitacion.y}]")
        estado_table.add_row("Tipo", "ENTRADA PRINCIPAL" if habitacion.inicial else "ARENA DE COMBATE")
        estado_table.add_row("Estado", "EXPLORADA" if habitacion.visitada else "INEXPLORADA")
        
        contenido_habitacion.append(estado_table)
        
        # Contenido de la habitación
        if habitacion.contenido:
            contenido_panel = Panel(
                f"{habitacion.contenido.descripcion}",
                title="CONTENIDO DETECTADO",
                border_style="red" if habitacion.contenido.tipo in ["monstruo", "jefe"] else "yellow"
            )
            contenido_habitacion.append(contenido_panel)
        else:
            contenido_habitacion.append(
                Panel("ESTA ARENA ESTA VACIA", border_style="dim")
            )
        
        # Conexiones disponibles
        conexiones = habitacion.obtener_direcciones_disponibles()
        if conexiones:
            direcciones_text = " | ".join([f"=> {dir.upper()}" for dir in conexiones])
            conexiones_panel = Panel(
                direcciones_text,
                title="RUTAS DISPONIBLES",
                border_style="green"
            )
        else:
            conexiones_panel = Panel(
                "SIN SALIDAS - ARENA CERRADA",
                border_style="red"
            )
        
        contenido_habitacion.append(conexiones_panel)
        
        # Mostrar todo en un panel principal
        self.console.print(
            Panel(
                "\n\n".join([str(item) for item in contenido_habitacion]),
                title="ARENA ACTUAL DEL COLISEO",
                border_style="bold cyan",
                padding=(1, 2)
            )
        )
    
    def mostrar_minimapa(self, mapa: Mapa, explorador: Explorador):
        """Minimapa compacto y estilizado"""
        # Crear grid compacto
        grid = Table(
            show_header=True,
            show_lines=True,
            box=ROUNDED,
            header_style="bold gold1",
            title="VISTA RAPIDA DEL COLISEO"
        )
        
        # Añadir encabezados de columnas
        grid.add_column("Y\\X", style="bold cyan", justify="center")
        for x in range(mapa.ancho):
            grid.add_column(str(x), justify="center", width=3)
        
        # Llenar filas
        for y in range(mapa.alto):
            row_cells = [Text(str(y), style="bold cyan")]
            for x in range(mapa.ancho):
                habitacion = mapa.obtener_habitacion_por_coordenadas(x, y)
                
                if habitacion and habitacion.visitada:
                    if (x, y) == explorador.posicion_actual:
                        cell = Text("P", style="bold red")
                    elif habitacion.inicial:
                        cell = Text("E", style="bold green")
                    elif habitacion.contenido:
                        tipo = habitacion.contenido.tipo
                        if tipo == "jefe": cell = Text("J", style="bold yellow")
                        elif tipo == "monstruo": cell = Text("M", style="bold magenta")
                        elif tipo == "tesoro": cell = Text("T", style="bold cyan")
                        elif tipo == "evento": cell = Text("V", style="bold blue")
                        else: cell = Text("·", style="white")
                    else:
                        cell = Text("·", style="dim white")
                else:
                    cell = Text(" ", style="dim black")
                
                row_cells.append(cell)
            
            grid.add_row(*row_cells)
        
        # Leyenda del minimapa
        leyenda_mini = Table(show_header=False, box=ROUNDED)
        leyenda_mini.add_column("Clave", style="bold")
        leyenda_mini.add_column("Significado", style="white")
        
        claves = [
            ("P", "Tu posición"),
            ("E", "Entrada"),
            ("J", "Jefe"),
            ("M", "Monstruo"),
            ("T", "Tesoro"),
            ("V", "Evento"),
            ("·", "Explorado")
        ]
        
        for clave, significado in claves:
            leyenda_mini.add_row(clave, significado)
        
        # Combinar grid y leyenda
        contenido = Columns([grid, leyenda_mini])
        self.console.print(Panel(contenido, border_style="blue"))
    
    def mostrar_estado_explorador(self, explorador: Explorador):
        """Panel de estado del gladiador mejorado"""
        # Barra de vida visual
        vida_porcentaje = (explorador.vida / explorador.vida_maxima) * 100
        if vida_porcentaje > 70:
            vida_color = "green"
            estado = "EN PLENA FORMA"
        elif vida_porcentaje > 30:
            vida_color = "yellow"
            estado = "HERIDO LEVE"
        else:
            vida_color = "red"
            estado = "GRAVEMENTE HERIDO"
        
        barra_vida = "█" * explorador.vida + "░" * (explorador.vida_maxima - explorador.vida)
        
        # Panel de vida
        vida_panel = Panel(
            f"{barra_vida}\n"
            f"Vida: {explorador.vida}/{explorador.vida_maxima} HP\n"
            f"Estado: {estado}",
            title="ESTADO FISICO",
            border_style=vida_color
        )
        
        # Panel de inventario mejorado
        if explorador.inventario:
            inventario_items = []
            for obj in explorador.inventario:
                valor_color = "green" if obj.valor > 100 else "yellow" if obj.valor > 50 else "white"
                inventario_items.append(f"• {obj.nombre} [bold {valor_color}]({obj.valor} pts)[/]")
            inventario_text = "\n".join(inventario_items)
            titulo_inventario = f"INVENTARIO ({len(explorador.inventario)} objetos)"
        else:
            inventario_text = "Mochila vacia"
            titulo_inventario = "INVENTARIO"
        
        inventario_panel = Panel(
            inventario_text,
            title=titulo_inventario,
            border_style="yellow"
        )
        
        # Panel de posición y estadísticas
        habitacion_actual = explorador.mapa.obtener_habitacion_por_coordenadas(*explorador.posicion_actual)
        stats_text = f"Posicion: {explorador.posicion_actual}\n"
        
        if habitacion_actual:
            distancia = abs(habitacion_actual.x - explorador.mapa.habitacion_inicial.x) + \
                       abs(habitacion_actual.y - explorador.mapa.habitacion_inicial.y)
            stats_text += f"Distancia desde entrada: {distancia} pasos\n"
        
        stats_text += f"Bonificacion combate: {explorador.bonificacion_combate} arenas" if explorador.bonificacion_combate > 0 else "Sin bonificaciones activas"
        
        stats_panel = Panel(
            stats_text,
            title="ESTADISTICAS",
            border_style="cyan"
        )
        
        # Mostrar en layout de 2x2
        layout_table = Table(show_header=False, box=None)
        layout_table.add_column()
        layout_table.add_column()
        
        layout_table.add_row(vida_panel, inventario_panel)
        layout_table.add_row(stats_panel, "")
        
        self.console.print(
            Panel(
                layout_table,
                title="GLADIADOR: NOBLE SIX",
                border_style="bold gold1",
                padding=(1, 1)
            )
        )
