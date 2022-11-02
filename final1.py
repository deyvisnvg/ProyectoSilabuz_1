import csv
from termcolor import colored

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

    def __init__(self, id, titulo, genero, ISBN, editorial, autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores
        self._lista_libros = []

    def leer_archivo(self):
        if(len(self._lista_libros) == 0):
            count = 1
            with open(self.__nombre_csv, "r") as file:
                reader = csv.DictReader(file)

                for libro in reader:
                    if count < 4:
                        self._lista_libros.append(libro)
                    count+=1
            
            print("\nMensaje: Se ha cargado los datos del archivo correctamente!!!")
        else:
            print("\nMensaje: El archivo ya ha sido leído")
        
        return self._continuar()
    def listar_libro(self):
        Title = '''
        |||||||||||||||||||||||||||||
        ||||    LISTAR LIBROS    ||||
        |||||||||||||||||||||||||||||
        '''
        print(Title)

        try:
            for libro in self._lista_libros[:3]:
                self._print_libros(libro)

            return self._continuar()

        except:
            print(
                f"Mensaje: No es posible continuar listando los libros ya que se encuentra incompleto")

    def agregar_libro(self):
        pass

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

        print(f"Mensaje: Se ha eliminado el Libro {num_libro} correctamente!!!")

        return self._continuar()

    def buscar_libro(self):
        pass

    def ordenar_titulo(self):
        pass

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

        for libro in self.lista_libros:
            count_autor = len(libro['autores'].split(','))
            
            if count_autor == num_autor:
                self._print_libros(libro)

        return self._continuar()


    def editar_libro(self):
        pass

    def guardar_libro(self):
        pass

    def _print_libros(self, libro):
        print(colored(f"\n\t LIBRO {libro['id']}:\n", 'yellow', attrs=['bold']))
        print(f"\tTitle: {libro['titulo']}\n")
        print(f"Gender: {libro['genero']}\n")
        print(f"\tISBN: {libro['ISBN']}\n")
        print(f"Editorial: {libro['editorial']}\n")
        print(f"\tAuthors: {libro['autores']}\n")
        print("\t**********" * 5)

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
            pass
        elif opcion == 4:
            respuesta = libro.eliminar_libro()
            if respuesta.upper() == 'N':
                break
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            libro.buscar_libro3()
        elif opcion == 9:
            pass
        elif opcion == 10:
            pass
        else:
            print("La opcion no es correcta, vuelva a selecionar: ")


if __name__ == '__main__':
    run()