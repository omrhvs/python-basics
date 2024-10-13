persona = {"nombre": "Omar", "edad": 21, "ciudad": "Mexico"}

print (persona["nombre"]) # Prints "Omar"
print (persona["edad"]) # Prints 21
print (persona["ciudad"]) # Prints "Mexico"

print (persona.keys()) # Prints dict_keys(["nombre", "edad", "ciudad"])
print (persona.values()) # Prints dict_keys(["Omar", 21, "Mexico"])
print (persona.items()) # Prints dict_keys([("nombre": "Omar"), ("edad": 21), ("ciudad": "Mexico")])

persona.update({"profesion": "Ingeniero"})
print (persona) # Prints {"nombre": "Omar", "edad": 21, "ciudad": "Mexico", "profesion": "Ingeniero"}