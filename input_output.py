# Input
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Hola, " + nombre + "!")
print("Tienes " + edad + "años.")

edad2 = int(input("Ingresa tu edad:"))

if edad2 >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Output
nombre2 = "Omar"
edad3 = 21

print(f"Hola, mi nombre es {nombre2} y tengo {edad3} años.")
