# Typical pattern exercise

rows = 5
print("1)\n")

"""
Ouput:

    *
    * *
    * * *
    * * * *
    * * * * *

"""

for i in range(0, rows):
    for j in range(0, i + 1):
        print("* ", end = '')
    print("\r")

# Shorter
print("\n\n1.1)\n")

for i in range(1, 6):
    print("* " * i)

print("\n\n2)\n")

"""
Ouput:

            *
          * *
        * * *
      * * * *
    * * * * *

"""

for j in range(1, rows + 1):
    print(" " * (2 * (rows - j)) + "* " * j)


print("\n\n3)\n")

"""
Ouput:

    * * * * *
    * * * *
    * * *
    * *
    *

"""

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("* ", end='')
    print(" ")
