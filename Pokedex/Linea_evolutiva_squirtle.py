from clase_Pokemon import Pokemon

class Squirtle(Pokemon):
    pokemon = 'Squirtle'
    tipo = ("agua")
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 104,
        "ataque": 78.5,
        "defensa": 95.5,
        "atq_esp": 80.5,
        "def_esp": 94.5,
        "velocidad": 73.5
    }
    # 'Movimiento': Nivel requerido
    lista_mov = {
        'Placaje':1,
        'Burbuja':9,
        'Pistola agua':3,
        'Giro rápido':9,
        'Mordisco':12,
        'Hidropulso':15,
        'Acua cola':24,
        'Cabezazo':31,
        'Hidrobomba':33
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):
        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def evolucion(self):
        if self.get_nivel() >= 16:
            confirmacion = None
            while (confirmacion != 'Si' or confirmacion != 'No'):
                confirmacion = input('¿Desea evolucionar a Wartortle? Si/No: ')
            if confirmacion == 'Si':
                return Wartortle(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                  self.get_experiencia())
            else:
                return False
        else:
            return False
    def imprimir_nombre(self):
        print(type(self).__name__)

    def __str__(self):
        return super().__str__()


class Wartortle(Pokemon):
    pokemon = 'Wartortle'
    tipo = ("agua")
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 119,
        "ataque": 93.5,
        "defensa": 110.5,
        "atq_esp": 95.5,
        "def_esp": 110.5,
        "velocidad": 88.5
    }
    lista_mov = {
        'Placaje': 1,
        'Burbuja': 9,
        'Pistola agua': 3,
        'Giro rápido': 9,
        'Mordisco': 12,
        'Hidropulso': 15,
        'Acua cola': 24,
        'Cabezazo': 31,
        'Hidrobomba': 33
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):

        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def evolucion(self):
        if self.get_nivel() >= 36:
            confirmacion = None
            while (confirmacion != 'Si' or confirmacion != 'No'):
                confirmacion = input(f'¿Desea evolucionar a Blastoise? Si/No')
            if confirmacion == 'Si':
                return Blastoise(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                  self.get_experiencia())
            else:
                return False
        else:
            return False

    def __str__(self):
        return super().__str__()


class Blastoise(Pokemon):
    pokemon = 'Blastoise'
    tipo = ('agua')
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 139,
        "ataque": 113.5,
        "defensa": 130.5,
        "atq_esp": 115.5,
        "def_esp": 135.5,
        "velocidad": 108.5
    }
    lista_mov = {
        'Placaje': 1,
        'Burbuja': 9,
        'Pistola agua': 3,
        'Giro rápido': 9,
        'Mordisco': 12,
        'Hidropulso': 15,
        'Acua cola': 24,
        'Cabezazo': 31,
        'Hidrobomba': 33,
        'Excavar':38,
        'Rayo hielo': 45,
        'Pulso drágon': 62
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):

        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def evolucion(self):
        if self.get_nivel() >= 50:
            confirmacion = None
            while (confirmacion != 'Si' or confirmacion != 'No'):
                confirmacion = input(f'¿Desea evolucionar a Mega-Blastoise? Si/No')
            if confirmacion == 'Si':
                return Mega_Blastoise(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                 self.get_experiencia())
            else:
                return False
        else:
            return False

    def __str__(self):
        return super().__str__()


class Mega_Blastoise(Pokemon):
    pokemon = 'Mega-Blastoise'
    tipo = ('agua')
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 186,
        "ataque": 97,
        "defensa": 189,
        "atq_esp": 205,
        "def_esp": 183,
        "velocidad": 143
    }
    lista_mov = {
        'Placaje': 1,
        'Burbuja': 9,
        'Pistola agua': 3,
        'Giro rápido': 9,
        'Mordisco': 12,
        'Hidropulso': 15,
        'Acua cola': 24,
        'Cabezazo': 31,
        'Hidrobomba': 33,
        'Excavar': 38,
        'Rayo hielo': 45,
        'Pulso drágon': 62,
        'Foco resplandor': 53,
        'Esfera aural': 60,
        'Ventisca': 70,
        'Metereobola': 51
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):
        super().__init__(nivel, nombre, experiencia, movimientos_guardados)

    def __str__(self):
        return super().__str__()