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

    def list_poke_habilidad(self,endpoint ,habilidad):
        response = requests.get(self.API + endpoint + "/" + habilidad)
        self.lista_pokemon = response.json()
        filtrado_habilidad = []
        
        for nombre in self.lista_pokemon["pokemon"]:
            filtrado_habilidad.append(nombre["pokemon"]["name"])
            
        for lista in filtrado_habilidad:
            response = requests.get(self.API + "pokemon/" + lista)
            dato = response.json()
            print(f"Ficha de {lista}")
            self.print_pokemon(dato)

    def list_poke_habitad(self,endpoint ,habitad):
        response = requests.get(self.API + endpoint + "/" + habitad)
        self.lista_pokemon = response.json()
        filtrado_habitad = []
        
        for habi in self.lista_pokemon["pokemon_species"]:
            filtrado_habitad.append(habi["name"])
        
        for lista in filtrado_habitad:
            response = requests.get(self.API + "pokemon/" + lista)
            dato = response.json()
            print(f"Ficha de {lista}")
            self.print_pokemon(dato)


    def list_poke_tipo(self):
        pass

    def print_pokemon(self,dato):
        
        print("-"*20)
        print(f'Nombre: {dato["name"]}')
        print("Habilidades: ")
        for i,var in enumerate(dato["abilities"], start=1):
            print(f'{i}) {var["ability"]["name"]}')
        # for var in dato["sprites"]:
        #     print(var["front_default"])
        print("-"*20)
        
    def _continuar(self):
        pass
    

def run():
    print(Bienvenida)

    API = "https://pokeapi.co/api/v2/"
    
    endpoint = ""

    pokeAPi = PokeApi(API)

    while True:
        print(Menu)

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            Title = '''
            ||||||||||||||||||||||||||||||||||||||||||||||
            ||||     LISTAR POKEMON POR HABILIDAD     ||||
            ||||||||||||||||||||||||||||||||||||||||||||||
            '''
            print(Title)
            
            habilidad = input("Ingrese una habilidad: ")
            endpoint = "ability"
            pokeAPi.list_poke_habilidad(endpoint, habilidad)
        elif opcion == 4:
            Title = '''
            ||||||||||||||||||||||||||||||||||||||||||||||
            ||||      LISTAR POKEMON POR HABITAD      ||||
            ||||||||||||||||||||||||||||||||||||||||||||||
            '''
            print(Title)
            
            habitad = input("Ingrese una habitad: ")
            print("\n")
            print("-"*20)
            endpoint = "pokemon-habitat"
            pokeAPi.list_poke_habitad(endpoint, habitad)
        elif opcion == 5:
            pass
        elif opcion == 6:
            break
        else:
            print("La opcion no es correcta, vuelva a selecionar: ")


if __name__ == '__main__':
    run()