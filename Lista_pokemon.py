from Pokedex.Linea_evolutiva_charmander import *
from Pokedex.Linea_evolutiva_squirtle import *
from Pokedex.Linea_evolutiva_bulbasur import *
import numpy as np
def lista_pokemons():
    lista = np.array([
        Bulbasaur, Ivysaur, Venusaur, Venusaur,
        Squirtle, Wartortle, Blastoise, Blastoise,
        Charmander, Charmeleon, Charizard, Charizard_X, Charizard_Y,
    ], dtype=object)
    return lista
def desplegar_lista_pokemons():
    for elemento in lista_pokemons():
        print(elemento.pokemon)
def verificacion_de_pokemon(pokemon, nivel, nombre, movimientos_guardados, experiencia=0):
    for elemento in lista_pokemons():
        if pokemon == elemento.pokemon:
            pokemon_creado = elemento(nivel, nombre, movimientos_guardados, experiencia)
            return pokemon_creado

    print('Pokémon no existe en la lista')
    return False
