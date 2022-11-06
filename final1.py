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
        self._lista_libros = []
        with open(self.__nombre_csv, "r") as file:
            reader = csv.DictReader(file)

            for libro in reader:
                if libro["id"] not in self._libros_eliminados:
                    self._lista_libros.append(libro)
        
        print("\n\tMensaje: Se cargó el archivo y se ha Actualizado la lista de datos correctamente!!!")
        
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
                self.print_libros(libro)

            return self._continuar()

        except:
            print(f"\tMensaje: No es posible continuar listando los libros ya que se encuentra incompleto")

    def agregar_libro(self, libros_eliminados):
        self._libros_eliminados = libros_eliminados
        lista_libro = [self.id,self.titulo,self.genero,self.ISBN,self.editorial,self.autores]
        respuesta = input("\nEsta seguro que quiere agregar un nuevo libro(S/N): ")
        try:
            with open(self.__nombre_csv,'a',newline='') as nuevo_libro:
                if respuesta.upper() == "S":
                    objeto_libro = csv.writer(nuevo_libro)
                    objeto_libro.writerow(lista_libro)
                    print("\n\tMensaje: El libro fue agregado correctamente!!")
        except Exception as ex:
            print("Mensaje: Ha ocurrido un error", ex)
        
        return self.leer_archivo()       
                

    def eliminar_libro(self):
        num_libro = input(f"\nDigite el número del libro a eliminar 1 hasta el {len(self._lista_libros)}: ")

        # while num_libro not in (1,2,3):
        #     num_libro = int(input("Debes responder 1, 2 ó 3. Ingresa nuevamente tu respuesta: "))

        Title = '''
        ||||||||||||||||||||||||||||||
        ||||    ELIMINAR LIBRO    ||||
        ||||||||||||||||||||||||||||||
        '''
        print(Title)

        index = [i for i, libro in enumerate(self._lista_libros) if libro["id"] == num_libro]
        
        del self._lista_libros[int(index[0])]
        self._libros_eliminados.append(num_libro)


        print(f"\tMensaje: Se ha eliminado el Libro {num_libro} correctamente!!!")

        return self.leer_archivo()


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
                self.print_libros(linea)
                
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
            self.print_libros(libro)
        
        return self._continuar()

    def buscar_libro2(self):
        Title = '''
        ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        ||||    BUSQUEDA DE LIBRO POR AUTOR, EDITOR O GÉNERO    ||||
        ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
        '''
        print(Title)
        param = input("Ingrese el libro a buscar por autor, editor o género: ")
        for linea in self._lista_libros:
            autor_libro = linea["autores"].split(",")
            if param in autor_libro or param == linea["editorial"] or param == linea["genero"]:     
                self.print_libros(linea)
                
        return self._continuar()

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
                self.print_libros(libro)

        return self._continuar()

    def editar_libro(self,index,lista_libros):
        #self.leer_archivo()
        #index = [i for i,libro in enumerate(self._lista_libros) if libro["id"] == self.id][0]
        self._lista_libros = lista_libros
        
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
            with open(self.__nombre_csv, 'w') as file:
                colum = list(self._lista_libros[0].keys())

                writer = csv.DictWriter(file, fieldnames=colum)
                writer.writeheader()

                writer.writerows(self._lista_libros)
                
        print("\nDatos modificados:")
        print("-"*20,"\n")
        
        self.print_libros(self._lista_libros[index])
        
        return self._continuar()

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
                    file.write(self.print_libros(libro))
        
        Title = '''
        ||||||||||||||||||||||||||||||
        ||||    GUARDAR LIBRO    |||||
        ||||||||||||||||||||||||||||||
        '''
        print(Title)
        print(f"Mensaje: Los Libros se guardaron correctamente!!!")

        return self._continuar()

    def print_libros(self, libro):
        titulo = f"\n\tLIBRO {libro['id']}:\n"
        cuerpo = (f"\tTitle: {libro['titulo']}\n"
                    f"\tGender: {libro['genero']}\n"
                    f"\tISBN: {libro['ISBN']}\n"
                    f"\tEditorial: {libro['editorial']}\n"
                    f"\tAuthors: {libro['autores']}\n")
        espacio = "\t**********" * 5
        print(titulo + cuerpo + espacio)
        
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
            
            while True:
                try:
                    id = int(input("Ingrese Id: "))
                    break
                except ValueError:
                    print("Ingrese un Id correcto\n")
                    
            titulo = input("Ingrese el título: ")
            genero = input("Ingrese el género: ")
            isbn = input("Ingrese el ISBN: ")
            editorial = input("Ingrese la editorial: ")
            autores = input("Ingrese los autores separados por comas: ")
            
            libros_eliminados = libro._libros_eliminados
            
            lista = [id, titulo, genero, isbn, editorial, autores]     
            libro = Libro(*lista)
            
            respuesta = libro.agregar_libro(libros_eliminados)
            if respuesta.upper() == 'N':
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
            Title = '''
            ||||||||||||||||||||||||||||||
            ||||     EDITAR LIBRO     ||||
            ||||||||||||||||||||||||||||||
            '''
            print(Title)
            
            id = input("Ingrese ID del libro a modificar: ")
            print("\nDatos previos:")
            print("-"*20)
            
            lista_libros = libro._lista_libros
            index = [i for i, libro in enumerate(lista_libros) if libro["id"] == id][0]
            
            libro.print_libros(lista_libros[index])
            
            print("\nIngrese nuevos datos:")
            print("-"*20,"\n")
            
            titulo = input("Ingrese el nuevo título: ")
            genero = input("Ingrese el nuevo género: ")
            isbn = input("Ingrese el nuevo ISBN: ")
            editorial = input("Ingrese la nueva editorial: ")
            autores = input("Ingrese los nuevos autores separados por comas: ")
            
            lista = [id, titulo, genero, isbn, editorial, autores]
            libro = Libro(*lista)
            
            respuesta = libro.editar_libro(index,lista_libros)
            if respuesta.upper() == 'N':
                break
            
        elif opcion == 10:
            libro.guardar_libro()
        else:
            print("La opcion no es correcta, vuelva a selecionar: ")


if __name__ == '__main__':
    run()