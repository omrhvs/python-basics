# For

frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print (fruta)


# While

contador = 0

while contador < 5:

    print (contador)
    contador += 1

# Advanced Control Statements - Break
contador = 0

while True:

    print (contador)
    contador += 1
    
    if contador == 5:
            break

# Continue
for i in range(10):

    if i % 2 == 0:
            continue
    print(i)

# Pass
for i in range(5):
    pass