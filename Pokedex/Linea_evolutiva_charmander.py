from clase_Pokemon import Pokemon

class Charmander(Pokemon):
    pokemon = 'Charmander'
    tipo = ("fuego")
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 99,
        "ataque": 82.5,
        "defensa": 73.5,
        "atq_esp": 90.5,
        "def_esp": 80.5,
        "velocidad": 95.5
    }
    # 'Movimiento': Nivel requerido
    lista_mov = {
        "Arañazo": 1,
        "Ascuas": 4,
        "Garra metal": 13,
        "Dragoaliento": 12,
        "Colmillo igneo": 17,
        "Lanzallamas": 36
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):
        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def evolucion(self):
        if self.get_nivel() >= 16:
            confirmacion = None
            while (confirmacion != 'Si' or confirmacion != 'No'):
                confirmacion = input('¿Desea evolucionar a Charmeleon? Si/No: ')
            if confirmacion == 'Si':
                return Charmeleon(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                  self.get_experiencia())
            else:
                return False
        else:
            return False

    def __str__(self):
        return super().__str__()


class Charmeleon(Pokemon):
    pokemon = 'Charmeleon'
    tipo = ("fuego")
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 118,
        "ataque": 94.5,
        "defensa": 88.5,
        "atq_esp": 110.5,
        "def_esp": 95.5,
        "velocidad": 110.5
    }

    lista_mov = {
        "Arañazo": 1,
        "Ascuas": 4,
        "Garra metal": 13,
        "Dragoaliento": 12,
        "Colmillo igneo": 17,
        "Lanzallamas": 36,
        "Infierno": 48
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):

        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def evolucion(self):
        if self.get_nivel() >= 36:
            confirmacion = None
            while (confirmacion != 'Si' or confirmacion != 'No'):
                confirmacion = input(f'¿Desea evolucionar a Charizard? Si/No')
            if confirmacion == 'Si':
                return Charizard(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                  self.get_experiencia())
            else:
                return False
        else:
            return False

    def __str__(self):
        return super().__str__()


class Charizard(Pokemon):
    pokemon = 'Charizard'
    tipo = ("fuego", "volador")
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 138,
        "ataque": 114.5,
        "defensa": 108.5,
        "atq_esp": 139.5,
        "def_esp": 115.5,
        "velocidad": 130.5
    }
    lista_mov = {
        "Arañazo": 1,
        "Ascuas": 4,
        "Garra metal": 13,
        "Dragoaliento": 12,
        "Colmillo igneo": 17,
        "Lanzallamas": 36,
        "Infierno": 48,
        "Ataque ala": 36,
        "Tajo aereo": 64
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):
        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def evolucion(self):
        if self.get_nivel() >= 50:
            mega_evolucion = input("¿Cual mega-evolución deseas obtener? (X/Y):")

            if mega_evolucion == "X":
                print(f'{self.get_nombre()} ha evolucionado a Mega Charizard X')
                return Charizard_X(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                   self.get_experiencia())
            elif mega_evolucion == "Y":
                print(f'{self.get_nombre()} ha evolucionado a Mega Charizard Y')
                return Charizard_Y(self.get_nivel(), self.get_nombre(), self.get_movimientos_guardados(),
                                   self.get_experiencia())
            else:
                return False

    def __str__(self):
        return super().__str__()


class Charizard_X(Pokemon):
    pokemon = 'Charizard X'
    tipo = ("fuego", "dragón")
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 185,
        "ataque": 200,
        "defensa": 179,
        "atq_esp": 121,
        "def_esp": 150,
        "velocidad": 167
    }
    lista_mov = {
        "Arañazo": 1,
        "Ascuas": 4,
        "Garra metal": 13,
        "Dragoaliento": 12,
        "Colmillo igneo": 17,
        "Lanzallamas": 36,
        "Infierno": 48,
        "Ataque ala": 36,
        "Tajo aereo": 64,
        "Triturar": 1,
        "Garra dragón": 1,
        "Garra umbría": 1,
        "Cuchillada": 24,
        "Envite ígneo": 62
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):
        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def __str__(self):
        return super().__str__()

class Charizard_Y(Pokemon):
    pokemon = 'Charizard Y'
    tipo = ("fuego", "volador")
    tipo_experiencia = "Parabolico"
    atributos = {
        "ps": 185,
        "ataque": 98,
        "defensa": 143,
        "atq_esp": 232,
        "def_esp": 183,
        "velocidad": 167
    }
    lista_mov = {
        "Arañazo": 1,
        "Ascuas": 4,
        "Garra metal": 13,
        "Dragoaliento": 12,
        "Colmillo igneo": 17,
        "Lanzallamas": 36,
        "Infierno": 48,
        "Ataque ala": 36,
        "Tajo aereo": 64,
        "Onda ígnea": 71,
        "Pirotecnia": 32
    }

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):
        super().__init__(nivel, nombre, movimientos_guardados, experiencia)

    def __str__(self):
        return super().__str__()