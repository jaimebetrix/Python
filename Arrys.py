class Estructura:
    def __init__(self):
        self.arreglo = []

    def llenarArreglo(self):
        try:
            dato = int(input("Ingrese la cantidad de número a usar en la lista: "))

            for x in range(dato):
                valor = int(input(f"Ingrese el dato #{x+1} de la lista: "))
                self.arreglo.append(valor)

            print(f"\nArreglo creado con éxito: {self.arreglo}")            

        except ValueError:
            print("Error: Debe ingresar un número en la lista. Lista numérica.")
        except Exception as e:
            print(f"Ha ocurrido un error. {e}")   

if __name__ == "__main__":
    obj = Estructura()
    obj.llenarArreglo()