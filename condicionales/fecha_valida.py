dia = int(input())
mes = int(input())
anio = int(input())

#primero validemos que la cantidad de dias concuerden con el mes
#Caso especial de febrero y año bisiesto

# meses con 30 dias 4, 6, 9, 11
# meses con 31 dias (los demas menos el 2)
# meses con 28-29 dias (el que queda) (2)
#años positivos

mes_es_de_30 = (mes == 4 or mes == 6 or mes == 9 or mes == 11)
mes_es_de_31 = (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)
anio_es_bisiesto = (anio%100 == 0 and anio%400 == 0) or (anio%100 != 0 and anio%4 == 0)
 
if anio > 0:
    if (dia >= 1 and dia <= 30 and mes_es_de_30):
        print("Fecha valida")
    elif (dia >= 1 and dia <= 31 and mes_es_de_31):
        print("Fecha valida") 
    elif (mes == 2):
        if anio_es_bisiesto and (dia >= 1 and dia <= 29):
            print("Fecha valida")
        elif dia >= 1 and dia <= 28:
            print("Fecha valida") 
        else:
            print("Fecha invalida")
    else:
        print("Fecha no valida")
else:
    print("Fecha no valida") 
