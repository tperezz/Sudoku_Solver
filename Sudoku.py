import numpy as np
import copy

class Sudoku_Solver:
    def __init__(self, tablero):
            self.tablero = np.array(tablero)
        

    # Imprimir tablero    
    def imprimir_tablero(self):
        for fila in self.tablero:
            print(" ".join(map(str, fila)))

    # Verificar movimiento válido
    def movimiento_valido(self, fila, col, num):
        # En la fila y columna
        if num in self.tablero[fila, :] or num in self.tablero[:, col]:
            return False

        # En el bloque 3x3
        iniciar_fila, iniciar_columna = 3 * (fila // 3), 3 * (col // 3)
        bloque = self.tablero[iniciar_fila:iniciar_fila+3, iniciar_columna:iniciar_columna+3]
        if num in bloque:
            return False

        return True

    # Encontrar celda vacía
    def encontrar_vacia(self):
        celda_vacia = np.where(self.tablero == 0)
        if len(celda_vacia[0]) > 0:
            return celda_vacia[0][0], celda_vacia[1][0]
        return None

    # Resolver
    def resolver(self):
        pila = [self]  # Usamos una pila para simular la recursión

        while pila:
            juego = pila.pop()
            celda_vacia = juego.encontrar_vacia()

            if not celda_vacia:
                # Si todas las celdas están llenas, entonces el Sudoku está resuelto
                self.tablero = juego.tablero  # Actualizamos el tablero con la solución
                return True

            fila, col = celda_vacia

            for num in range(1, 10):
                if juego.movimiento_valido(fila, col, num):
                    nuevo_juego = juego.crear_copia()  # Usamos la función auxiliar
                    nuevo_juego.tablero[fila][col] = num

                    # Agregar una copia del juego a la pila para simular la recursión
                    pila.append(nuevo_juego)

        # En esta celda aún no hay solución
        return False

    # Función auxiliar para crear copias del juego
    def crear_copia(self):
        return Sudoku_Solver(copy.deepcopy(self.tablero))

"""tablero_inicial = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

juego = Sudoku_Solver(tablero_inicial)
juego.resolver()
juego.imprimir_tablero()"""



