from queue_circular import CircularQueue

size = 10
colaReproduccion = CircularQueue(size)


for i in range(1, size + 1):
    colaReproduccion.enqueue(f'cancion {i}')

while True:
    front = colaReproduccion.front
    currentSong = colaReproduccion.elements[front]
    print('Cola de Reporoduccion:', colaReproduccion)
    print('Reproduciendo:', currentSong)
    print('Seleccione la opcion deseada: \n 1. Siguiente cancion \n 2. Agregar cancion \n 3. Salir')
    opcion = input()
    if opcion == '1':
        print('Reproduciendo:', colaReproduccion.dequeue())
    elif opcion == '2':
        cancion = input('Ingrese el nombre de la cancion: ')
        colaReproduccion.enqueue(cancion)
        print('Se ha agreagado la cancion a la cola de reproduccion: ', cancion)
        print(currentSong)
    elif opcion == '3':
        break
    else:
        print('Opcion invalida')
        continue
    if colaReproduccion.front == -1:
        print('No hay mas canciones en la cola')
        continue
print('Cola de Reproduccion:', colaReproduccion)
print('Ha salido del programa.')
