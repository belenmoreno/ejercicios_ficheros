n = int(input("introduce un numero entero del 1 al 10: "))
numero = 'tabla-' + str(n) + '.txt'
try:
    numeros = open(numero, 'r')
except FileNotFoundError:
    print("este fichero no existe", n)
else:
    print(numeros.read())


n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())
