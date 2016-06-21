#TRAZADORES LINEALES

print "Ingrese los valores de x,y en orden; de menor a mayor en x"
n = input('Ingrese numero de Puntos: ')
xList = []
yList = []
for i in range(n):
    x = input('Inserte X' + str(i) + ': ')
    y = input('Inserte Y' + str(i) + ': ')
    xList.append(x*1.00)
    yList.append(y*1.00)

x = input('Ingrese x buscado: ')
cant = len(xList)
pendientes = []

print yList

for i in range (1, cant):
    pend = 0.00000
    temp = 0.00000
    pend = ((yList[i] - yList[i-1])/(xList[i] - xList[i-1]))*1.00
    temp = (yList[i-1]-(pend*xList[i-1]))*1.00
    pendientes.append(pend);
    print pend, 'x + ', temp
    if(x < xList[i] and x > xList[i-1]):
        valor = x*pend + temp
        
print '\nEl valor encontrado es:',valor

