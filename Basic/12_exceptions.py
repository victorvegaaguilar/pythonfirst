#### Exceptions Handling ####
number1, number2 = 5, 1

number2 = "33333"

try:
    print(number1 + number2)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")


try:
    print(number1 + number2)
    print("No se ha producido un error")
except ValueError as error:
    print(f"Se ha producido un ValueError2 {error}")
except TypeError as error:
    print(f"Se ha producido un ValueError2 {error}")
except Exception as error:
    print(f"Se ha producido un Error3 {error}")
else: # Opcional
    print("Else")
finally: # Opcional
    print("Finally")


#print(number1 + number2)