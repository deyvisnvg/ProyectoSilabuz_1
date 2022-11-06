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

Title = {
    "generacion": '''
        ||||||||||||||||||||||||||||||||||||||||||||||
        ||||    LISTAR POKEMONS POR GENERACIÓN    ||||
        ||||||||||||||||||||||||||||||||||||||||||||||
        ''',
    "forma": '''
        |||||||||||||||||||||||||||||||||||||||||
        ||||    LISTAR POKEMONS POR FORMA    ||||
        |||||||||||||||||||||||||||||||||||||||||
        ''',
    "habilidad": '''
            ||||||||||||||||||||||||||||||||||||||||||||||
            ||||     LISTAR POKEMON POR HABILIDAD     ||||
            ||||||||||||||||||||||||||||||||||||||||||||||
            ''',
    "habitat": '''
            ||||||||||||||||||||||||||||||||||||||||||||||
            ||||      LISTAR POKEMON POR HABITAD      ||||
            ||||||||||||||||||||||||||||||||||||||||||||||
            ''',
    "tipo": '''
        ||||||||||||||||||||||||||||||||||||||||
        ||||    LISTAR POKEMONS POR TIPO    ||||
        ||||||||||||||||||||||||||||||||||||||||
        '''
}

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
        print(Title["generacion"])

        detail = "generation"
        generation = input("\tIngrese alguna generación Ej.[1 al 8]: ")

        while generation not in ('1','2','3','4','5','6','7','8'):
            generation = input(
                "\tLa opcion no es correcta, vuelva a ingresar la generación Ej.[1 al 8]: ")

        detail_generation = detail + "/" + generation
        lista_generation = self.obtener_pokemon(detail_generation)

        for pokemon in lista_generation["pokemon_species"]:
            if pokemon['name'] in self.lista_name_pokemons:
                poke = self.obtener_pokemon(self.detail_pokemon + "/" + pokemon['name'])
                self.print_pokemon(poke)

        self._continuar()

    def list_poke_forma(self):
        print(Title["forma"])

        detail = "pokemon-shape"

        filtro = self.obtener_filtro_pokemon(detail)
        forma = input(f"\tIngrese alguna forma Ej.{filtro[5:11]}: ")
        print("\n")
        while forma not in filtro:
                forma = input("Forma incorrecta, ingrese nuevamente: ")

        detail_forma = detail + "/" + forma
        lista_forma = self.obtener_pokemon(detail_forma)

        for pokemon in lista_forma["pokemon_species"]:
            if pokemon['name'] in self.lista_name_pokemons:
                poke = self.obtener_pokemon(self.detail_pokemon + "/" + pokemon['name'])
                self.print_pokemon(poke)

        self._continuar()

    def list_poke_habilidad(self, endpoint, habilidad):
        response = requests.get(self.API + endpoint + "/" + habilidad)
        self.lista_pokemon = response.json()
        filtrado_habilidad = []

        for nombre in self.lista_pokemon["pokemon"]:
            filtrado_habilidad.append(nombre["pokemon"]["name"])

        for lista in filtrado_habilidad:
            response = requests.get(self.API + "pokemon/" + lista)
            dato = response.json()
            print(f"\n\tFicha de {lista}")
            self.print_pokemon(dato)

    def list_poke_habitad(self, endpoint, habitad):
        response = requests.get(self.API + endpoint + "/" + habitad)
        self.lista_pokemon = response.json()
        filtrado_habitad = []

        for habi in self.lista_pokemon["pokemon_species"]:
            filtrado_habitad.append(habi["name"])

        for lista in filtrado_habitad:
            response = requests.get(self.API + "pokemon/" + lista)
            dato = response.json()
            print(f"\n\tFicha de {lista}")
            self.print_pokemon(dato)

    def list_poke_tipo(self):
        print(Title["tipo"])

        detail = "type"

        filtro = self.obtener_filtro_pokemon(detail)
        tipo = input(f"\tIngrese algun Tipo Ej.{filtro[5:11]}: ")
        print("\n")
        while tipo not in filtro:
                tipo = input("Tipo incorrecto, ingrese nuevamente: ")
                
        detail_tipo = detail + "/" + tipo
        lista_tipo = self.obtener_pokemon(detail_tipo)

        for pokemon in lista_tipo["pokemon"]:
            if pokemon['pokemon']['name'] in self.lista_name_pokemons:
                poke = self.obtener_pokemon(self.detail_pokemon + "/" + pokemon['pokemon']['name'])
                self.print_pokemon(poke)

        self._continuar()

    def print_pokemon(self, dato):
        print("\t", end="")
        print(f"-" * (len(dato["name"]) + 9))
        print(f'\n\tNombre: {dato["name"]}')
        print("\tHabilidades: ")
        for i, var in enumerate(dato["abilities"], start=1):
            print(f'\t  {i}) {var["ability"]["name"]}')
        print(f'\tUrl-imagen: {dato["sprites"]["front_default"]}')
        print("\t---"*10)

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
            pokeAPi.list_poke_forma()
        elif opcion == 3:
            print(Title["habilidad"])
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
            print(Title["habitat"])
            
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
            pokeAPi.list_poke_tipo()
        elif opcion == 6:
            break
        else:
            print("La opcion no es correcta, vuelva a selecionar: ")


if __name__ == '__main__':
    run()
