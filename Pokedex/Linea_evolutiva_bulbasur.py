from clase_Pokemon import Pokemon

class Bulbasaur(Pokemon):
    pokemon = 'Bulbasaur'
    tipo = ("planta", 'veneno')
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 105,
        "ataque": 79.5,
        "defensa": 79.5,
        "atq_esp": 95.5,
        "def_esp": 95.5,
        "velocidad": 75.5
    }
    # 'Movimiento': Nivel requerido
    lista_mov = {
        'Placaje':1,
        'Látigo cepa':3,
        'Hoja afilada':12,
        'Bomba germen':18,
        'Derribo':21
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):
        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def evolucion(self):
        if self.get_nivel() >= 16:
            confirmacion = None
            while (confirmacion != 'Si' or confirmacion != 'No'):
                confirmacion = input('¿Desea evolucionar a Wartortle? Si/No: ')
            if confirmacion == 'Si':
                return Ivysaur(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                  self.get_experiencia())
            else:
                return False
        else:
            return False

    def __str__(self):
        return super().__str__()


class Ivysaur(Pokemon):
    pokemon = 'Ivysaur'
    tipo = ("plata", 'veneno')
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 120,
        "ataque": 92.5,
        "defensa": 93.5,
        "atq esp": 110.5,
        "def esp": 110.5,
        "velocidad": 90.5
    }
    lista_mov = {
        'Placaje': 1,
        'Látigo cepa': 3,
        'Hoja afilada': 12,
        'Bomba germen': 18,
        'Derribo': 21,
        'Doble filo':33,
        'Rayo solar':36,
        'Bomba lodo':25
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):

        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def evolucion(self):
        if self.get_nivel() >= 36:
            confirmacion = None
            while (confirmacion != 'Si' or confirmacion != 'No'):
                confirmacion = input(f'¿Desea evolucionar a Blastoise? Si/No')
            if confirmacion == 'Si':
                return Venusaur(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                  self.get_experiencia())
            else:
                return False
        else:
            return False

    def __str__(self):
        return super().__str__()

class Venusaur(Pokemon):
    pokemon = 'Venasaur'
    tipo = ('planta', 'veneno')
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 140,
        "ataque": 112.5,
        "defensa": 113.5,
        "atq_esp": 130.5,
        "def_esp": 130.5,
        "velocidad": 110.5
    }
    lista_mov = {
        'Placaje': 1,
        'Látigo cepa': 3,
        'Hoja afilada': 12,
        'Bomba germen': 18,
        'Derribo': 21,
        'Doble filo': 33,
        'Rayo solar': 36,
        'Bomba lodo': 25,
        'Terremoto':40,
        'Energibola':38,
        'Hiperrayo':53,
        'Golpe cuerpo':38
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):

        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def evolucion(self):
        if self.get_nivel() >= 50:
            confirmacion = None
            while (confirmacion != 'Si' or confirmacion != 'No'):
                confirmacion = input(f'¿Desea evolucionar a Mega-Blastoise? Si/No')
            if confirmacion == 'Si':
                return Mega_Venasaur(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                 self.get_experiencia())
            else:
                return False
        else:
            return False

    def __str__(self):
        return super().__str__()


class Mega_Venasaur(Pokemon):
    pokemon = 'Mega-Venesaur'
    tipo = ('planta', 'veneno')
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 187,
        "ataque": 94,
        "defensa": 192,
        "atq_esp": 191,
        "def_esp": 189,
        "velocidad": 145
    }
    lista_mov = {
        'Placaje': 1,
        'Látigo cepa': 3,
        'Hoja afilada': 12,
        'Bomba germen': 18,
        'Derribo': 21,
        'Doble filo': 33,
        'Rayo solar': 36,
        'Bomba lodo': 25,
        'Terremoto': 40,
        'Energibola': 38,
        'Golpe cuerpo': 38,
        'Hiperrayo': 53,
        'Planta feroz':73,
        'Enfado':57
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):
        super().__init__(nivel, nombre, experiencia, movimientos_guardados)

    def __str__(self):
        return super().__str__()