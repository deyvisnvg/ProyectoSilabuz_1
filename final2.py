import requests

Bienvenida = '''
    B I E N V E N I D O    A     L A     P O K E A P I
    ===================================================
'''
Menu = '''
    OPCIONES: 
    
    [1]: Listar pokemons por generación.
    [2]: Listar pokemons por forma.
    [3]: Listar pokemons por habilidad.
    [4]: Listar pokemons por habitat.
    [5]: Listar pokemons por tipo.
    [6]: Salir.
'''


class PokeApi:
    detail_pokemon = "pokemon"
    limit = '1154'

    def __init__(self, api):
        self.API = api
        self.lista_name_pokemons = []

    def obtener_lista_pokemons(self):
        lista_pokemons = self.obtener_pokemon(
            self.detail_pokemon + "/" + f"?offset=0&limit={self.limit}")

        for pokemon in lista_pokemons['results']:
            self.lista_name_pokemons.append(pokemon['name'])

    def obtener_pokemon(self, detail_pokemon):
        response = requests.get(self.API + detail_pokemon)
        lista_pokemon = response.json()

        return lista_pokemon

    def list_poke_generacion(self):
        Title = '''
        ||||||||||||||||||||||||||||||||||||||||||||||
        ||||    LISTAR POKEMONS POR GENERACIÓN    ||||
        ||||||||||||||||||||||||||||||||||||||||||||||
        '''
        print(Title)

        detail = "generation"
        generation = input("\tIngrese alguna generación Ej.[1 al 8]: ")

        while int(generation) > 8:
            generation = input(
                "\tLa opcion no es correcta, vuelva a ingresar Ej.[1 al 8]: ")

        detail_generation = detail + "/" + generation
        lista_generation = self.obtener_pokemon(detail_generation)

        resul_pokemons = []
        for pokemon in lista_generation["pokemon_species"]:
            if pokemon['name'] in self.lista_name_pokemons:
                poke = self.obtener_pokemon(
                    self.detail_pokemon + "/" + pokemon['name'])
                resul_pokemons.append({
                    "name": pokemon['name'],
                    "ability": [abiliy['ability']['name'] for abiliy in poke['abilities']],
                    "url_imagen": poke['sprites']['front_default']
                })

        for pokemon in resul_pokemons:
            self.print_pokemon(pokemon)

        self._continuar()

    def list_poke_forma(self):
        pass

    def list_poke_habilidad(self):
        pass

    def list_poke_hibitad(self):
        pass

    def list_poke_tipo(self):
        pass

    def print_pokemon(self, pokemon):
        titulo = f"\n\tNombre: {pokemon['name']}:\n"
        cuerpo = (f"\tHabilidad: {', '.join(pokemon['ability'])}\n"
                  f"\tUrl imagen: {pokemon['url_imagen']}""\n")
        espacio = "\t*******************" * 3

        print(titulo + cuerpo + espacio)

    def _continuar(self):
        respuesta = input("\nDesea continuar? S/N: ")

        while respuesta.upper() not in ("S", "N"):
            respuesta = input(
                "Debes responder s ó n. Ingresa nuevamente tu respuesta: ")

        return respuesta


def run():
    print(Bienvenida)

    API = "https://pokeapi.co/api/v2/"

    pokeAPi = PokeApi(API)
    pokeAPi.obtener_lista_pokemons()

    while True:
        print(Menu)

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            pokeAPi.list_poke_generacion()
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            break
        else:
            print("La opcion no es correcta, vuelva a selecionar: ")


if __name__ == '__main__':
    run()
