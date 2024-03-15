#Fizz Buzz
"""
esccribe un programa que muestre por consola
los numeros del 1 al 100 con un salto de linea sustituyendo los siguientes:
multiplo de 3 por la palabra fizz
multiplo de 5 por la palabra buzz
multiplos de 3 y 5 a la vez por la palabra fizzbuzz
"""

def fizzbuzz():
    for index in range (1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()