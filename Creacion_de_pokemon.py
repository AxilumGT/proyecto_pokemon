from Lista_pokemon import *
from Lista_de_movimientos import *
import numpy as np
def creacion_de_pokemon_propio():
    pokemon = False
    while pokemon is False:
        desplegar_lista_pokemons()
        seleccionar_pokemon = input('¿Cual pokémon desea seleccionar?:')
        nombre = input(f'Introduzca el nuevo nombre de {seleccionar_pokemon}:')
        nivel = int(input(f'Introduzca el nivel de {nombre} en el rango (1-100):'))
        pokemon = verificacion_de_pokemon(pokemon=seleccionar_pokemon, nivel=nivel, nombre=nombre,
                                          movimientos_guardados=[], experiencia=0)
    return pokemon
def creacion_de_pokemon_rival():
    pokemon_rival = False
    while pokemon_rival is False:
        desplegar_lista_pokemons()
        seleccionar_pokemon = input('¿Cual pokémon desea seleccionar?:')
        nombre = input(f'Introduzca el nuevo nombre de {seleccionar_pokemon}:')
        nivel = int(input(f'Introduzca el nivel de {nombre} en el rango (1-100):'))
        pokemon_rival = verificacion_de_pokemon(pokemon=seleccionar_pokemon, nivel=nivel, nombre=nombre,
                                          movimientos_guardados=[], experiencia=0)
    return pokemon_rival
def desplegar_lista_de_ventajas(tipo_de_movimiento):

    lista = {
        'fuego': ['planta', 'hielo', 'bicho', 'acero'],
        'agua': ['fuego', 'tierra', 'roca'],
        'normal': None,
        'planta': ['tierra', 'roca', 'agua'],
        'electrico': ['agua', 'volador'],
        'hielo': ['planta', 'tierra', 'volador', 'dragón'],
        'lucha': ['normal', 'hielo', 'roca', 'siniestro', 'acero'],
        'veneno': ['veneno', 'hada'],
        'bicho': ['planta', 'psiquico', 'siniestro'],
        'dragón': ['dragón', 'hielo'],
        'hada': ['dragón', 'lucha', 'siniestro'],
        'fantasma': ['fantasma', 'psiquico'],
        'psiquico': ['lucha', 'veneno'],
        'siniestro': ['fantasma', 'psiquico'],
        'tierra':['acero', 'electrico', 'roca', 'veneno', 'fuego'],
        'roca':['bicho', 'fuego', 'hielo', 'volador'],
        'volador':['bicho', 'lucha', 'planta'],
        'acero':['hada', 'hielo', 'roca'],
    }

    return lista[tipo_de_movimiento]
def desplegar_lista_de_desventajas(tipo_de_movimiento):
    lista = {
        'fuego': ['agua', 'dragón', 'fuego', 'roca'],
        'agua': ['agua', 'dragón', 'planta'],
        'normal': ['acero', 'roca'],
        'planta': ['acero', 'bicho', 'dragón', 'fuego', 'planta', 'veneno', 'volador'],
        'electrico': ['dragón', 'electrico', 'planta'],
        'hielo': ['acero', 'agua', 'fuego', 'hielo'],
        'lucha': ['bicho', 'hada', 'psiquico', 'veneno', 'volador'],
        'veneno': ['fantasma', 'roca', 'tierra', 'veneno'],
        'bicho': ['acero', 'fantasma', 'fuego', 'hada', 'lucha', 'veneno', 'volador'],
        'dragon': ['dragón', 'hielo'],
        'hada': ['acero', 'fuego', 'veneno'],
        'fantasma': ['siniestro'],
        'psiquico': ['acero', 'psiquico'],
        'siniestro': ['hada', 'lucha', 'siniestro'],
        'tierra': ['bicho', 'planta'],
        'roca': ['acero', 'lucha', 'tierra'],
        'volador': ['acero', 'electrico', 'roca'],
        'acero': ['acero', 'agua', 'electrico', 'fuego'],
    }
    return lista[tipo_de_movimiento]
