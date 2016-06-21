#INTERPOLACION DE LAGRANGE

n = input('Ingrese numero de Puntos: ')
xList = []
yList = []
for i in range(n):
    x = input('Inserte X' + str(i) + ': ')
    y = input('Inserte Y' + str(i) + ': ')
    xList.append(x)
    yList.append(y)

m = input('Ingrese n: ')
x = input('Ingrese x buscado: ')
for p in range(m):
    y = 0.0
    for j in range(n):
        Lx = 1.0
        for k in range(n):
            if k != j:
                Lx = Lx * (x - xList[k]) / (xList[j] - xList[k])
        y = y + yList[j] * Lx
        
print y