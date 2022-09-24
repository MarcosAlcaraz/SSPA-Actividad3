# Actividad 2 - Python
# B) Haz un script para pedirle al usuario el día y mes de nacimiento, y de acuerdo a su día y mes de nacimiento mostrar en pantalla su signo zodiacal.
# Alcaraz Valdivia Marcos Fernando
# Seminario de Solución de Problemas de Algoritmia
# NRC: 59928 - Profesor: Sanchez Estrada Jairo Cain
# 29 - 09 - 2022

dia = int(input("Escribe tu dia de nacimiento [1 - 31]\n: "))
mes = int(input("Escribe tu mes de nacimiento [1 - 12]\n: "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    print("Eres Aries\n")
else:
    if (mes == 4 and dia >= 21) or (mes == 5 and dia <= 21):
        print("Eres Tauro.\n")
    else:
        if (mes == 5 and dia >= 22) or (mes == 6 and dia <= 21):
            print("Eres Geminis.\n")
        else:
            if (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
                print("Eres Cancer.\n")
            else:
                if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
                    print("Eres Leo.\n")
                else:
                    if (mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
                        print("Eres Virgo.\n")
                    else:
                        if (mes == 9 and dia >= 24) or (mes == 10 and dia <= 23):
                            print("Eres Libra.\n")
                        else:
                            if (mes == 10 and dia >= 24) or (mes == 11 and dia <= 22):
                                print("Eres Escorpion.\n")
                            else:
                                if (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
                                    print("Eres Sagitario.\n")
                                else:
                                    if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
                                        print("Eres Capricornio.\n")
                                    else:
                                        if (mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
                                            print("Eres Acuario.\n")
                                        else:
                                            if (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
                                                print("Eres Piscis.\n")

print("\n\nREALIZADO POR ALCARAZ VALDIVIA MARCOS FERNANDO\n")