def desplegar_lista_de_inmunes(tipo_movimiento):
    lista = {
        'electrico':'tierra',
        'normal':'fantasma',
        'lucha':'fantasma',
        'dragón':'hada',
        'psiquico':'siniestro',
        'veneno':'acero',
        'fantasma':'normal'
    }
    if tipo_movimiento in lista:
        return lista[tipo_movimiento]
def evaluando_listas_ventajas(tipo_de_movimiento, tipo_del_receptor, tipo_atacante):
    multiplicador = 1.0
    contador_lista = 0
    lista_efectivos = desplegar_lista_de_ventajas(tipo_de_movimiento)
    lista_ineficaz = desplegar_lista_de_desventajas(tipo_de_movimiento)
    lista_inmune = desplegar_lista_de_inmunes(tipo_de_movimiento)
    if type(tipo_del_receptor) == list:
        while contador_lista < len(tipo_del_receptor):
            if tipo_del_receptor[contador_lista] in lista_efectivos:
                multiplicador *= 2.0
                contador_lista += 1
            elif tipo_del_receptor[contador_lista] in lista_ineficaz:
                multiplicador = multiplicador / 2
                contador_lista += 1
            elif tipo_del_receptor[contador_lista] in lista_inmune:
                multiplicador = 0
                return multiplicador
            else:
                contador_lista += 1
    else:
        if tipo_del_receptor in lista_efectivos:
            multiplicador *= 2.0
            contador_lista += 1
        elif tipo_del_receptor in lista_ineficaz:
            multiplicador = multiplicador / 2
            contador_lista += 1
        elif tipo_del_receptor in lista_inmune:
            multiplicador = 0
            return multiplicador

    if type(tipo_atacante) == list:
        for elemento in tipo_atacante:
            if elemento == tipo_de_movimiento:
                multiplicador *= 1.5

    if tipo_atacante == tipo_de_movimiento:
        multiplicador *= 1.5

    return multiplicador

def acierta_movimiento(precision):
    #Probabilidad de que acierte dependiendo la precision
    return np.random.choice([True, False], size=1, p=[precision / 100, 1 - (precision / 100)])

def calcular_danio(tipo_de_ataque_movimiento, potencia, multiplicador, atributosPokemonJ, atributosPokemonRival):
    if tipo_de_ataque_movimiento == 'atq':
        # Diferencia = Defensa (oponente) - Ataque (usuario)
        diferencia = atributosPokemonRival[2] - atributosPokemonJ[1]
        danio_total = int(multiplicador * diferencia * potencia / 50)
        if diferencia >= 0:
            diferencia = -1
            danio_total = int(multiplicador * diferencia * potencia / 40)
            return danio_total

        else: return danio_total

    elif tipo_de_ataque_movimiento == 'atq esp':
        # Diferencia especiales = Defensa especial (oponente) - Ataque especial (usuario)
        diferencia_especiales = atributosPokemonRival[4] - atributosPokemonJ[3]
        danio_total = int(multiplicador * diferencia_especiales * potencia / 50)
        if diferencia_especiales >= 0:
            diferencia_especiales = -1
            danio_total = int(multiplicador * diferencia_especiales * potencia / 50)
            return danio_total

        else: return danio_total

def preparando_movimiento(PokemonJ, PokemonRival):
    print(PokemonJ.get_movimientos_guardados)
    opcion = int(input(f'Seleccione el movimiento deacuerdo al orden mostrado entre los números (1-4):'))
    # Movimiento preparado va obtener los valores de potencia, precisión, tipo, etc, del movimiento
    # Nombre:[Potencia, precision, pp, elemento, tipo(atq/atq esp/especial), efecto, probabilidad del efecto en %
    movimiento_preparado = diccionario_movimientos(PokemonJ.get_movimientos_guardados[opcion - 1])

    if acierta_movimiento(movimiento_preparado[1]) == True:
        multiplicador = evaluando_listas_ventajas(movimiento_preparado[3], PokemonJ.tipo, PokemonRival.tipo)
        return calcular_danio(movimiento_preparado[4], movimiento_preparado[0], multiplicador, PokemonJ.calcular_atributos(),
                       PokemonRival.calcular_atributos())
    else:
        return False

