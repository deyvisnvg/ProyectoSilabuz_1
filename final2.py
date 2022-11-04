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
        self.lista_pokemon = []

    def obtener_pokemon(self, detail_pokemon):
        response = requests.get(self.API + detail_pokemon)
        self.lista_pokemon = response.json()

    def list_poke_generacion(self):
        pass

    def list_poke_forma(self):
        pass

    def list_poke_habilidad(self):
        pass

    def list_poke_hibitad(self):
        pass

    def list_poke_tipo(self):
        pass

    def print_pokemon(self):
        pass
        
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
            pass
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