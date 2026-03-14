import tkinter as tk
from tkinter import messagebox
from pyswip import Prolog, Variable, Functor, Query

class SudokuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver com Prolog")

        self.prolog = Prolog()
        self.prolog.consult("sudoku.pl")

        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                e = tk.Entry(master, width=2, font=("Arial", 18), justify='center')
                e.grid(row=i, column=j, padx=5, pady=5)
                row.append(e)
            self.entries.append(row)

        self.solve_button = tk.Button(master, text="Resolver", command=self.solve)
        self.solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    def read_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                if val.isdigit() and val != '0':
                    row.append(int(val))
                else:
                    row.append(Variable())
            board.append(row)
        return board

    def solve(self):
        board = self.read_board()

        solve_sudoku_functor = Functor("solve_sudoku", 1)
        q = Query(solve_sudoku_functor(board))

        if q.nextSolution():
            solved_board = board  

            for i in range(9):
                for j in range(9):
                    val = solved_board[i][j]
                    if hasattr(val, 'value'):
                        val = val.value
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(val))
        else:
            messagebox.showinfo("Sudoku", "Nenhuma solução encontrada.")
        q.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
