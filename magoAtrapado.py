def adivinaNum():
    secret_number = 777
    
    print(
    """
    +==================================+
    | ¡Bienvenido a mi juego, muggle!  |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """)
    numero = int(input("Ingresa un número para adivinar:"))
    while numero != secret_number:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
        numero = int(input("Intenta otro número: "))
    
    print("¡Bien hecho, muggle! Eres libre ahora")
    
adivinaNum()