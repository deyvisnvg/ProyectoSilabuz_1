import csv

Tema = '''
    B I E N V E N I D O    R E G I S T R A R    L I B R O S
    =======================================================
'''
Menu = '''
    OPCIONES: 
    
    [1]: Leer Libro.
    [2]: Listar libros.
    [3]: Agregar libro.
    [4]: Eliminar libro.
    [5]: Buscar libro por ISBN o por título.
    [6]: Ordenar libros por título.
    [7]: Buscar libros por autor, editorial o género.
    [8]: Buscar libros por número de autores.
    [9]: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).
   [10]: Guardar libros en archivo de disco duro (.txt o csv).
   [11]: Salir.
'''

Title = {
    "2": '''
        |||||||||||||||||||||||||||||
        ||||    LISTAR LIBROS    ||||
        |||||||||||||||||||||||||||||
        ''',
    "3": '''
        ||||||||||||||||||||||||||||||
        ||||    AGREGAR LIBRO     ||||
        ||||||||||||||||||||||||||||||
        ''',
    "4": '''
        ||||||||||||||||||||||||||||||
        ||||    ELIMINAR LIBRO    ||||
        ||||||||||||||||||||||||||||||
        ''',
    "5": '''
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||    BUSQUEDA DE LIBRO POR TITULO O ISBN    ||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        ''',
    "6": '''
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||       LIBROS ORDENADOS POR TITULO         ||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        ''',
    "7": '''
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||    BUSQUEDA DE LIBRO POR AUTOR, EDITORIAL O GÉNERO    ||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        ''',
    "8": '''
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||    BUSCAR LIBROS POR NUMERO DE AUTORES    ||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        ''',
    "9": '''
        ||||||||||||||||||||||||||||||
        ||||     EDITAR LIBRO     ||||
        ||||||||||||||||||||||||||||||
        ''',
    "10": '''
        ||||||||||||||||||||||||||||||
        ||||    GUARDAR LIBRO    |||||
        ||||||||||||||||||||||||||||||
        ''',
}


