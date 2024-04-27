
tablero = [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)

def hacer_movimiento(tablero, fila, columna, jugador):
    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador
    else:
        print('Esa casilla ya está ocupada.')


hacer_movimiento(tablero, 0, 0, 'X')
hacer_movimiento(tablero, 1, 1, 'X')
hacer_movimiento(tablero, 2, 2, 'X')
hacer_movimiento(tablero, 0, 1, 'O')
hacer_movimiento(tablero, 0, 2, 'O')
hacer_movimiento(tablero, 2, 0, 'O')

imprimir_tablero(tablero)


print("********************")

calificaciones = [[0 for _ in range(4)] for _ in range(5)]


calificaciones = [
    [85, 90, 100, 92],  # Estudiante 1
    [88, 76, 93, 87],  # Estudiante 2
    [89, 67, 86, 94],  # Estudiante 3
    [92, 88, 79, 75],  # Estudiante 4
    [76, 85, 88, 89]   # Estudiante 5
]


for i in range(5):
    nota_final = sum(calificaciones[i]) / 4
    print(f"La nota final del estudiante {i+1} es {nota_final:.2f}")

print("********************")


reservas = [[0 for _ in range(20)] for _ in range(4)]

def reservar(horario, espacio):
   
    if 1 <= horario <= 4 and 1 <= espacio <= 20:
       
        horario -= 1
        espacio -= 1

       
        if reservas[horario][espacio] == 0:
           
            reservas[horario][espacio] = 1
            print(f"Has reservado el asiento {espacio+1} en el horario {horario+1}.")
        else:
            print("Lo siento, ese espacio ya está reservado.")
    else:
        print("Por favor, introduce un horario y un espacio válidos.")

reservar(2, 5)
reservar(2, 5)
reservar(1, 4)
reservar(4, 5)