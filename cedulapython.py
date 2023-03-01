__author__ = "Jose Jaime"

def validaced():
        try:
            ced = input("Ingrese el número de cédula a validar: ")
            prov = int(ced[0:2])
            tercer = int(ced[2])
            cant = len(ced)

            if cant != 10:
                print("La cédula ingresa No cumple con la cantidad de dígitos que le corresponde, tiene",cant,' dígitos, deben ser 10.')
            elif (prov < 1) or (prov > 24):
                print("Los dos primeros dígitos hacen referencia a un código de provincia inválido. Provincia",prov,", No existe.")
            elif (tercer < 1) or (tercer > 5):
                print("El tercer dígito comprende valores del 1 al 5. El dígito",tercer," en esta posición, No es válido.")
            else:
                #print("Desde aquí se garantiza que la cédula cumple con los datos principales.")
                #print("Programar lo que Falta.")
                datoP = 0
                datoI = 0
                for i in range(cant-1):
                    #print("Aqui",i)
                    if (i%2 == 0):
                        temp = int(ced[i])*2
                        if temp > 9:
                            temp = temp -9
                        datoP = datoP + temp 
                    else:
                        datoI = datoI + int(ced[i])*1
                                
                Total = datoP + datoI
                print("Total",Total)
                digito = 10-(Total%10)

                if digito == int(ced[9]):
                    print("La cedula de identidad",ced,", es valida.")
                else:
                    print("La cedula de identidad",ced,", es Invalida.")    

        except Exception as e:
            print('Error:',e)
        
validaced()