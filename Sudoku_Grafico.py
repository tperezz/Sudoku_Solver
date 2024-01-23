import tkinter as tk
from tkinter import messagebox
from Sudoku import Sudoku_Solver

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        # Create widgets
        self.crear_widgets()

    def crear_widgets(self):
        # Create entry cells
        self.cuadros = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.cuadros[i][j] = tk.Entry(self.master, width=3, font=('Arial', 14), justify='center', bd=2)
                self.cuadros[i][j].grid(row=i, column=j)

                # For separating the 3x3 blocks visually
                if (j) % 3 == 0 and j < 9:
                    self.cuadros[i][j].grid(padx=(7, 0))
                if (i) % 3 == 0 and i < 9:
                    self.cuadros[i][j].grid(pady=(7, 0))

        # Solving button
        resolver_button = tk.Button(self.master, text="Solve", command=self.obtener_valores_y_resolver)
        resolver_button.grid(row=10, column=4, pady=10)

    def obtener_valores_y_resolver(self):
        # Get the entered values and solve the sudoku
        tablero_original = []
        for i in range(9):
            fila = [int(self.cuadros[i][j].get()) if self.cuadros[i][j].get().isdigit() else 0 for j in range(9)]
            tablero_original.append(fila)

        juego = Sudoku_Solver(tablero_original.copy())  # Create a copy to preserve the original board
        resuelto = juego.resolver()

        if resuelto:
            self.mostrar_resultado(juego.tablero, tablero_original)
        else:
            messagebox.showwarning("Advertencia", "No hay solución para el Sudoku ingresado.")

    # Function for showing results
    def mostrar_resultado(self, tablero_resuelto, tablero_original):
        resultado_window = tk.Toplevel(self.master)
        resultado_window.title("Sudoku Resuelto")

        for i in range(9):
            for j in range(9):
                valor = tablero_resuelto[i][j]
                original = tablero_original[i][j]
                fg_color = "blue" if valor != original else "black"
                label = tk.Label(resultado_window, text=str(valor), width=3, font=('Arial', 14), bd=2, relief="solid", fg=fg_color)

                if (j) % 3 == 0 and j < 9:
                    label.grid(padx=(7, 0))
                if (i) % 3 == 0 and i < 9:
                    label.grid(pady=(7, 0))

                label.grid(row=i, column=j)

        # Some space down the board
        tk.Label(resultado_window, text="", pady=10).grid(row=9)

        # Some more space
        tk.Label(resultado_window, text="", padx=10).grid(row=0, column=10)

# Create the app
root = tk.Tk()
app = SudokuGUI(root)

# Start events loop
root.mainloop()

