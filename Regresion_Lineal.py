# -*- coding: UTF-8 -*-

 

# Regresion Lineal

# Kevin Javier Estevez 21411165

 

print "\n\tRegresion Lineal\n\n"

 

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

        y = float(input("Ingrese 'y' > "))

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

    print "y = ",a0," + ",a1,"x"

 

    

    raw_input()

 

main()
