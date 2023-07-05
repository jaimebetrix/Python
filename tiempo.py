import time

    # Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle - usar: time.sleep (1)

# Escribe una función de impresión con el mensaje final.
def contar():
    try:
        for i in range(1,6):
            time.sleep(5)
            print(i,'Mississippi')
    
        print("¡Listos o no, ahí voy!")
    except Exception as e:
        print("Error - ",e)
        
contar()