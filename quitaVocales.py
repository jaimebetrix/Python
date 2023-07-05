# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

user_word = input("Ingrese una palabra:")
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter in ('A','E','I','O','U'):
        continue
    print("\n",letter)