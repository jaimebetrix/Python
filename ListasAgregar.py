# paso 1
Beatles = []
print("Paso 1:", Beatles)
# paso 2
print("Paso 2:", Beatles)
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
# paso 3
print("Paso 3:", Beatles)
for i in range(2):
    integrante = input("Ingrese integrante:")
    Beatles.append(integrante)
# paso 4
print("Paso 4:", Beatles)
for i in range(len(Beatles)-1):
    if Beatles[i] == "Stu Sutcliffe":
        del Beatles[i]
    if Beatles[i] == "Pete Best":
        del Beatles[i]    
# paso 5
print("Paso 5:", Beatles)
Beatles.insert(-1,"Ringo Starr")

# probando la longitud de la lista
print("Los Fav", len(Beatles))
print(Beatles)