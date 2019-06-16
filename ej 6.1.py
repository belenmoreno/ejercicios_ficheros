import os

def opcion_4(nombre):
    f = open('listin.txt', 'r')
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


def opcion_1():
    f = open('listin.txt', 'w+')
    print("Fichero listin.txt creado.")
    f.close()

def opcion_2(nombre):   #dentro del parentesis no tiene xq llamarse igual que la variable de abajo
    f = open('listin.txt', 'r')
        
    for linea in f:
        campos = linea.split(' ')
        if nombre == campos[0]:
            print(campos[1])
    f.close()

def opcion_3(nombre1, numero): #si hay un fichero se tendria que llamar igual que la variable xq no si no no sabe como se llama
    f = open('listin.txt', 'a+')
    
    f.write(nombre1 + " " + numero)
    f.close()

def main():
    opcion = input("introduce 1 para crear un fichero si no existe:\n introduce un 2 para consultar el tlf de un cliente:\n introduce un 3 para añadir un tlf de un cliente: \n y el 4 para eliminar el tlf de un cliente:")
    if opcion == '1':
        opcion_1()

    elif opcion == '2':
        nombre = input("introduce el nombre del contacto del que quieres saber el numero:")
        opcion_2(nombre)

    elif opcion == '3':
        nombre1 = input("introduce un nombre")
        numero = input("introduce el numero de " + nombre1)
        opcion_3(nombre1, numero)
        
    elif opcion == '4':
        nombre = input("introduce el nombre del contacto del que quieres borrar:")
        opcion_4(nombre)
        

#TODO dentro de cada if, el código que hay habría que sacarlo en una nueva funcion.




if __name__ == "__main__":
    main()