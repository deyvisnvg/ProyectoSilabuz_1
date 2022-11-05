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
    def __init__(self, api):
        self.API = api
        self.lista_generation = []

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
        generation = input("\tIngrese alguna generación: ")

        detail_generation = detail + "/" + generation

        self.lista_generation = self.obtener_pokemon(detail_generation)

        lista_pokemons = []
        for pokemon in self.lista_generation["pokemon_species"][:10]:
            pokemon_species = self.obtener_pokemon(pokemon['url'].replace(self.API, ""))
            pokemon = self.obtener_pokemon(pokemon_species["varieties"][0]["pokemon"]['url'].replace(self.API, ""))

            lista_pokemons.append({
                "name": pokemon['name'],
                # 'ability': 
                "ability": [abiliy['ability']['name'] for abiliy in pokemon['abilities']]
            })

        for pokemon in lista_pokemons:
            self.print_pokemon(pokemon)

    def list_poke_forma(self):
        pass

    def list_poke_habilidad(self):
        pass

    def list_poke_hibitad(self):
        pass

    def list_poke_tipo(self):
        pass

    def print_pokemon(self, pokemon):
        titulo = f"\n\tNombre {pokemon['name']}:\n"
        cuerpo = (f"\tHabilidad: {', '.join(pokemon['ability'])}\n"
                    f"\tUrl imagen: ""\n")
        espacio = "\t*******************" * 3
        
        print(titulo + cuerpo + espacio)
        
    def _continuar(self):
        pass
    

def run():
    print(Bienvenida)

    API = "https://pokeapi.co/api/v2/"

    pokeAPi = PokeApi(API)

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