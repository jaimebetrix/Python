#Hacer un programa que genere un número entero al azar (módulo random) entre 0 y 
#1000, y le vaya pidiendo al usuario que ingrese números enteros para adivinarlo. Si el 
#usuario  ingresa  un  número  menor  que  el  objetivo,  muestra  ¡“Es  más  alto!";  si  el 
#usuario ingresa uno mayor, muestra “Es más bajo!”; si el usuario acierta, muestra 
#“Viva Python!”, y termina. Si el usuario no acertó en 7 intentos, muestre ¡“Alpiste 
#perdiste! Booo” y termine.

from random import randrange
#Inicializar Contador de Intentos en cero
def adivinanza():
    try:
        cont=0;

        #Generar aleatoreamente el número ganador y guardarlo en la variable numGanador
        numGanador = randrange(1001);

        print("Juego de Adivinanza");
        print("Tienes hasta 7 intentos para adividar el número ganador");
        print("Este número se encuentra ente el 0 al 1000");
        print("Premio: Viaje a Qatar FIFA World Cup 2022, Todo Pagado.");
        print("Mucha Suerte");
        #print(numGanador); Descomentar linea 22 para conocer numero ganador
        #Sentencia Repetitiva para realizar 7 veces el proceso de adivinanza
        for x in range(7):
            #Contablizar los intentos
            cont = cont +1;
            #Solicitando al participante el valor de su intento.
            #numParticipante = eval(input("Ingrese su Intento #",(x+1),": "))
            numParticipante = eval(input("Ingrese su Intento: "));
            #Consulto si el valor ingresado es (>, < ó =)
            if numParticipante > numGanador:
                print("Es más bajo!");
            elif numParticipante < numGanador:
                print("¡“Es  más  alto!");
            else:
                print("Viva Python!");
                print("Felicitaciones acertaste el Premio.");
                print("Número Ganador: ",numGanador);
                break;
        #Si los intentos son igual a 7, Mostrar mensaje fallido
        if cont == 7:
            #Si llego a la línea 38 del código del programa,
            #esto significa que el participante agotó sus intentos.
            print("Usted ha agotado sus intentos 7/7.");
            print("El número Ganador es: ",numGanador);
            print("¡“Alpiste perdiste! Booo”");
    except Exception as e:
            print('Error:',e)

adivinanza()





            


