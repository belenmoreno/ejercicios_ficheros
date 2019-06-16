n = int(input('introduce un numero entero enytre el 1 y el 10: '))
nombre = 'tabla-' + str(n) + '.txt'
fnombre = open(nombre, 'w')
multiplicacion = 1

while multiplicacion <= 10:
    fnombre.write(str(n * multiplicacion)+'\t')
    multiplicacion += 1

fnombre.close()