def preparando_movimiento_rival(PokemonRival, PokemonJ):
    contador = 0
    lista_probabilidad = []
    while contador < len(PokemonRival.get_movimientos_guardados):
        lista_probabilidad.append(1 / len(PokemonRival.get_movimientos_guardados))
        contador += 1

    opcion = np.random.choice(PokemonRival.get_movimientos_guardados, size=1, p=lista_probabilidad)
    # Movimiento preparado va obtener los valores de potencia, precisión, tipo, etc, del movimiento
    # Nombre:[Potencia, precision, pp, elemento, tipo(atq/atq esp/especial), efecto, probabilidad del efecto en %
    movimiento_preparado = diccionario_movimientos(PokemonRival.get_movimientos_guardados[opcion])

    if acierta_movimiento(movimiento_preparado[1]) == True:
        multiplicador = evaluando_listas_ventajas(movimiento_preparado[3], PokemonRival.tipo, PokemonJ.tipo)
        return calcular_danio(movimiento_preparado[4], movimiento_preparado[0], multiplicador,
                              PokemonRival.calcular_atributos(), PokemonJ.calcular_atributos())
    else: return False

def calcular_velocidad(velocidadUsuario, velocidadRival):
    if velocidadUsuario >= velocidadRival: return True
    else: return False

def danio(PokemonReceptor, danioUsuario, vidaReceptor):
    if danioUsuario != False:
        vidaReceptor -= danioUsuario
        print(f'Daño recibido: {vidaReceptor}')
        print(f'Vida restante {PokemonReceptor.get_nombre}: {vidaReceptor}')
        return vidaReceptor
    else:
        print(f'{PokemonReceptor.get_nombre} ha esquivado el movimiento')
        return vidaReceptor

def combate_1vs1(PokemonJ1, PokemonRival):
    # [0,1,2,3,4,5]
    # [PS, Ataque, Defensa, Ataque especial, Defensa especial, Velocidad]
    contador_de_turnos = 1
    atributos_de_batalla_j1 = PokemonJ1.calcular_atributos()
    atributos_de_batalla_rival = PokemonRival.calcular_atributos()
    vida_total_j1 = atributos_de_batalla_j1[0]
    vida_total_rival = atributos_de_batalla_rival[0]
    vida_combate_usuario = vida_total_j1
    vida_combate_rival = vida_total_rival

    while vida_combate_usuario > 0 or vida_combate_rival > 0:
        print(f'Turno {contador_de_turnos}')
        danio_usuario = preparando_movimiento(PokemonJ1, PokemonRival)
        # Si la velocidad del usuario es mayor que la del rival, inicia el usuario
        if calcular_velocidad(atributos_de_batalla_j1[5], atributos_de_batalla_rival[5]) == True:
            vida_combate_rival = danio(PokemonRival, danio_usuario, vida_combate_rival)
            danio_rival = preparando_movimiento_rival(PokemonRival, PokemonJ1)
            vida_combate_usuario = danio(PokemonJ1, danio_rival, vida_combate_usuario)
        else:
            danio_rival = preparando_movimiento_rival(PokemonRival, PokemonJ1)
            vida_combate_usuario = danio(PokemonJ1, danio_rival, vida_combate_usuario)
            vida_combate_rival = danio(PokemonRival, danio_usuario, vida_combate_rival)

        contador_de_turnos += 1
    if vida_combate_rival <= 0:
        experiencia_ganada = vida_total_rival * 10
        print(f'{PokemonJ1.get_nombre} ha ganadado {experiencia_ganada} de experiencia')
        PokemonJ1.subir_exp(experiencia_ganada)
        if PokemonJ1.subir_nivel() is True:
            if PokemonJ1.evolucion() is not False:
                PokemonJ1 = PokemonJ1.evolucion()
                return PokemonJ1
    else:
        print(f'Has fracasado en el combate')