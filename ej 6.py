import os

def main():
    opcion = input("introcuce 1 para crear un fichero si no existe:\n introduce un 2 para consultar el tlf de un cliente:\n introduce un 3 para añadir un tlf de un cliente: \n y el 4 para eliminar el tlf de un cliente:")
    if opcion == '1':
        f = open('listin.txt', 'w+')
        f.close()
    if opcion == '2':
        f = open('listin.txt', 'r')
        nombre = input("introduce el nombre del contacto del que quieres saber el numero:")
        for linea in f:
            campos = linea.split(' ')
            if nombre == campos[0]:
                print(campos[1])
        f.close()
    if opcion == '3':
        f = open('listin.txt', 'a+')
        nombre1 = input("introduce un nombre")
        numero = input("introduce el numero de " + nombre1)
        f.write(nombre1 + " " + numero)
        f.close()
    if opcion == '4':
        f = open('listin.txt', 'r')
        nombre = input("introduce el nombre del contacto del que quieres borrar:")
        nombres = []
        telefonos = []

        for linea in f:
            campos = linea.split(' ')
            if nombre != campos[0]:
                nombres.append(campos[0])
                telefonos.append(campos[1])

        f.close()
        os.remove('listin.txt')
        f2 = open('listin.txt', 'w')

        i = 0
        while i < len(nombres):
            f2.write(nombres[i] + ' ' + telefonos[i])
            i += 1

        f2.close()

        

#TODO ver si hay que hacer 'ifs' o 'if/else if? depura/debuguea
#TODO dentro de cada if, el código que hay habría que sacarlo en una nueva funcion.




if __name__ == "__main__":
    main()