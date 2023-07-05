class python:
    def programa(numero): 
        try:
            numpar, numimpar = 0, 0
            while numero != 0:
                if numero % 2 == 0:
                    numpar += 1
                else:
                    numimpar += 1
                numero = int(input("Ingrese un número: "))
        
        except Exception as e:
            print("Error - ",e)
        
        print("Existiron",numpar,"números Pares.")
        print("Existiron",numimpar,"números Impares.")

dato = int(input("Ingrese un número: "))
obj = python
obj.programa(dato)
