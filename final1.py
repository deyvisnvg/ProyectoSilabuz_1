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
'''


class Libro:
    #
    def __init__(self, id, titulo, genero, ISBN, editorial, autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores
        self._lista_libros = []
        self.__nombre_csv = "Libros.csv"
        self._libros_eliminados = []

    def leer_archivo(self):
        with open(self.__nombre_csv, "r") as file:
            reader = csv.DictReader(file)

            for libro in reader:
                if libro["id"] not in self._libros_eliminados:
                    self._lista_libros.append(libro)
        
        print("\nMensaje: Se ha cargado los datos del archivo correctamente!!!")
        
        return self._continuar()

    def listar_libro(self):
        Title = '''
        |||||||||||||||||||||||||||||
        ||||    LISTAR LIBROS    ||||
        |||||||||||||||||||||||||||||
        '''
        print(Title)

        try:
            for libro in self._lista_libros:
                print(self._print_libros(libro))

            return self._continuar()

        except:
            print(
                f"Mensaje: No es posible continuar listando los libros ya que se encuentra incompleto")

    def agregar_libro(self):

        lista_libro = [self.id,self.titulo,self.genero,self.ISBN,self.editorial,self.autores]
        agregaono = input("Esta seguro que quiere agregar un nuevo libro(S/N): ")
        try:
            with open(self.__nombre_csv,'a',newline='') as nuevo_libro:
                if agregaono.upper() == "S":
                    objeto_libro = csv.writer(nuevo_libro)
                    objeto_libro.writerow(lista_libro)
                    print("\nMensaje: El libro fue agregado correctamente!!")
            self._continuar()
        except Exception as ex:
            print("Mensaje: Ha ocurrido un error", ex)
        
        self.leer_archivo()       
                

    def eliminar_libro(self):
        num_libro = int(input("\nDigite el número del libro a eliminar 1, 2 ó 3: "))

        while num_libro not in (1,2,3):
            num_libro = int(input("Debes responder 1, 2 ó 3. Ingresa nuevamente tu respuesta: "))

        Title = '''
        ||||||||||||||||||||||||||||||
        ||||    ELIMINAR LIBRO    ||||
        ||||||||||||||||||||||||||||||
        '''
        print(Title)

        del self._lista_libros[num_libro - 1]
        self._libros_eliminados.append(num_libro - 1)


        print(f"\tMensaje: Se ha eliminado el Libro {num_libro} correctamente!!!")
        return self._continuar()

    def buscar_libro(self):
        Title = '''
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||    BUSQUEDA DE LIBRO POR TITULO O ISBN    ||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        '''
        print(Title)
        param = input("Ingrese el libro a buscar por título o ISBN: ")
        for linea in self._lista_libros:
            if param == linea["titulo"] or param == linea["ISBN"]:     
                print(self._print_libros(linea))
                
        return self._continuar()
                
    def ordenar_titulo(self):
        Title = '''
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||       LIBROS ORDENADOS POR TITULO         ||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        '''
        print(Title)
        lista_aux = sorted(self._lista_libros, key=lambda libro:libro["titulo"])
        for libro in lista_aux:
            print(self._print_libros(libro))
        
        return self._continuar()

    def buscar_libro2(self):
        pass

    def buscar_libro3(self):
        num_autor = int(input("\nDigite la cantidad de autores: "))

        Title = '''
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||    BUSCAR LIBROS POR NUMERO DE AUTORES    ||||
        |||||||||||||||||||||||||||||||||||||||||||||||||||
        '''
        print(Title)

        for libro in self._lista_libros:
            count_autor = len(libro['autores'].split(','))
            
            if count_autor == num_autor:
                print(self._print_libros(libro))

        return self._continuar()

    def editar_libro(self):
        pass

    def guardar_libro(self):
        respuesta = input("\nDesea guardar los libros en un archivo txt o csv? \n" +
                            "Seleccione una opcion: 1:txt, 2:csv: ")
        nombre_archivo = input("\nEspecifique el nombre del archivo a generar: ")

        if respuesta == '2' and len(self._lista_libros) > 0:
            with open(nombre_archivo + '.csv', 'w') as file:
                colum = list(self._lista_libros[0].keys())

                writer = csv.DictWriter(file, fieldnames=colum)
                writer.writeheader()

                writer.writerows(self._lista_libros)
        else:
            with open(nombre_archivo + '.txt', 'w') as file:
                for libro in self._lista_libros:
                    file.write(self._print_libros(libro))
        
        Title = '''
        ||||||||||||||||||||||||||||||
        ||||    GUARDAR LIBRO    ||||
        ||||||||||||||||||||||||||||||
        '''
        print(Title)
        print(f"Mensaje: Los Libros se guardaron correctamente!!!")

        return self._continuar()

    def _print_libros(self, libro):
        titulo = f"\n\tLIBRO {libro['id']}:\n"
        cuerpo = (f"\tTitle: {libro['titulo']}\n"
                    f"\tGender: {libro['genero']}\n"
                    f"\tISBN: {libro['ISBN']}\n"
                    f"\tEditorial: {libro['editorial']}\n"
                    f"\tAuthors: {libro['autores']}\n")
        espacio = "\t**********" * 5

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

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            respuesta = libro.leer_archivo()
            if respuesta.upper() == 'N':
                break
        elif opcion == 2:
            respuesta = libro.listar_libro()
            if respuesta.upper() == 'N':
                break
        elif opcion == 3:
            Title = '''
        ||||||||||||||||||||||||||||||
        ||||    AGREGAR LIBRO     ||||
        ||||||||||||||||||||||||||||||
        '''
            print(Title)
            id_edit = input("Ingrese Id: ")
            titulo_edit = input("Ingrese el título: ")
            genero_edit = input("Ingrese el género: ")
            isbn_edit = input("Ingrese el ISBN: ")
            editorial_edit = input("Ingrese la editorial: ")
            autores_edit = input("Ingrese los autores separados por comas: ")
            lista = [id_edit,titulo_edit,genero_edit,isbn_edit,editorial_edit,autores_edit]
            libro = Libro(*lista)
            libro.agregar_libro()
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
            pass
        elif opcion == 8:
            libro.buscar_libro3()
        elif opcion == 9:
            pass
        elif opcion == 10:
            libro.guardar_libro()
        else:
            print("La opcion no es correcta, vuelva a selecionar: ")


if __name__ == '__main__':
    run()