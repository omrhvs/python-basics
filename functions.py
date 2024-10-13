# Definition
def saludo():
    print ("Hola, Mundo!")

saludo() # Prints "Hola, Mundo!"

# Parameters and arguments
def saludo2(nombre):
    print(f"Hola, {nombre}!")

saludo2("Omar") # Prints "Hola, Omar!"
saludo2("Blas") # Prints "Hola, Blas!"
saludo2("Oliver") # Prints "Hola, Oliver!"

# Return values
def suma(a, b):
    return a + b

resultado = suma (3, 4)
print (resultado) # Prints 7


# Lambda functions
cuadrado = lambda x: x ** 2
print(cuadrado(5)) # Prints 25

# Variable scope
def funcion():
    variable_local = 10
    print(variable_local) # Accesible only within the funtcion

variable_global = 20

def funcion2():
    print(variable_global) # Accesible from anywhere outside

funcion() # Prints 10
funcion2() # Prints 20
print(variable_global) # Prints 20
#print(variable_local) # Throws an error since this variable is outside the scope



# Docstrings
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args: 
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns: float: El área del rectángulo.
    """
    return base * altura

# Functions with a versatile number of arguments
def suma_variable(*numeros):
        total = 0
        for numero in numeros:
                total += numero
        return total

print(suma_variable(1, 2, 3)) # Imprime 6
print(suma_variable(4, 5, 6, 7)) # Imprime 22