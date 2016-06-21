#REGRESION LINEAL

#n = input('Ingrese numero de Puntos: ')
n = 9
xList = []
yList = []
if 0: #colocar 0 en lugar de 1 para no ingresar los valores
    for i in range(n):
        x = input('Inserte X' + str(i) + ': ')
        y = input('Inserte Y' + str(i) + ': ')
        xList.append(x)
        yList.append(y)

if 1: #colocar 1 en lugar de 0 para no ingresar valores y tomar los de abajo
    xList = [1,2,3,4,5,6,7,8,9]
    yList = [1, 1.5, 2, 3, 4, 5, 8, 10, 13]
    
xy = []
xx = []
y_m_yp = []
sumx = 0
sumy = 0
sumxy = 0
sumxx = 0
for i in range(n):
    sumx += xList[i]
    sumy += yList[i]
    
    valor = xList[i]*yList[i]
    sumxy += valor
    xy.append( valor )
    
    sumxx += xList[i]**2
    xx.append(xList[i]**2)

for i in range(n):
    valor = yList[i] - sumy/n
    valor = valor**2
    y_m_yp.append(valor)

print sumx, sumy, sumxy, sumxx, y_m_yp

a1 = (n*sumxy - sumx*sumy)/(n*sumxx - sumx**2)
a0 = (sumy/n) - a1*(sumx/n)

print a1, 'X +', a0