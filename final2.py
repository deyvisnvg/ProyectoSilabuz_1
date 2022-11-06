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
    
    def obtener_filtro_pokemon(self, endpoint):
        lista_pokemons = self.obtener_pokemon(endpoint)
        
        lista_name_filtro = []
        
        for resul in lista_pokemons['results']:
            lista_name_filtro.append(resul['name'])
        
        return lista_name_filtro
        

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

    def list_poke_habilidad(self,endpoint ,habilidad):
        lista_pokemon = self.obtener_pokemon(endpoint + "/" + habilidad)
        filtrado_habilidad = []
        
        for nombre in lista_pokemon["pokemon"]:
            filtrado_habilidad.append(nombre["pokemon"]["name"])
            
        for nom_poke in filtrado_habilidad:
            dato = self.obtener_pokemon(self.detail_pokemon + "/"+ nom_poke)
            print(f"Ficha de {nom_poke}")
            self.print_pokemon(dato)

    def list_poke_habitad(self,endpoint ,habitad):
        
        lista_pokemon = self.obtener_pokemon(endpoint + "/" + habitad)
        filtrado_habitad = []
        
        for habi in lista_pokemon["pokemon_species"]:
            filtrado_habitad.append(habi["name"])
        
        for nom_poke in filtrado_habitad:
            dato = self.obtener_pokemon(self.detail_pokemon + "/" + nom_poke)
            print(f"Ficha de {nom_poke}")
            self.print_pokemon(dato)


    def list_poke_tipo(self):
        pass

    def print_pokemon(self,dato):
        
        print(f"-"*20)
        print(f'Nombre: {dato["name"]}')
        print("Habilidades: ")
        for i,var in enumerate(dato["abilities"], start=1):
            print(f'{i}) {var["ability"]["name"]}')
        print(f'Url-imagen: {dato["sprites"]["front_default"]}')
        print("-"*20)
        
    def _continuar(self):
        respuesta = input("\nDesea continuar? S/N: ")

        while respuesta.upper() not in ("S", "N"):
            respuesta = input(
                "Debes responder s ó n. Ingresa nuevamente tu respuesta: ")

        return respuesta


def run():
    print(Bienvenida)

    API = "https://pokeapi.co/api/v2/"
    
    endpoint = ""

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
            Title = '''
            ||||||||||||||||||||||||||||||||||||||||||||||
            ||||     LISTAR POKEMON POR HABILIDAD     ||||
            ||||||||||||||||||||||||||||||||||||||||||||||
            '''
            print(Title)
            endpoint = "ability"
            
            
            filtro = pokeAPi.obtener_filtro_pokemon(endpoint)
            count = 0
            print("Posibles valores a ingresar")
            print("*"*28 , "\n")
            for i, resultado in enumerate(filtro, start=1):
                if i == count + 5:
                    print("\n")
                    count +=5
                print(f"\t{i}: {resultado}", end=" ")
            
            habilidad = input("\n\nIngrese una habilidad: ")
            while habilidad not in filtro:
                habilidad = input("\n\nHabilidad incorrecta, intente nuevamente: ")
                
            pokeAPi.list_poke_habilidad(endpoint, habilidad)
            
            
        elif opcion == 4:
            Title = '''
            ||||||||||||||||||||||||||||||||||||||||||||||
            ||||      LISTAR POKEMON POR HABITAD      ||||
            ||||||||||||||||||||||||||||||||||||||||||||||
            '''
            print(Title)
            
            endpoint = "pokemon-habitat"
            
            filtro = pokeAPi.obtener_filtro_pokemon(endpoint)
            count = 0
            print("Posibles valores a ingresar")
            print("*"*28 , "\n")
            for i, resultado in enumerate(filtro, start=1):
                if i == count + 5:
                    print("\n")
                    count +=5
                print(f"\t{i}: {resultado}", end=" ")
            
            habitad = input("\n\nIngrese una habitad: ")
            while habitad not in filtro:
                habitad = input("\n\nHabilidad incorrecta, intente nuevamente: ")
            print("\n")
            print("-"*20)
            
            pokeAPi.list_poke_habitad(endpoint, habitad)
        elif opcion == 5:
            pass
        elif opcion == 6:
            break
        else:
            print("La opcion no es correcta, vuelva a selecionar: ")


if __name__ == '__main__':
    run()
