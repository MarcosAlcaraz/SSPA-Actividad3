# Actividad 2 - Python
# A) Programa tres funciones para calcular el area del Cuadrado, Triangulo y Circulo.
# Alcaraz Valdivia Marcos Fernando
# Seminario de Solución de Problemas de Algoritmia
# NRC: 59928 - Profesor: Sanchez Estrada Jairo Cain
# 29 - 09 - 2022

def areaCuadrado():
    print("______________________________\nArea Cuadrado\nEscribe el valor del eje x:")
    a = int(input())
    print("Escribe el valor del eje y:")
    b = int(input())
    print("El area del cuadrado es: ", a*b)

def areaTriangulo():
    print("______________________________\nArea Triangulo\nEscribe el valor de la base:")
    a = int(input())
    print("Escribe el valor de la altura:")
    b = int(input())
    print("El area del Triangulo es: ", (a*b)/2)

def areaCirculo():
    print("______________________________\nArea Circulo\nEscribe el radio del circulo:")
    a = int(input())
    print("El area del Circulo es: ", 3.14159265*(a**2), "\n______________________________\n")

areaCuadrado()
areaTriangulo()
areaCirculo()

print("\n\n\n\nREALIZADO POR ALCARAZ VALDIVIA MARCOS FERNANDO\n\n\n\n")