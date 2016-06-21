#DIFERENCIAS DIVIDIDAS DE NEWTHON

n = input('Ingrese numero de Puntos: ')
#n = 6
xList = []
yList = []
if 1: #colocar 0 en lugar de 1 para no ingresar los valores
    for i in range(n):
        x = input('Inserte X' + str(i) + ': ')
        y = input('Inserte Y' + str(i) + ': ')
        xList.append(x)
        yList.append(y)
if 0: #colocar 1 en lugar de 0 para no ingresar valores y tomar los de abajo
    xList = [-2,-1,0,2,3,6]
    yList = [-18, -5, -2, -2, 7, 142]     
    
a = []

difdiv = []
temp = []
difdiv = yList
a.append(yList[0])

x = 1
for i in range(1,n):
    for ii in range (1, n-x+1):
        if(i == 1):
            valor = (difdiv[ii] - difdiv[ii-1])/(xList[ii] - xList[ii-x])
            temp.append(valor)
            #print '\t Valor',ii,': ',valor
        else:
            valor = (difdiv[ii] - difdiv[ii-1])/(xList[x+ii-1] - xList[ii-1])
            temp.append(valor)
            #print '\t Valor',ii,': ',valor
        if (ii == 1):
            a.append(valor)
    difdiv = temp;
    x+=1
    temp = []
    #print 'Nueva difdiv: ',difdiv
    #print 'A: ', a
    #print 'x:', x, '|  i:',i, '|  ii:',  ii
    #nada = raw_input( 'Ingrese algo para continuar')
#print a

resultado = ''
for e in range(n):
    resultado += str(a[e])
    for i in range(e):
        resultado += ('(X - ' + str(xList[i]) + ')')
    if (e == n-1):
        break
    resultado += ' + '
print resultado