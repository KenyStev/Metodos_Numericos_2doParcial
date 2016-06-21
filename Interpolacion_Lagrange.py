# -*- coding: UTF-8 -*-

# Interpolacion polinomica de Lagrange
# Kevin Estevez - 21411165
# Metodos Numericos

import numpy as np

print "\n\tINTERPOLACION POLINOMICA DE LAGRANGE\n\n"

def prod(A):
    a = 1
    for i in range(len(A)):
        a = a*A[i]
    return a

def main():
    cantPoints = input("Ingrese cantidad de puntos conocidos > ")\

    if cantPoints < 2:
        print "\nCANTIDAD DE PUNTOS CONOCIDOS >= 2\n"
        main()\

    results = []
    points = np.arange(cantPoints*2,dtype=float)
    lfun = np.arange((cantPoints)**2,dtype=float)
    points.shape = (2,cantPoints)
    lfun.shape = (cantPoints,cantPoints)\

    for i in range(cantPoints):
        print "\nx",i,",y",i
        x = float(input("Ingrese 'x' > "))
        y = float(input("Ingrese 'y' > "))
        points[0,i] = x
        points[1,i] = y\

    unkoPoint = float(input("Ingrese 'x' de punto desconocido > "))\

    for i in range(len(points[0])):
        for j in range(len(lfun)):
            if i == j:  lfun[i,j] = 1
            else:  lfun[i,j] = (unkoPoint-points[0,j])/(points[0,i]-points[0,j])\

    for i in range(len(points[1])):
        results.append(prod(lfun[i])*points[1,i])\

    res = sum(results)
    print "\nResultado: 'y' para x =",unkoPoint," :>",res

main()
