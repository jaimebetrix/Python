def usoBreak():
    try:
        while True:
            word = input("Ingrese una palabra: ")
            if word == "chupacabra":
                break
        print("¡Has dejado el bucle con éxito")
    except Exception as e:
        print("Error - ",e)

usoBreak()