my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for i in range(len(my_list)):
    dato = my_list[i]
    if dato in my_list:
        if dato not in new_list:
            new_list.append(dato)
my_list = new_list[:]
print("La lista con elementos únicos:")
print(my_list)