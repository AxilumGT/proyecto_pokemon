def diccionario_movimientos(movimiento):
    # Nombre:[Potencia, precision, pp, elemento, tipo(atq/atq esp/especial), efecto, probabilidad del efecto en %
    # Modalidades efecto, probabilidad del efecto (Proximamente)
    lista = {
        "Arañazo": [40, 100, 35, "normal", "atq", None, None],
        'Placaje': [40, 100, 35, 'normal', 'atq', None, None],
        "Pistola de agua": [40, 100, 25, "agua", "atq esp", None, None],
        "Ascuas": [40, 100, 25, "fuego", "atq esp", 'quemar', 10],
        "Latigo cepa": [40, 100, 25, "planta", "atq", None, None],
        'Burbuja': [40, 100, 25, 'agua', 'atq esp', None, None],
        'Hoja mágica': [60, 1000, 20, 'planta', 'atq esp'],
        'Hoja afilada': [55, 95, 25, 'planta', 'atq'],
        'Bomba germen': [80, 100, 15, 'planta', 'atq', None, None],
        'Derribo': [90, 85, 20, 'normal', 'atq', 'reducir ps propios segun daño', 0.25],
        'Doble filo': [120, 100, 20, 'normal', 'atq', 'reducir ps propios segun ps reducidos del oponente', 0.333],
        'Rayo solar': [120, 100, 10, 'planta', 'atq esp', 'esperar con condicion', 1],
        'Bomba lodo': [90, 100, 10, 'veneno', 'atq esp', 'envenenar', 30],
        'Terremoto': [100, 100, 10, 'tierra', 'atq', None, None],
        'Energibola': [90, 100, 10, 'planta', 'bajar def esp un nivel', 10],
        'Golpe cuerpo': [85, 100, 15, 'normal', 'paralizar', 30],
        'Hiperrayo': [150, 90, 5, 'normal', 'atq esp', 'acierta y espera', 1],
        'Planta feroz': [150, 90, 5, 'planta', 'atq esp', 'acierta y espera', 1],
        'Enfado': [120, 100, 5, 'dragón', 'atq', 'fijo con confusión', 3],
        "Garra metal": [50, 95, 35, 'metal', 'atq', 'aumenta ataque un nivel', 10],
        "Dragoaliento": [60, 100, 20, 'dragón', 'atq esp', 'paralizar', 30],
        "Onda ígnea": [95, 90, 10, 'fuego', 'atq esp', 'quemar', 10],
        "Pirotecnia": [70, 100, 15, 'fuego', 'atq esp', None, None],
        'Pistola agua': [40, 100, 25, 'agua', 'atq esp', None, None],
        'Giro rápido': [50, 100, 40, 'normal', 'atq', 'aumenta velocidad un nivel', 100],
        'Mordisco': [60, 100, 25, 'siniestro', 'atq', 'retroceder', 30],
        'Hidropulso': [60, 100, 20, 'agua', 'atq esp', 'confundir', 20],
        'Acua cola': [90, 90, 10, 'agua', 'atq', None, None],
        'Cabezazo': [130, 100, 10, 'normal', 'atq', 'esperar con condicion', 1],
        'Hidrobomba': [110, 80, 5, 'agua', 'atq esp', None, None],
        'Excavar': [80, 100, 10, 'tierra', 'atq', 'esperar y no seleccionable', 1],
        'Rayo hielo': [90, 100, 10, 'hielo', 'atq esp', 'congelar', 10],
        'Pulso dragón': [85, 100, 10, 'dragón', 'atq esp', None, None],
        'Foco resplandor': [80, 100, 10, 'acero', 'atq esp', 'bajar def esp un nivel', 10],
        'Esfera aural': [80, 1000, 20, 'lucha', 'atq esp', None, None],
        'Ventisca': [110, 70, 5, 'hielo', 'atq esp', 'congelar', 10],
        "Colmillo igneo": [65, 95, 15, 'fuego', 'atq', 'quemar o retroceder', 10],
        "Lanzallamas": [90, 100, 15, 'fuego', 'atq esp', 'quemar', 10],
        "Infierno": [100, 50, 5, 'fuego', 'quemar', 100],
        "Ataque ala": [60, 100, 35, 'volador', 'atq', None, None],
        "Tajo aéreo": [75, 95, 15, 'volador', 'atq', 'retroceder', 30],
        "Triturar": [80, 100, 15, 'siniestro', 'atq', 'bajar defensa un nivel', 20],
        "Garra dragón": [80, 100, 15, 'dragón', 'atq', None, None],
        "Garra umbría": [70, 100, 15, 'fantasma', 'atq', None, None],
        "Cuchillada": [70, 100, 20, 'normal', 'atq', 'aumento golpe critico', 12.5],
        "Envite ígneo": [120, 100, 15, 'fuego', 'atq', ['quemar', 'reducir ps propios segun ps reducidos del oponente'],
                         [10, 0.333]]
    }
    if movimiento in lista:
        movimiento = lista[movimiento]
        return movimiento
    else:
        print('El movimiento no existe')
        return False
