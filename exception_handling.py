# Try
try:
	# Code that might throw and exception
	resultado = 10 / 0 # Division by cero
	print (resultado) 
except ZeroDivisionError:
    print("Error: División por cero")

# Except
try:
	# Code that might throw and exception
	resultado = 10 / 0 # Division by cero
	print (resultado) 
except ZeroDivisionError:
	print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

# Finally
try:
	# Code that might throw and exception
	archivo = open("archivo.txt", "r")
	# Make operations with the file
	print("Archivo encontrado")
except FileNotFoundError:
	print("Error: Archivo no encontrado")
finally:
	archivo.close() # Close the file forever, even if it throws and exception

# Custom exception
registrado = False

def funcion():
	#  Code that might throw an exception
	if not registrado:
	    raise Exception("No se ha registrado")
	
try:
	funcion()
except Exception as e:
	print(f"Error: {str(e)}")
