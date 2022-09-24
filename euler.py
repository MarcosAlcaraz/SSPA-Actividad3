# Actividad 2 - Python
# C) Haz un script que haga el cálculo del Número "e"
# Alcaraz Valdivia Marcos Fernando
# Seminario de Solución de Problemas de Algoritmia
# NRC: 59928 - Profesor: Sanchez Estrada Jairo Cain
# 29 - 09 - 2022

def factorial(numero):
    f = 1
    #numero = int(input("Escribe un Numero: "))
    if numero != 0:
        for i in range(1, numero + 1):
            f = f * i
    return f


def euler(limite):
    e = 0
    for n in range(limite):
        e = e + 1/factorial(n)
    return e


print("Euler = ", euler(int(input("Escribe un valor para el limite: "))))

print("\n\nREALIZADO POR ALCARAZ VALDIVIA MARCOS FERNANDO\n")