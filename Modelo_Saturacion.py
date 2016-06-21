# -*- coding: UTF-8 -*-

 

# Modelo de Saturacion

# Kevin Javier Estevez 21411165
import math

 

print "\n\tModelo de Saturacion\n\n"

 

def main():

    cantPoints = input("Ingrese cantidad de puntos conocidos > ")\

 

    if cantPoints < 2:

        print "\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n"

        main()\

 

    points = [[],[]]

    sumXY = 0
    sumX = 0
    sumY = 0
    sumXsumY = 0
    sumXcuadrado = 0
    sumX_cuadrado = 0

 

    for i in range(cantPoints):

        print "\n( x",i,",y",i,")"

        x = float(input("Ingrese 'x' > "))
	x = 1/x
        y = float(input("Ingrese 'y' > "))
	y = 1/y

        points[0].append(x)

        points[1].append(y)
	
	sumXY = sumXY + x*y
	sumX = sumX + x
	sumY = sumY + y
	sumXcuadrado = sumXcuadrado + x*x
    
    sumXsumY = sumX*sumY
    sumX_cuadrado = sumX*sumX

    a1 = (cantPoints*sumXY - sumXsumY)/(cantPoints*sumXcuadrado - sumX_cuadrado)
    a0 = sumY/cantPoints - a1*(sumX/cantPoints)

    alpha = 1/a0
    betha = a1*alpha

    print "y = ",a0," + ",a1,"x"
    print "y = ",alpha,"(x/(",betha," + x))"

 

    

    raw_input()

 

main()
