from Lista_de_movimientos import diccionario_movimientos

class Pokemon():
    # Ejemplos para los distintos pokemon
    pokemon = 'Pokémon'
    tipo = None
    tipo_experiencia = 'Rapido'
    atributos = None
    lista_mov = None

    def __init__(self, nivel, nombre, movimientos_guardados, experiencia):
        self.__nivel = nivel
        self.__nombre = nombre
        self.__movimientos_guardados = movimientos_guardados
        # Sirve para obtener la experiencia con respecto al nivel
        seleccionar_nivel = self.lista_experiencia()
        if (experiencia >= seleccionar_nivel[self.__nivel - 1] and experiencia < seleccionar_nivel[self.__nivel]):
            self.__experiencia = experiencia
        else:
            self.__experiencia = seleccionar_nivel[self.__nivel - 1]

    def get_nivel(self):
        return self.__nivel

    def set_nivel(self, nivel):
        self.__nivel = nivel

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
        return self.__nombre

    def get_movimientos_guardados(self):
        return self.__movimientos_guardados

    def set_movimientos_guardados(self, movimientos_guardados):
        self.__movimientos_guardados = movimientos_guardados

    def get_experiencia(self):
        return self.__experiencia

    def set_experiencia(self, experiencia):
        self.__experiencia = experiencia

    # Funcionan cuando ya se ha creado un pokémon como tal Ejm: Charmander

    def calcular_atributos(self):
        # Función que calcula los atributos debidos del pokemon según su nivel
        nuevos_valores = []
        valores = list(self.atributos.values())
        print(valores)

        for valor in valores:
            nuevo_valor = valor * self.get_nivel / 50
            nuevos_valores.append(nuevo_valor)
        # [0,1,2,3,4,5]
        # [PS, Ataque, Defensa, Ataque especial, Defensa especial, Velocidad]
        return nuevos_valores

    def aprender(self, nuevo_movimiento):
        '''El pokemon aprende cierto movimiento y verifica si esta en la lista de movimientos
        correspondientes para aprender'''
        verificador = False
        if nuevo_movimiento not in self.get_movimientos_guardados() and diccionario_movimientos(
                nuevo_movimiento) is not False:

            if len(self.get_movimientos_guardados()) < 4:
                movimientos = self.get_movimientos_guardados()
                movimientos.append(nuevo_movimiento)
                print(f'Se ha aprendido: {nuevo_movimiento}')
                self.set_movimientos_guardados(movimientos)

            elif len(self.get_movimientos_guardados()) == 4:
                while verificador == False:
                    print(self.get_movimientos_guardados())
                    print("Con el valor 0, no se aprende el movimiento")
                    n = int(input("¿Cual movimiento desea modificar por " + nuevo_movimiento + " (1/2/3/4)?:"))
                    if n in range(1, 5):
                        movimientos = self.get_movimientos_guardados()
                        movimientos[n - 1] = nuevo_movimiento
                        self.set_movimientos_guardados(movimientos)
                    elif n == 0:
                        print("El movimiento no se ha aprendido")
    def evaluar_movimientos(self):
        # Evalua si hay un movimiento por aprender de una lista
        # Condicion de nivel: Nivel requerido para aprender cierto movimiento
        for condicion_de_nivel in range(self.get_nivel() + 1):
            if condicion_de_nivel in self.lista_mov.values() and self.get_nivel() <= (self.lista_mov.values() + 7):
                # Extraer llave a traves del valor
                nuevo_movimiento = list(self.lista_mov.keys())[list(self.lista_mov.values()).index(condicion_de_nivel)]
                self.aprender(nuevo_movimiento)

    @classmethod
    def lista_experiencia(cls):

        lista_de_experencia = []
        if (cls.tipo_experiencia == "Rapido"):
            for i in range(1, 101):
                lista_de_experencia.append(0.8 * pow(i, 3))
                lista_de_experencia[i - 1] = int(float(lista_de_experencia[i - 1]))

            return lista_de_experencia

        elif (cls.tipo_experiencia == "Lento"):
            for i in range(1, 101):
                lista_de_experencia.append(5 * pow(i, 3) / 4)
                lista_de_experencia[i - 1] = int(float(lista_de_experencia[i - 1]))

            return lista_de_experencia

        elif (cls.tipo_experiencia == "Normal"):
            for i in range(1, 101):
                lista_de_experencia.append(pow(i, 3))
                lista_de_experencia[i - 1] = int(float(lista_de_experencia[i - 1]))

            return lista_de_experencia

        elif (cls.tipo_experiencia == "Parabolico"):
            for i in range(1, 101):
                lista_de_experencia.append((6 * pow(i, 3) / 5) - 15 * pow(i, 2) + 100 * i - 140)
                lista_de_experencia[i - 1] = int(float(lista_de_experencia[i - 1]))

            return lista_de_experencia

        else:
            print("Error: tipo de experiencia no existente")

    def subir_nivel(self):
        # Busca en la lista la experiencia requerida para el siguiente nivel
        exp_nivel = self.lista_experiencia()
        for i in range(1, 101):

            if (self.get_experiencia() >= exp_nivel[self.get_nivel() + 1]):
                while (self.get_experiencia() >= exp_nivel[self.get_nivel() + 1]):
                    self.set_nivel(self.get_nivel() + 1)
                    print(f'{self.get_nombre()} ha subido de nivel a {self.get_nivel()}')
                return True
            else:
                return False

    def exp_faltante(self):
        # Revisa cuanto es la experiencia faltante para el siguiente nivel
        lista_nivel = self.lista_experiencia()
        if (self.get_experiencia() >= lista_nivel[self.get_nivel()] and self.get_experiencia() <=
                lista_nivel[self.get_nivel() + 1]):
            dif_exp = lista_nivel[self.get_nivel()] - self.get_experiencia()
            print("Experiencia faltante para subir de nivel es:", dif_exp)
        elif self.get_nivel() == 100:
            print(f'Experiencia faltante para subir de nivel es: 0')
        else:
            print(f'La experiencia faltante no se encuentra entre el rango de los niveles '
                  f'({str(self.get_nivel())}-{str(self.get_nivel() + 1)})')

    def subir_exp(self, experiencia_ganada):
        experiencia_total = self.get_experiencia() + experiencia_ganada
        self.set_experiencia(experiencia_total)

    def __str__(self):
        return f'Pokemon: {self.pokemon}\n' \
               f'Tipo: {self.tipo}\n' \
               f'Nombre: {self.get_nombre()}\n' \
               f'Nivel: {str(self.get_nivel())}\n' \
               f'Experiencia: {str(self.get_experiencia())}\n' \
               f'Movimientos: {str(self.get_movimientos_guardados())}'