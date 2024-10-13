# Creation
frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

# Basic operations
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1 | conjunto2
print (union) # Prints {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print (interseccion) # Prints {3}

diferencia = conjunto1 - conjunto2
print (diferencia) # Prints {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print (diferencia_simetrica) # Prints {1, 2, 4, 5}

# Methods
Frutas = {"manzana", "banana", "naranja"}

frutas.add("pera")
print (frutas) # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print (frutas) # Imprime {"manzana",  "naranja", "pera"}

frutas.add("uva")
print (frutas) # Imprime {"manzana", "banana", "naranja", "pera",}

frutas.clear()
print (frutas) # Imprime set()