class Libro:
    nombre_csv = "Libros.csv"
    nombre_txt = "Libros.txt"

    def __init__(self, id, titulo, genero, ISBN, editorial, autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores
        self._lista_libros = []
        self._libros_eliminados = []
        self.archivo_actual = ""

    def leer_archivo(self, estado):
        if estado == 1:
            if len(self._lista_libros) >= 1:
                print(f"\n\tMensaje: El archivo {self.archivo_actual} ya fue cargado!...\n")
                return self._continuar()

            leer = input("\nDesea leer el libro por 1:txt o 2:csv?: ")

            while leer not in ('1', '2'):
                leer = input("Opción incorrecta!. Desea leer el libro por 1:txt o 2:csv?: ")
            
            if leer == '1':
                archivo = self.nombre_txt
            elif leer == '2':
                archivo = self.nombre_csv
            
            self.archivo_actual = archivo

        self._lista_libros = []
        with open(self.archivo_actual, 'r') as file:
            reader = csv.DictReader(file)

            for libro in reader:
                if libro["id"] not in self._libros_eliminados:
                    self._lista_libros.append(libro)
        
        print("\n\tMensaje: Se cargó el archivo y se ha Actualizado la lista de datos correctamente!!!")
        
        return self._continuar()

    def listar_libro(self):
        print(Title["2"])

        if len(self._lista_libros) == 0:
            print("\tDatos vacíos, debe de Leer el Libro antes de Ordenar (Opción 1)")
            return self._continuar()

        try:
            for libro in self._lista_libros:
                print(self.print_libros(libro))

            return self._continuar()

        except:
            print(f"\tMensaje: No es posible continuar listando los libros ya que se encuentra incompleto")

    def agregar_libro(self, libros_eliminados, archivo_actual):
        self.archivo_actual = archivo_actual
        self._libros_eliminados = libros_eliminados
        estado = 0

        lista_libro = [self.id,self.titulo,self.genero,self.ISBN,self.editorial,self.autores]
        respuesta = input("\nEsta seguro que quiere agregar un nuevo libro(S/N): ")
        try:
            with open(self.archivo_actual, 'a', newline='') as nuevo_libro:
                if respuesta.upper() == "S":
                    objeto_libro = csv.writer(nuevo_libro)
                    objeto_libro.writerow(lista_libro)
                    print("\n\tMensaje: El libro fue agregado correctamente!!")
        except Exception as ex:
            print("Mensaje: Ha ocurrido un error", ex)
        
        return self.leer_archivo(estado)       

    def eliminar_libro(self):
        print(Title["4"])

        if len(self._lista_libros) >= 1:
            num_libro = input(f"\nDigite el número del libro a eliminar: ")

            filtro = [libro['id'] for libro in self._lista_libros]

            while num_libro not in filtro:
                num_libro = input(f"El Libro no existe. Digite nuevamente: ")
        else:
            print("\tDatos vacíos, debe de Leer el Libro antes de Eliminar (Opción 1)")
            return self._continuar()

        index = [i for i, libro in enumerate(self._lista_libros) if libro["id"] == num_libro]
        
        del self._lista_libros[index[0]]
        self._libros_eliminados.append(num_libro)

        print(f"\n\tMensaje: Se ha eliminado el Libro {num_libro} correctamente!!!")

        return self._continuar()

    def buscar_libro(self):
        print(Title["5"])

        if len(self._lista_libros) >= 1:
            param = input("Ingrese el libro a buscar por título o ISBN: ")
        else:
            print("\tDatos vacíos, debe de Leer el Libro antes de Buscar (Opción 1)")
            return self._continuar()

        for linea in self._lista_libros:
            if param == linea["titulo"] or param == linea["ISBN"]:     
                print(self.print_libros(linea))
                
        return self._continuar()
                
    def ordenar_titulo(self):
        print(Title["6"])

        if len(self._lista_libros) == 0:
            print("\tDatos vacíos, debe de Leer el Libro antes de Ordenar (Opción 1)")
            return self._continuar()

        lista_aux = sorted(self._lista_libros, key=lambda libro:libro["titulo"])
        for libro in lista_aux:
            print(self.print_libros(libro))
        
        return self._continuar()

    def buscar_libro2(self):
        print(Title["7"])

        if len(self._lista_libros) >= 1:
            param = input("Ingrese el libro a buscar por autor, editorial o género: ")
        else:
            print("\tDatos vacíos, debe de Leer el Libro antes de Buscar (Opción 1)")
            return self._continuar()

        for linea in self._lista_libros:
            autor_libro = linea["autores"].split(",")
            if param in autor_libro or param == linea["editorial"] or param == linea["genero"]:     
                print(self.print_libros(linea))
                
        return self._continuar()

    def buscar_libro3(self):
        print(Title["8"])

        if len(self._lista_libros) >= 1:
            num_autor = input("\nDigite la cantidad de autores: ")

            filtro = [str(len(libro['autores'].split(','))) for libro in self._lista_libros]

            while num_autor not in filtro:
                num_autor = input(f"No existe el Libro con esa cantidad de Autores. Digite nuevamente: ")
        else:
            print("\tDatos vacíos, debe de Leer el Libro antes de Buscar (Opción 1)")
            return self._continuar()

        for libro in self._lista_libros:
            count_autor = len(libro['autores'].split(','))
            
            if count_autor == int(num_autor):
                print(self.print_libros(libro))

        return self._continuar()

    def editar_libro(self,index,lista_libros, archivo_actual):
        self._lista_libros = lista_libros
        self.archivo_actual = archivo_actual
        
        if self.titulo != "":
            self._lista_libros[index]["titulo"] = self.titulo
        if self.genero != "":
            self._lista_libros[index]["genero"] = self.genero
        if self.ISBN != "":
            self._lista_libros[index]["ISBN"] = self.ISBN
        if self.editorial != "":
            self._lista_libros[index]["editorial"] = self.editorial
        if self.autores != "":
            self._lista_libros[index]["autores"] = self.autores
        
        if len(self._lista_libros) > 0:
            with open(self.archivo_actual, 'w') as file:
                colum = list(self._lista_libros[0].keys())

                writer = csv.DictWriter(file, fieldnames=colum)
                writer.writeheader()

                writer.writerows(self._lista_libros)
                
        print("\nDatos modificados:")
        print("-"*20,"\n")
        
        print(self.print_libros(self._lista_libros[index]))
        
        return self._continuar()

    def guardar_libro(self):
        print(Title["10"])

        if len(self._lista_libros) >= 1:
            respuesta = input("\nDesea guardar los libros en un archivo txt o csv? \n" +
                                "Seleccione una opcion: 1:txt, 2:csv: ")

            while respuesta not in ('1', '2'):
                respuesta = input("Opción incorrecta!. Seleccione una opcion:: 1:txt, 2:csv: ")
                
            if respuesta == '1':
                extension = ".txt"
            elif respuesta == '2':
                extension = ".csv"
        
            nombre_archivo = input("\nEspecifique el nombre del archivo a generar: ")

            if respuesta == '2' and len(self._lista_libros) > 0:
                with open(nombre_archivo + extension, 'w') as file:
                    colum = list(self._lista_libros[0].keys())

                    writer = csv.DictWriter(file, fieldnames=colum)
                    writer.writeheader()

                    writer.writerows(self._lista_libros)
            else:
                with open(nombre_archivo + extension, 'w') as file:
                    for libro in self._lista_libros:
                        file.write(self.print_libros(libro))
            
            print(f"\nMensaje: Los Libros se guardaron correctamente!!!")

            return self._continuar()
        else:
            print(f"\n\tMensaje: Es necesario realizar la opción 1.\n")
            print(f"\t\t     La Lista de Libros se encuentra vacía!\n")
            return self._continuar()

    def print_libros(self, libro):
        titulo = f"\n\tLIBRO {libro['id']}:\n"
        cuerpo = (f"\tTitle: {libro['titulo']}\n"
                    f"\tGender: {libro['genero']}\n"
                    f"\tISBN: {libro['ISBN']}\n"
                    f"\tEditorial: {libro['editorial']}\n"
                    f"\tAuthors: {libro['autores']}\n")
        espacio = "\t**********" * 5
        # print(titulo + cuerpo + espacio)
        
        return titulo + cuerpo + espacio
        
    def _continuar(self):
        respuesta = input("\nDesea continuar? S/N: ")

        while respuesta.upper() not in ("S", "N"):
            respuesta = input("Debes responder s ó n. Ingresa nuevamente tu respuesta: ")

        return respuesta
    

def run():
    print(Tema)
    libro = Libro("", "", "", "", "", "")

    while True:
        print(Menu)

        opcion = input("Seleccione una opcion: ")

        while opcion not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'):
            opcion = input("Opción incorrecta. Seleccione una opción: ")

        opcion = int(opcion)

        if opcion == 1:
            estado = 1
            respuesta = libro.leer_archivo(estado)
            if respuesta.upper() == 'N':
                break
        elif opcion == 2:
            respuesta = libro.listar_libro()
            if respuesta.upper() == 'N':
                break
        elif opcion == 3:
            print(Title["3"])

            libros_eliminados = libro._libros_eliminados
            lista_libros = libro._lista_libros
            archivo_actual = libro.archivo_actual

            if len(lista_libros) >= 1:
                filtro = [int(lib['id']) for lib in lista_libros]

                while True:
                    try:
                        id = int(input("Ingrese un Id: "))

                        while id in filtro:
                            id = int(input("El id ya existe. Ingrese nuevamente: "))

                        break
                    except:
                        print("\nAdvertencia!: El Id es incorrecto!\n")

                titulo = input("Ingrese el título: ")
                genero = input("Ingrese el género: ")
                isbn = input("Ingrese el ISBN: ")
                editorial = input("Ingrese la editorial: ")
                autores = input("Ingrese los autores separados por comas: ")

                lista = [id, titulo, genero, isbn, editorial, autores]     
                libro = Libro(*lista)
                
                respuesta = libro.agregar_libro(libros_eliminados, archivo_actual)
                if respuesta.upper() == 'N':
                    break
            else:
                print(f"\n\tIMPORTANTE!: Es necesario realizar la opción 1.\n")
                print(f"\t\t     Para obtener el archivo y poder agregar un Libro!\n")
                continuar = libro._continuar()
                if continuar.upper() == 'N':
                    break
            
        elif opcion == 4:
            respuesta = libro.eliminar_libro()
            if respuesta.upper() == 'N':
                break
        elif opcion == 5:
            respuesta = libro.buscar_libro()
            if respuesta.upper() == 'N':
                break
        elif opcion == 6:
            respuesta = libro.ordenar_titulo()
            if respuesta.upper() == 'N':
                break
        elif opcion == 7:
            respuesta = libro.buscar_libro2()
            if respuesta.upper() == 'N':
                break
        elif opcion == 8:
            libro.buscar_libro3()
        elif opcion == 9:
            print(Title["9"])

            lista_libros = libro._lista_libros
            archivo_actual = libro.archivo_actual

            if len(lista_libros) >= 1:
                filtro = [int(lib['id']) for lib in lista_libros]

                while True:
                    try:
                        id = int(input("Ingrese ID del libro a modificar: "))

                        while id not in filtro:
                            id = int(input("El id del libro no existe. Ingrese nuevamente: "))

                        break
                    except:
                        print("\nAdvertencia!: El Id del libro es incorrecto!\n")

                print("\nDatos previos:")
                print("-"*20)
                
                index = [i for i, libro in enumerate(lista_libros) if libro["id"] == str(id)][0]
                
                print(libro.print_libros(lista_libros[index]))
                
                print("\nIngrese nuevos datos:")
                print("-"*20,"\n")
                
                titulo = input("Ingrese el nuevo título: ")
                genero = input("Ingrese el nuevo género: ")
                isbn = input("Ingrese el nuevo ISBN: ")
                editorial = input("Ingrese la nueva editorial: ")
                autores = input("Ingrese los nuevos autores separados por comas: ")
                
                lista = [str(id), titulo, genero, isbn, editorial, autores]
                libro = Libro(*lista)
                
                respuesta = libro.editar_libro(index, lista_libros, archivo_actual)
                if respuesta.upper() == 'N':
                    break
            else:
                print(f"\n\tIMPORTANTE!: Es necesario realizar la opción 1.\n")
                print(f"\t\t     Para obtener la Lista de Libros y poder editarlo!\n")
                continuar = libro._continuar()
                if continuar.upper() == 'N':
                    break
            
        elif opcion == 10:
            libro.guardar_libro()
        elif opcion == 11:
            break
        else:
            print("La opcion no es correcta, vuelva a selecionar: ")


if __name__ == '__main__':
    run()