# -*- coding: UTF-8 -*-

 

# REGLA COMPUESTA DEL TRAPECIO

# Kevin Javier Estevez 21411165

 

print "\n\tREGLA COMPUESTA DEL TRAPECIO\n\n"

 

def main():

    cantPoints = input("Ingrese cantidad de puntos conocidos > ")\

 

    if cantPoints < 2:

        print "\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n"

        main()\

 

    points = [[],[]]

    integs = []

 

    for i in range(cantPoints):

        print "\n( x",i,",y",i,")"

        x = float(input("Ingrese 'x' > "))

        y = float(input("Ingrese 'y' > "))

        points[0].append(x)

        points[1].append(y)

 

    for i in range(cantPoints-1):

        integ = ((points[0][i+1]-points[0][i])/2)*(points[1][i]+points[1][i+1])

        integs.append(integ)

 

    print "\nIntegral: ",sum(integs)

    raw_input()

 

main()
